# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class dobtor_todolist_lifetime(models.Model):
#     _name = 'dobtor_todolist_lifetime.dobtor_todolist_lifetime'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100