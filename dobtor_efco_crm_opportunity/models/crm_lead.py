# -*- coding: utf-8 -*-
import time
from odoo import models, fields, api


class crm_lead(models.Model):
    _inherit = 'crm.lead'

    @api.depends('planned_revenue', 'project_lifetime')
    def compute_project_value(self):
        for item in self:
            item.compute_value = item.planned_revenue * item.project_lifetime

    project_lifetime = fields.Float(
        string=u'Project lifetime', default=0.0
    )
    compute_value = fields.Float(
        string=u'Compute Value', compute="compute_project_value"
    )
    expected_income_id = fields.One2many(
        string='expected income',
        comodel_name='crm.expected.income',
        inverse_name='crm_lead_id',
    )
    opp_id = fields.Char(string=u'Opp ID',readonly=True)

    end_customer = fields.Many2one('res.partner', string=u"End Customer",)

    @api.model
    def create(self,values):
        values['opp_id'] = self.env['ir.sequence'].next_by_code('crm.lead.opp')
        res = super(crm_lead, self).create(values)
        return res

class crm_product(models.Model):
    _inherit = "product.product"

    @api.multi
    def name_get(self):
        res = []
        if self.env.context.get('only_product_name', False):
            for product in self.sudo():
                variable_attributes = product.attribute_line_ids.filtered(
                    lambda l: len(l.value_ids) > 1).mapped('attribute_id')
                variant = product.attribute_value_ids._variant_name(
                    variable_attributes)
                name = variant and "%s (%s)" % (
                    product.name, variant) or product.name
                res.append((product.id, (name)))
            return res
        return super(crm_product, self).name_get()


class crm_expected_income(models.Model):
    _name = 'crm.expected.income'
    _order = 'crm_lead_id, sequence'

    @api.model
    def get_current_year(self):
        return time.strftime("%Y")

    @api.multi
    @api.depends('q1_quantity', 'q2_quantity', 'q3_quantity', 'q4_quantity', 'amount')
    def _compute_total_price(self):
        for item in self:
            item.q1_total_price = item.q1_quantity * item.amount
            item.q2_total_price = item.q2_quantity * item.amount
            item.q3_total_price = item.q3_quantity * item.amount
            item.q4_total_price = item.q4_quantity * item.amount
            item.annual_quantity = item.q1_quantity + \
                item.q2_quantity + item.q3_quantity + item.q4_quantity
            item.annual_amount = item.q1_total_price + item.q2_total_price + \
                item.q3_total_price + item.q4_total_price

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
    q1_quantity = fields.Float(
        string='Q1 FcstQTY',
    )
    q2_quantity = fields.Float(
        string='Q2 FcstQTY',
    )
    q3_quantity = fields.Float(
        string='Q3 FcstQTY',
    )
    q4_quantity = fields.Float(
        string='Q4 FcstQTY',
    )
    q1_total_price = fields.Float(
        string='Q1 Total',
        compute='_compute_total_price'
    )
    q2_total_price = fields.Float(
        string='Q2 Total',
        compute='_compute_total_price'
    )
    q3_total_price = fields.Float(
        string='Q3 Total',
        compute='_compute_total_price'
    )
    q4_total_price = fields.Float(
        string='Q4 Total',
        compute='_compute_total_price'
    )
    annual_quantity = fields.Float(
        string='Annual Fcst Qty', compute='_compute_total_price'
    )
    annual_amount = fields.Float(
        string='Annual Fcst Total', compute='_compute_total_price')
    amount = fields.Float(
        string='Unit Price',
    )
    Total_price = fields.Float(
        string='Total price',
        compute='_compute_total_price'
    )
    crm_lead_id = fields.Many2one(
        string='Associate crm opportunity',
        comodel_name='crm.lead', required=True, ondelete='cascade',
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
        string='Product',
        comodel_name='product.product',
    )
    article_number = fields.Many2one(
        string='Article Number',
        comodel_name="article.number"
    )
    partner_id = fields.Many2one(
        string=u'Revenue Customer', related="crm_lead_id.partner_id")
    opp_id = fields.Char(related="crm_lead_id.opp_id")
    end_customer = fields.Many2one(related="crm_lead_id.end_customer")
    new_part_code = fields.Many2one(
        string="Part Number", comodel_name="part.number")
    stage_id = fields.Many2one(
        related="crm_lead_id.stage_id"
    )
    region = fields.Many2one(
        'res.country', string='Region', related="partner_id.country_id")
    business_line = fields.Many2one(
        string=u'BL', related="crm_lead_id.team_id")

    @api.onchange('article_number')
    def do_change_product(self):
        for record in self:
            if record.article_number:
                product = self.env['product.product'].search(
                    [('new_part_code', '=', record.article_number.id)], limit=1)
                if not record.product_id and product:
                    record.product_id = product
                elif record.product_id and record.product_id.new_part_code != record.article_number and product:
                    record.product_id = product
                elif record.product_id and record.product_id.new_part_code != record.article_number and not product:
                    record.product_id = False

                # if not record.new_part_code and product and product.old_part_code:
                #     record.new_part_code = product.old_part_code
                # elif record.new_part_code and product and product.old_part_code and record.new_part_code != product.old_part_code:
                #     record.new_part_code = product.old_part_code

    @api.onchange('product_id')
    def do_change_article_number(self):
        for record in self:
            if record.product_id and record.product_id.new_part_code:
                if not record.article_number:
                    record.article_number = record.product_id.new_part_code
                elif record.article_number and record.article_number != record.product_id.new_part_code:
                    record.article_number = record.product_id.new_part_code
            else:
                record.article_number = False

            if record.product_id and record.product_id.old_part_code:
                if not record.new_part_code:
                    record.new_part_code = record.product_id.old_part_code
                elif record.product_id.old_part_code and record.new_part_code != record.product_id.old_part_code:
                    record.new_part_code = record.product_id.old_part_code
            else:
                record.new_part_code = False

    @api.onchange('new_part_code')
    def do_product_by_new_part_code(self):
        for record in self:
            if record.new_part_code:
                product = self.env['product.product'].search(
                    [('old_part_code', '=', record.new_part_code.id)], limit=1)
                if not record.product_id and product:
                    record.product_id = product
                elif record.product_id and product and record.product_id.old_part_code != record.new_part_code:
                    record.product_id = product
                elif record.product_id and not product and record.product_id.old_part_code != record.new_part_code:
                    record.product_id = False

                # if not record.article_number and product and product.new_part_code:
                #     record.article_number = product.new_part_code
                # elif record.article_number and record.article_number != product.new_part_code and product and product.new_part_code:
                #     record.article_number = product.new_part_code
