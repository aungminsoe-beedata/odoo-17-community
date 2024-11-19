# -*- coding: utf-8 -*-
# from odoo import http


# class ApprovalCustomization(http.Controller):
#     @http.route('/approval_customization/approval_customization', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/approval_customization/approval_customization/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('approval_customization.listing', {
#             'root': '/approval_customization/approval_customization',
#             'objects': http.request.env['approval_customization.approval_customization'].search([]),
#         })

#     @http.route('/approval_customization/approval_customization/objects/<model("approval_customization.approval_customization"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('approval_customization.object', {
#             'object': obj
#         })

