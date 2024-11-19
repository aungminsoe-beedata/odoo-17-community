import base64
from datetime import datetime

from xlrd import open_workbook

from odoo import api, fields, models, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.exceptions import UserError


class PurchaseLineImport(models.TransientModel):
    _name = 'purchase.line.import'

    data_file = fields.Binary(string='File', required=True)

    # @api.multi
    def import_file(self):
        context = self._context
        #current_adjustment_id = context['current_adjustment_id']
        file_data = base64.b64decode(self.data_file)
        book = open_workbook(file_contents=file_data)
        sheet = book.sheet_by_index(0)
        keys = [sheet.cell(0, col_index).value for col_index in range(sheet.ncols)]
        dict_list = []
        for row_index in range(1, sheet.nrows):
            d = {keys[col_index]: sheet.cell(row_index, col_index).value 
                 for col_index in range(sheet.ncols)}
            dict_list.append(d)
        product_obj = self.env['product.product']
        move_list = []
        for prod_list in dict_list:

            search_product = product_obj.search([('name','=',prod_list['name'])],limit=1)
            msg = 'Product not exist %s', prod_list['name']
            if not search_product:
                raise UserError(_("Product does not exist %s.") % (prod_list['name']))
            move_list.append({'product_id':search_product.id,
                              'name': str(search_product.name),
                              'product_qty': prod_list['quantity'],
                              'product_uom':search_product.uom_id.id,
                              'price_unit': prod_list['price'],
                              'date_planned':datetime.today().strftime(DEFAULT_SERVER_DATETIME_FORMAT)
                              
                              })
            # prod_list.update({'product_id':search_product.id})
            # prod_list.update({'name':str(search_product.name)})
            # prod_list.update({'product_qty': prod_list['quantity']})
            # prod_list.update({'price_unit': prod_list['price']})

            # prod_list.update({'product_uom':search_product.uom_po_id.id})
           
            # prod_list.update({'date_planned': datetime.today().strftime(DEFAULT_SERVER_DATETIME_FORMAT)})


        create_adjustment_line = self.env['purchase.order'].import_purchase_line(move_list,context['current_order_id'])

        return