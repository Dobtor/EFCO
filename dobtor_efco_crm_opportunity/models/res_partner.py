# -*- coding: utf-8 -*-
import time
from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict' ,required=True)