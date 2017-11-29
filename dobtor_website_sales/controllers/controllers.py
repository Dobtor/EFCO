# -*- coding: utf-8 -*-
from openerp import http

# class DobtorWebsiteSales(http.Controller):
#     @http.route('/dobtor_website_sales/dobtor_website_sales/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dobtor_website_sales/dobtor_website_sales/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dobtor_website_sales.listing', {
#             'root': '/dobtor_website_sales/dobtor_website_sales',
#             'objects': http.request.env['dobtor_website_sales.dobtor_website_sales'].search([]),
#         })

#     @http.route('/dobtor_website_sales/dobtor_website_sales/objects/<model("dobtor_website_sales.dobtor_website_sales"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dobtor_website_sales.object', {
#             'object': obj
#         })