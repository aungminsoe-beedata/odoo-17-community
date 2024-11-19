from odoo import http


class OdooController(http.Controller):
    @http.route('/odoo_controller/odoo_controller/',auth='public')
    def index(self,**kw):
        try:
            sales_order =http.request.env['sale.order'].search([])
        except:
            return "<h1>Can't Access Api"
        output ="<h1>Sales Orders</h1><ul>"
        for sale in sales_order:
            output+="<li>" +sale['name']+ "</li>"
        output+="</ul>"
        
        return output