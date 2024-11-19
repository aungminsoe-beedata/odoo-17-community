# -*- coding: utf-8 -*-
# from odoo import http


# class OwlDashboard(http.Controller):
#     @http.route('/owl_dashboard/owl_dashboard', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/owl_dashboard/owl_dashboard/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('owl_dashboard.listing', {
#             'root': '/owl_dashboard/owl_dashboard',
#             'objects': http.request.env['owl_dashboard.owl_dashboard'].search([]),
#         })

#     @http.route('/owl_dashboard/owl_dashboard/objects/<model("owl_dashboard.owl_dashboard"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('owl_dashboard.object', {
#             'object': obj
#         })

