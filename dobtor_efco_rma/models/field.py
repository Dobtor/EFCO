# -*- coding: utf-8 -*-
from odoo import models, fields, api


class newfield(models.Model):
    _inherit = 'mrp.repair'

    Article_Part = fields.Many2one(
        string='Article Part',
        comodel_name='product.template',
    )
    
    Rev = fields.Char(string="Rev")
    Serial_Number = fields.Char(string="Serial Number")
    Failure_Description = fields.Text(string="Failure Description")
    Note = fields.Text(string="Note")
    Attached_files = fields.Binary(string="Attached_files", store=False)
    PIC_Sales = fields.Char(string="PIC Sales")