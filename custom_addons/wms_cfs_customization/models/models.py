from odoo import models, fields, api,_
import logging
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)
class ProductLineWarningWizard(models.TransientModel):
    _name = 'product.line.warning.wizard'
    _description = 'Product Line Warning Wizard'

    message = fields.Text(string="Message", readonly=True, default="Please provide the Product Line before proceeding!")

    def action_close(self):
        return {'type': 'ir.actions.act_window_close'}

class WarehouseCustomization(models.Model):
    _name = 'warehouse.customization'
    _description = 'Inventory Warehouse Customization'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", store=True, copy=False, readonly=True, index=True,
                       default=lambda self: 'New')
    receive_date = fields.Datetime(string="Receive Date",store=True)
    customer = fields.Many2one('res.partner', string="Customer Name", required=True, tracking=True)
    contract_date = fields.Datetime(string="Contract Date")
    charge_type = fields.Many2one('warehouse.charge', string="Charge Type")
    charge_rate = fields.Float(string="Charge Rate", related="charge_type.price", store=True)
    state = fields.Selection([
        ('draft', 'Draft'), 
        ('ready', 'Ready'), 
        ('done', 'Done'),
        ('cancel', 'Cancelled')],
        string='State', readonly=True,
        help='State of WMS', default="draft"
    )
    currency_id = fields.Many2one('res.currency', string="Currency", required=True, 
                                  default=lambda self: self.env.company.currency_id.id)

    product_line_ids = fields.One2many(
        'warehouse.product.line',  # Related model
        'warehouse_id',            # Foreign key in related model
        string='Product Lines'
    )

    @api.model
    def create(self, vals):
        """Sequence number generation"""
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('warehouse.customization') or 'New'
        return super().create(vals)
    
    @api.depends('name', 'customer')
    def _compute_display_name(self):
        for record in self:
            if record.name:
                customer_info = f"[{record.customer.name}] " if record.customer else ''
                record.display_name = f"{customer_info}{record.name}"
            else:
                record.display_name = False

    def action_draft(self):
        for record in self:
            record.state = 'ready'
            
            
    def action_search(self):
        for record in self:
            if not record.receive_date:
             raise UserError("Please provide the Receive Date before proceeding  ! ")
            # if not record.product_line_ids:
            #     raise UserError(_("Please provide the Product Line before proceeding  !"))
            if not record.product_line_ids:
                return {
                    'type': 'ir.actions.act_window',
                    'res_model': 'product.line.warning.wizard',
                    'view_mode': 'form',
                    'target': 'new',
                }
            for line in record.product_line_ids:
                picking_type = self.env['stock.picking.type'].sudo().search([('code', '=', 'incoming'), ('warehouse_id', '=', line.warehouse_location.id)])
                search_values = [
                    ('origin', '=', self.name),
                    ('picking_type_id', '=', picking_type.id),
                    ('location_dest_id','=', line.lot_stock_id.id)
                ]
                search_result = self.env['stock.picking'].sudo().search(search_values)
                if search_result:
                    self.env['stock.move'].sudo().create({
                    'picking_id': search_result.id,  # Link to the created stock picking
                    'product_id': line.name.id,
                    'picking_type_id': picking_type.id,# Operation type
                    'product_uom_qty': 1,  # Assuming quantity is 1, adjust as necessary
                    'product_uom': line.name.uom_id.id,  # Unit of Measure
                    'location_id': line.lot_stock_id.location_id.id,  # Source Location ID
                    'location_dest_id': line.lot_stock_id.id,  # Destination Location ID
                    'name': line.name.name,  # Name for the stock move
                })
                    search_result.write({'state': 'assigned'})
                else:
                    
                    picking = self.env['stock.picking'].sudo().create({
                    'partner_id': record.customer.id,  # Customer (partner) ID
                    'picking_type_id': picking_type.id,
                    'scheduled_date':record.receive_date ,# Operation type (picking type)
                    'location_id': line.lot_stock_id.location_id.id,  # Source location (mandatory)
                    'origin': self.name,  # Source document reference
                    'location_dest_id': line.lot_stock_id.id,  # Destination Location ID    
                })
                    self.env['stock.move'].sudo().create({
                    'picking_id': picking.id,  # Link to the created stock picking
                    'product_id': line.name.id,
                    'picking_type_id': picking_type.id, # Operation type
                    'product_uom_qty': 1,  # Assuming quantity is 1, adjust as necessary
                    'product_uom': line.name.uom_id.id,  # Unit of Measure
                    'location_id': line.lot_stock_id.location_id.id,  # Source Location ID
                    'location_dest_id': line.lot_stock_id.id,  # Destination Location ID
                    'name': line.name.name,  # Name for the stock move
                })
                picking.write({'state': 'assigned'})    
        record.state = 'done'
               
    def action_cancel(self):
        for record in self:
            record.state = 'cancel'
            
    def action_set_draft(self):
        for record in self:
            record.state = 'draft'
            

class WarehouseProductLine(models.Model):
    _name = 'warehouse.product.line'
    _description = 'Warehouse Product Line'
    
    name = fields.Many2one('product.product', string="Product Name", required=True, copy=False)
    warehouse_location = fields.Many2one('stock.warehouse', string="Warehouse Location")
    lot_stock_id = fields.Many2one(
        'stock.location', 'Location Stock',
        domain="[('usage', '=', 'internal'), ('warehouse_id', '=', warehouse_location)]")
    states = fields.Selection(related='warehouse_id.state', store=True)
    charge_type = fields.Many2one(related='warehouse_id.charge_type', store=True)
    charge_rate = fields.Float(related='warehouse_id.charge_rate', store=True)
    customer = fields.Many2one(related='warehouse_id.customer', store=True)
    contact_date = fields.Datetime(related='warehouse_id.receive_date', store=True)
    receive_date = fields.Datetime(related='warehouse_id.contract_date', store=True)
    picking_type = fields.Many2one(
        'stock.picking.type',
        domain="[('code', '=', 'incoming'), ('warehouse_id', '=', warehouse_location)]",readonly=True
    )

    warehouse_id = fields.Many2one('warehouse.customization', ondelete='cascade', string="Warehouse Reference", required=True)
