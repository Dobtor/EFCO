# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ctw(models.Model):
    _inherit = 'mrp.repair'

    CTM_ref = fields.Char("CTM ref")
    CTW_PNLot = fields.Char("CTW_PNLot")
    CTW_AssemblyPO = fields.Char("CTW_AssemblyPO")
    CTW_ChangeCPU = fields.Boolean("CTW_ChangeCPU")
    CTW_Warranty  = fields.Boolean("CTW_Warranty")
    CTW_Heat_sink = fields.Char("CTW_Heat_sink")