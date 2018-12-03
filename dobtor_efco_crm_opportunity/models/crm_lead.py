# -*- coding: utf-8 -*-
import time
from odoo import models, fields, api


class crm_lead(models.Model):
    _inherit = 'crm.lead'

    product_id = fields.Many2one(
        string='Related Part Number',
        comodel_name='product.product',
    )
    expected_income_id = fields.One2many(
        string='expected income',
        comodel_name='crm.expected.income',
        inverse_name='crm_lead_id',
    )


class crm_expected_income(models.Model):
    _name = 'crm.expected.income'
    _order = 'crm_lead_id, sequence'

    @api.model
    def get_current_year(self):
        return time.strftime("%Y")

    @api.model
    def get_years(self):
        year_list = []
        year = self.get_current_year()
        for i in range(int(year) - 20, int(year) + 20):
            year_list.append((str(i), str(i)))
        return year_list

    year = fields.Selection(get_years, string='Year',
                            default=lambda self: self.get_current_year())
    quarterly = fields.Selection(
        string='Quarterly',
        selection=[('q1', 'Q1'), ('q2', 'Q2'), ('q3', 'Q3'), ('q4', 'Q4')]
    )

    quantity = fields.Float(
        string='Quantity',
    )
    amount = fields.Float(
        string='Unit Price',
    )
    Total_price = fields.Float(
        string='Total price',
    )
    crm_lead_id = fields.Many2one(
        string='Associate crm opportunity',
        comodel_name='crm.lead',
    )
    sequence = fields.Integer(
        string='sequence',
    )
    
