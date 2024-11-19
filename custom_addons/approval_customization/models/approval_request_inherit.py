from odoo import models, fields

class ApprovalRequestInherit(models.Model):
    _inherit = 'approval.request'  # Inherit from approval.request

    def get_all_approval_request_names(self):
        # Retrieve all approval request records
        approval_requests = self.env['approval.request'].search([])
        
        # Get the names of each approval request
        approval_names = approval_requests.mapped('name')
        
        # For demonstration, you can log the names or process them
        for name in approval_names:
            _logger.info(f"Approval Request Name: {name}")
            print(name,'--------------------------------------------------------------------------')

        return approval_names
