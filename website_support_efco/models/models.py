# -*- coding: utf-8 -*-

from odoo import models, fields, api

class website_support_efco(models.Model):
    _name = 'efco_model'

    model_description = fields.Char('Model Description')
    ticket_id = fields.Many2one(
        string=u'ticket_model',
        comodel_name='website_support.website.support.ticket',
    )
       
class Association_Website_Suppot_Ticket(models.Model):
    
    _inherit = 'website.support.ticket'

    ticket_model = fields.One2many(
        string=u'ticket_model',
        comodel_name='efco_model',
        inverse_name='ticket_id',
    )
    
    article_description = fields.Char('Article Descirpt')
    part_number = fields.Char('Part Number')
    hardware_revision = fields.Char('Hardware Revision')
    bios_revision = fields.Char('Bios Revision')
    serial_number = fields.Char('Serial Number')
    operiating_system = fields.Char('Operiating System')
    flat_panel = fields.Char('Flat Panel')
    
    


