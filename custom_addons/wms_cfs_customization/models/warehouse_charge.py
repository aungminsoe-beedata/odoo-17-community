from odoo import models, fields, api


class WarehouseCharge(models.Model):
    _name = "warehouse.charge"
    _description = 'Inventory Warehouse Charge Customization'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string="Charge Type", required=True, tracking=True)
    price = fields.Float(string="Price", required=True, tracking=True)
    currency_id = fields.Many2one('res.currency', string="Currency", required=True, default=lambda self: self.env.company.currency_id.id)
