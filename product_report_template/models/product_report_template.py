# -*- coding: utf-8 -*-

from openerp import models, fields, api


class ProductReportTemplate(models.Model):
    _name = 'product.report.template'

    name = fields.Char(
        string='Tempalte Name',
    )

    external_header_id = fields.Many2one(
        string='Current External Header Template *',
        comodel_name='ir.ui.view',
        default=lambda self: self.env.ref('product_report_template.custom_product_external_layout_header').id
    )

    external_footer_id = fields.Many2one(
        string='External Header Template *',
        comodel_name='ir.ui.view',
        default=lambda self: self.env.ref(
            'product_report_template.custom_product_external_layout_footer').id
    )
