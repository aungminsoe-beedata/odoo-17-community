import base64
from datetime import datetime

from xlrd import open_workbook

from odoo import api, fields, models, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.exceptions import UserError


class PurchaseLineImport(models.TransientModel):
    _name = 'purchase.line.import'

    data_file = fields.Binary(string='File', required=True)

    @api.multi
    def import_file(self):
        context = self._context
        #current_adjustment_id = context['current_adjustment_id']
        file_data = base64.b64decode(self.data_file)
        book = open_workbook(file_contents=file_data)
        sheet = book.sheet_by_index(0)
        keys = [sheet.cell(0, col_index).value for col_index in xrange(sheet.ncols)]
        dict_list = []
        for row_index in xrange(1, sheet.nrows):
            d = {keys[col_index]: sheet.cell(row_index, col_index).value 
                 for col_index in xrange(sheet.ncols)}
            dict_list.append(d)
        product_obj = self.env['product.product']

        for prod_list in dict_list:
            print(prod_list['code'])
            search_product = product_obj.search([('barcode','=',prod_list['code'])],limit=1)
            msg = 'Product not exist %s', prod_list['code']
            if not search_product:
                raise UserError(_("Product does not exist %s") % (prod_list['code']))
            prod_list.update({'product_id':search_product.id})
            prod_list.update({'name':search_product.name})
            prod_list.update({'product_uom':search_product.uom_po_id.id})
            prod_list.update({'product_qty': prod_list['qty']})
            prod_list.update({'price_unit': prod_list['price']})
            prod_list.update({'date_planned': datetime.today().strftime(DEFAULT_SERVER_DATETIME_FORMAT)})


        create_adjustment_line = self.env['purchase.order'].import_purchase_line(dict_list,context['current_order_id'])

        return