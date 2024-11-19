# -*- coding: utf-8 -*-
# from odoo import http


# class WmsCfsCustomization(http.Controller):
#     @http.route('/wms_cfs_customization/wms_cfs_customization', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wms_cfs_customization/wms_cfs_customization/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('wms_cfs_customization.listing', {
#             'root': '/wms_cfs_customization/wms_cfs_customization',
#             'objects': http.request.env['wms_cfs_customization.wms_cfs_customization'].search([]),
#         })

#     @http.route('/wms_cfs_customization/wms_cfs_customization/objects/<model("wms_cfs_customization.wms_cfs_customization"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wms_cfs_customization.object', {
#             'object': obj
#         })

