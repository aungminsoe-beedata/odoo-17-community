from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
     
    state = fields.Selection(selection_add=[('refused', 'Refused')])
    class_name_po = fields.Char(string='Class Name')
    refuse_reason = fields.Char(string="Refusal Reason")
    
    
    def action_request_approve(self):
        """Set the state to 'to approve' to request approval."""
        self.write({'state': 'to approve'})
        return True

    def action_request_refuse(self):
        """Open the wizard to ask for the refusal reason."""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Refusal Reason',
            'res_model': 'purchase.order.refuse.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_purchase_order_id': self.id},
        }
        
    def button_approve(self, force=False):
        # Call the super method to approve the PO
        res = super(PurchaseOrder, self).button_approve(force=force)
        
        # Update the related stock.picking records with "SSR" + Purchase Order name and class_name_po
        for order in self:
            pickings = order.picking_ids
            for picking in pickings:
                picking.ssr = order.origin
                picking.class_name_po = order.class_name_po
               
        return res
        
        
   