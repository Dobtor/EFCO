# -*- coding: utf-8 -*-
from odoo import http

# class DobtorEfcoRma(http.Controller):
#     @http.route('/dobtor_efco_rma/dobtor_efco_rma/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dobtor_efco_rma/dobtor_efco_rma/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dobtor_efco_rma.listing', {
#             'root': '/dobtor_efco_rma/dobtor_efco_rma',
#             'objects': http.request.env['dobtor_efco_rma.dobtor_efco_rma'].search([]),
#         })

#     @http.route('/dobtor_efco_rma/dobtor_efco_rma/objects/<model("dobtor_efco_rma.dobtor_efco_rma"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dobtor_efco_rma.object', {
#             'object': obj
#         })