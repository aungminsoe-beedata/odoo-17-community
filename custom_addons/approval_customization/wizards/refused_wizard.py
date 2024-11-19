from odoo import models, fields, api

class PurchaseOrderRefuseWizard(models.TransientModel):
    _name = 'purchase.order.refuse.wizard'
    _description = 'Refusal Reason Wizard'

    # Reference to the purchase order
    purchase_order_id = fields.Many2one('purchase.order', string="Purchase Order", required=True)

    # Textbox for the refusal reason
    refuse_reason = fields.Char(string="Refusal Reason", required=True)

    def action_confirm_refusal(self):
        """Confirm the refusal reason and update the purchase order state."""
        
        self.purchase_order_id.write({
            'state': 'refused',
            'refuse_reason': self.refuse_reason,
        })
        return True
