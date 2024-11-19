# -*- coding: utf-8 -*-
# from odoo import http


# class CfWebsiteCustomization(http.Controller):
#     @http.route('/cf_website_customization/cf_website_customization', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cf_website_customization/cf_website_customization/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cf_website_customization.listing', {
#             'root': '/cf_website_customization/cf_website_customization',
#             'objects': http.request.env['cf_website_customization.cf_website_customization'].search([]),
#         })

#     @http.route('/cf_website_customization/cf_website_customization/objects/<model("cf_website_customization.cf_website_customization"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cf_website_customization.object', {
#             'object': obj
#         })

