# -*- coding: utf-8 -*-
# from odoo import http


# class AmsApproval(http.Controller):
#     @http.route('/ams_approval/ams_approval', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ams_approval/ams_approval/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ams_approval.listing', {
#             'root': '/ams_approval/ams_approval',
#             'objects': http.request.env['ams_approval.ams_approval'].search([]),
#         })

#     @http.route('/ams_approval/ams_approval/objects/<model("ams_approval.ams_approval"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ams_approval.object', {
#             'object': obj
#         })

