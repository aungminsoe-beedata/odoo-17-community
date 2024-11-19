
from odoo import models, fields, api


class wms_cfs_customization(models.Model):
    _inherit = "stock.picking.type"
    _description = 'Inventory Warehouse Customization'

    
  