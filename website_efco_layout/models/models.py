# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class website__efco_layout(models.Model):
#     _name = 'website__efco_layout.website__efco_layout'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100