# -*- coding: utf-8 -*-
import time
from odoo import models, fields, api


class crm_lead(models.Model):
    _inherit = 'crm.lead'

    expected_income_id = fields.One2many(
        string='expected income',
        comodel_name='crm.expected.income',
        inverse_name='crm_lead_id',
    )
class crm_product(models.Model):
    _inherit = "product.product"

    @api.multi
    def name_get(self):
        res = []
        if self.env.context.get('only_product_name', False):
            for product in self.sudo():
                variable_attributes = product.attribute_line_ids.filtered(lambda l: len(l.value_ids) > 1).mapped('attribute_id')
                variant = product.attribute_value_ids._variant_name(variable_attributes)
                name = variant and "%s (%s)" % (product.name, variant) or product.name
                res.append((product.id, (name)))
            return res
        return super(crm_product, self).name_get()


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
        compute='_compute_total_price'
    )
    crm_lead_id = fields.Many2one(
        string='Associate crm opportunity',
        comodel_name='crm.lead',
    )
    sequence = fields.Integer(
        string='sequence',
    )
    saleperson = fields.Many2one(
        string='Sale person',
        comodel_name='res.users',
        related='crm_lead_id.user_id',
    )
    product_id = fields.Many2one(
        string='Product Name',
        comodel_name='product.product',
    )
    article_number = fields.Char(
        string='Article Number',
        related="product_id.default_code",
    )

    @api.multi
    @api.depends('quantity','amount')
    def _compute_total_price(self):
        for item in self:
            item.Total_price = item.quantity * item.amount
