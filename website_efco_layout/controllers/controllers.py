# -*- coding: utf-8 -*-
from openerp import http

# class WebsiteEfcoLayout(http.Controller):
#     @http.route('/website__efco_layout/website__efco_layout/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website__efco_layout/website__efco_layout/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website__efco_layout.listing', {
#             'root': '/website__efco_layout/website__efco_layout',
#             'objects': http.request.env['website__efco_layout.website__efco_layout'].search([]),
#         })

#     @http.route('/website__efco_layout/website__efco_layout/objects/<model("website__efco_layout.website__efco_layout"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website__efco_layout.object', {
#             'object': obj
#         })