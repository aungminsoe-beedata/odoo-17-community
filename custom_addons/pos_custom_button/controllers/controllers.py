# -*- coding: utf-8 -*-
# from odoo import http


# class PosCustomButton(http.Controller):
#     @http.route('/pos_custom_button/pos_custom_button', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_custom_button/pos_custom_button/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_custom_button.listing', {
#             'root': '/pos_custom_button/pos_custom_button',
#             'objects': http.request.env['pos_custom_button.pos_custom_button'].search([]),
#         })

#     @http.route('/pos_custom_button/pos_custom_button/objects/<model("pos_custom_button.pos_custom_button"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_custom_button.object', {
#             'object': obj
#         })

