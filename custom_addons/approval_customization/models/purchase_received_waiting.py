from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    receipt_state = fields.Selection([
        ('all_received', 'All Received'),
        ('waiting', 'Waiting')
    ], string="Receipt Status", compute="_compute_receipt_state", store=True)
    

    @api.depends('order_line.qty_received', 'order_line.product_qty')
    def _compute_receipt_state(self):
        for order in self:
            all_received = True
            for line in order.order_line:
                if line.qty_received < line.product_qty:
                    all_received = False
                    break
            order.receipt_state = 'all_received' if all_received else 'waiting'

    
    picking_state_text = fields.Char(compute='_compute_picking_state_text', string='Picking State')
    print('Picking State Text------------------------------------------------',picking_state_text)

    @api.depends('picking_ids.state')
    def _compute_picking_state_text(self):
        for order in self:
            if not order.picking_ids:
                order.picking_state_text = ""
            else:
                # Iterate over related pickings and show a corresponding label
                picking_states = set(picking.state for picking in order.picking_ids)
                
                if 'cancel' in picking_states:
                    order.picking_state_text = "Cancelled"
                elif 'done' in picking_states:
                    order.picking_state_text = "Done"
                elif 'assigned' in picking_states:
                    order.picking_state_text = "Ready"
                elif 'confirmed' in picking_states:
                    order.picking_state_text = "Waiting"
                elif 'waiting' in picking_states:
                    order.picking_state_text = "Waiting"
                else:
                    order.picking_state_text = "Draft"
                    
                    
                    
