# -*- coding: utf-8 -*-
import time
from odoo import models, fields, api


class crm_lead(models.Model):
    _inherit = 'crm.lead'

    # product_id = fields.Many2one(
    #     string='Related Part Number',
    #     comodel_name='product.product',
    # )
    expected_income_id = fields.One2many(
        string='expected income',
        comodel_name='crm.expected.income',
        inverse_name='crm_lead_id',
    )
class crm_product(models.Model):
    _inherit = "product.product"

    @api.multi
    def name_get(self):
        # TDE: this could be cleaned a bit I think

        def _name_get(d):
            name = d.get('name', '')
            code = self._context.get('display_default_code', True) and d.get('default_code', False) or False
            return (d['id'], name)

        partner_id = self._context.get('partner_id')
        if partner_id:
            partner_ids = [partner_id, self.env['res.partner'].browse(partner_id).commercial_partner_id.id]
        else:
            partner_ids = []

        # all user don't have access to seller and partner
        # check access and use superuser
        self.check_access_rights("read")
        self.check_access_rule("read")

        result = []

        # Prefetch the fields used by the `name_get`, so `browse` doesn't fetch other fields
        # Use `load=False` to not call `name_get` for the `product_tmpl_id`
        self.sudo().read(['name', 'default_code', 'product_tmpl_id', 'attribute_value_ids', 'attribute_line_ids'], load=False)

        product_template_ids = self.sudo().mapped('product_tmpl_id').ids

        if partner_ids:
            supplier_info = self.env['product.supplierinfo'].sudo().search([
                ('product_tmpl_id', 'in', product_template_ids),
                ('name', 'in', partner_ids),
            ])
            # Prefetch the fields used by the `name_get`, so `browse` doesn't fetch other fields
            # Use `load=False` to not call `name_get` for the `product_tmpl_id` and `product_id`
            supplier_info.sudo().read(['product_tmpl_id', 'product_id', 'product_name', 'product_code'], load=False)
            supplier_info_by_template = {}
            for r in supplier_info:
                supplier_info_by_template.setdefault(r.product_tmpl_id, []).append(r)
        for product in self.sudo():
            # display only the attributes with multiple possible values on the template
            variable_attributes = product.attribute_line_ids.filtered(lambda l: len(l.value_ids) > 1).mapped('attribute_id')
            variant = product.attribute_value_ids._variant_name(variable_attributes)

            name = variant and "%s (%s)" % (product.name, variant) or product.name
            sellers = []
            if partner_ids:
                product_supplier_info = supplier_info_by_template.get(product.product_tmpl_id, [])
                sellers = [x for x in product_supplier_info if x.product_id and x.product_id == product]
                if not sellers:
                    sellers = [x for x in product_supplier_info if not x.product_id]
            if sellers:
                for s in sellers:
                    seller_variant = s.product_name and (
                        variant and "%s (%s)" % (s.product_name, variant) or s.product_name
                        ) or False
                    mydict = {
                              'id': product.id,
                              'name': seller_variant or name,
                              'default_code': s.product_code or product.default_code,
                              }
                    temp = _name_get(mydict)
                    if temp not in result:
                        result.append(temp)
            else:
                mydict = {
                          'id': product.id,
                          'name': name,
                          'default_code': product.default_code,
                          }
                result.append(_name_get(mydict))
        return result

class crm_expected_income(models.Model):
    _name = 'crm.expected.income'

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
    product_id = fields.Many2one(
        string='Product Name',
        comodel_name='product.product',
    )
    product_code =  fields.Char(
        string='Product code',
        related="product_id.default_code",
    )

    @api.multi
    @api.depends('quantity','amount')
    def _compute_total_price(self):
        for item in self:
            item.Total_price = item.quantity * item.amount
