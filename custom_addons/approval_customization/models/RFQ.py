from odoo import models, fields, api
class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    # Store the original RFQ number
    rfq_number = fields.Char(string='RFQ Number', readonly=True)

    @api.model
    def create(self, vals):
        # Set the RFQ number if the state is draft
        if vals.get('state', 'draft') == 'draft':
            rfq_number = self.env['ir.sequence'].next_by_code('purchase.order.rfq') or 'New'
            vals['name'] = rfq_number
            vals['rfq_number'] = rfq_number
        return super(PurchaseOrder, self).create(vals)

    def write(self, vals):
        if 'state' in vals:
            for order in self:
                # States that should maintain the RFQ reference number
                rfq_states = ['draft', 'sent', 'to approve', 'refused']
                
                if vals.get('state') in rfq_states:
                    # If moving to an RFQ state, revert to the original RFQ number
                    vals['name'] = order.rfq_number
                elif order.state in rfq_states and vals.get('state') not in rfq_states:
                    # If moving out of an RFQ state, change to a PO number
                    vals['name'] = order.name.replace('RFQ', 'PO', 1)
        return super(PurchaseOrder, self).write(vals)

    
class CreateRfqDirect(models.Model):
    _inherit = 'approval.request'
    
    request_status = fields.Selection([
        ('new', 'Request'),
        ('pending', ''),#hide value
        ('approved', 'Request Finished'),
        ('refused', ''),
        ('cancel', ''),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft',track_visibility = "always")
    
    
    def action_confirm(self):
        self.action_create_purchase_orders()
        res = super(CreateRfqDirect, self).action_confirm()
        return res
        
