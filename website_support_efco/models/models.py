# -*- coding: utf-8 -*-

from odoo import models, fields, api

class website_support_efco(models.Model):
    _name = 'efco_model'

    model_description = fields.Char('Model_Description')
    ticket_id = fields.Many2one(
        string=u'ticket_model',
        comodel_name='website_support.website.support.ticket',
    )
       
class Association_Website_Suppot_Ticket(models.Model):
    
    _inherit = 'website_support.website_support_ticket'

    ticket_model = fields.One2many(
        string=u'ticket_model',
        comodel_name='website_support_efco.efco_model',
        inverse_name='model_description',
    )
    
    
    
    


