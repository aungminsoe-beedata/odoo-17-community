from odoo import models, fields


class ProductTemplateView(models.Model):
    _inherit = "product.template"
    _description = 'Inventory Warehouse Charge Customization'

    inv_name = fields.Char(string="INV Name", related='property_stock_inventory.name', store=True)
    inv_id = fields.Many2one(related='property_stock_inventory.location_id', string="INV ID", store=True)


