# -*- coding: utf-8 -*-
# from odoo import http


# class RegionCustomization(http.Controller):
#     @http.route('/region_customization/region_customization', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/region_customization/region_customization/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('region_customization.listing', {
#             'root': '/region_customization/region_customization',
#             'objects': http.request.env['region_customization.region_customization'].search([]),
#         })

#     @http.route('/region_customization/region_customization/objects/<model("region_customization.region_customization"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('region_customization.object', {
#             'object': obj
#         })
