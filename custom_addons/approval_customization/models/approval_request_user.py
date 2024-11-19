from odoo import fields, models

class ApprovalRequest(models.Model):
    _inherit = 'approval.request'
   
    purchase_order_id = fields.Many2one('purchase.order', string='Purchase Order')
    department_name = fields.Many2one('school.classname', string="Class Name", required=True, track_visibility="always")
    
    # Related field to fetch picking state text from purchase order
    picking_state_text = fields.Char(related='purchase_order_id.picking_state_text', string='Picking State Text', store=True)

    def action_create_purchase_order_request_user(self):
        PurchaseOrder = self.env['purchase.order']
        PurchaseOrderLine = self.env['purchase.order.line']
        
        for request in self:
            # Print department name
            print(request.department_name.name)
            
            # Print request name
            print(request.name, 'is SSR id')
            
            # Print requester name
            print(request.request_owner_id.name, 'is requester teacher name')
            
            # Fetch related product lines
            approval_product_lines = self.env['approval.product.line'].search([('approval_request_id', '=', request.id)])
            
            if not approval_product_lines:
                print("No product lines found for request ID:", request.id)
                continue
            
            # Find existing RFQ
            existing_order = PurchaseOrder.search([('origin', '=', request.name), ('state', '=', 'draft')], limit=1)
            
            if existing_order:
                order = existing_order
                # If RFQ exists, update its lines
                existing_lines = PurchaseOrderLine.search([('order_id', '=', order.id)])
                existing_lines.unlink()  # Remove existing lines (optional, or update instead)
            else:
                # Create a new RFQ if it doesn't exist
                order_vals = {
                    'partner_id': request.request_owner_id.partner_id.id,
                    'class_name_po':request.department_name.name,
                    'state': 'draft',  # Initial state
                    'origin': request.name,
                }
                order = PurchaseOrder.create(order_vals)
            
            # Create or update purchase order lines
            for line in approval_product_lines:
                if not line.product_id or line.quantity <= 0:
                    print(f"Skipping line with invalid product or quantity for request ID: {request.id}")
                    continue

                order_line_vals = {
                    'order_id': order.id,
                    'product_id': line.product_id.id,
                    'product_qty': line.quantity,
                    'price_unit': line.product_id.lst_price,  # Use list price or another method to get the unit price
                    'name': line.description or line.product_id.name,
                }
                PurchaseOrderLine.create(order_line_vals)
            
            # Update the approval request state to 'Request Finished'
            request.write({'request_status': 'approved'})
            
            # print("Purchase Order updated with ID:", order.id)
            
            # print("Purchase Order number:", order.picking_state_text, '------------------------------------------------------------------------------------')
            # print("Purchase Order number:", order.name, '------------------------------------------------------------------------------------')
        
        return True
