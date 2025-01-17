# -*- coding: utf-8 -*-

from odoo import models, api

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    # @api.multi
    def action_import_line(self):
        [action] = self.env.ref('purchase_line_import.action_purchase_line_import').read()
        action.update({'context': (u"{'current_id': context['current_order_id']}")})
        return action

    # @api.multi
    def import_purchase_line(self, dict_list, order_id):
        # for adjustment in self:
            current_id = self.browse(order_id)
            line_ids = current_id.order_line.browse([])
            for line in dict_list:
                print(line)
                line_ids += current_id.order_line.new(line)
            current_id.order_line = line_ids
            return True