from odoo import models, fields, api
from odoo.exceptions import UserError

class WarehouseChargeNote(models.Model):
    _name = "warehouse.charge.note"
    _description = 'Inventory Warehouse Charge Note Customization'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Charge Note",  store=True, copy=False, readonly=True, index=True,
                       default=lambda self: 'New CN')
    GRN_name = fields.Many2one('warehouse.customization', 
                               string="Customer Name", required=True,
                               domain=[('state', '=', 'done')])
    customers = fields.Many2one('res.partner', related="GRN_name.customer",string="Customer", store=True)
    charge = fields.Float('Charge Total', compute='_compute_charge_total', store=True)
    note_line = fields.Many2many('warehouse.product.line', string="Charge Note Lines",domain=[('states', '=', 'done')])

    @api.onchange('customers')
    def _onchange_note_line_type(self):
        if self.customers:
            domain = [('customer', '=', self.customers.name)]  # Use customer ID instead of name
        else:
            domain = []
        return {'domain': {'note_line': domain}}
    @api.depends('note_line.charge_rate')
    def _compute_charge_total(self):
        """Compute the total charge based on the selected note lines."""
        for record in self:
            total_charge = sum(line.charge_rate for line in record.note_line)
            record.charge = total_charge

    charged_date = fields.Date(string="Charged Date")
    state = fields.Selection([
        ('draft', 'To Charge'), 
        ('confirm', 'Charged'), 
        ('cancel', 'Cancelled')],
        string='State', readonly=True,
        help='State of Charge Notes', default="draft")
    
    @api.model
    def create(self, vals):
        """Sequence number generation"""
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('warehouse.charge.note') or 'New'
        return super().create(vals)    
    
    def action_charged(self):
        for record in self:
            matching_lines = record.note_line.filtered(lambda line: line.customer == record.customers)
            if len(matching_lines) == len(record.note_line):
                record.state = 'confirm'
            else:
                raise UserError("Note line of customer name and charge customer must be Same")

    def action_cancel(self):
        for record in self:
            record.state = 'cancel'
    def action_set_tocharge(self):
        for record in self:
            record.state ="draft"
