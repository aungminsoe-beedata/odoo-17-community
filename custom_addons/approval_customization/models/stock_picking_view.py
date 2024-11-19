from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    purchase_order_id = fields.Many2one('purchase.order', string='Purchase Order')

    partner_name1 = fields.Char('Name', related="name")
    print(partner_name1,'--------------------------------------------------------------------------------------------------------------------------')
    
    class_name_po = fields.Char(string="SSR Class Name", readonly=True)
    ssr = fields.Char(string="SSR NO.", readonly=True)