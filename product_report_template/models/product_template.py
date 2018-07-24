# -*- coding: utf-8 -*-

from openerp import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    report_template_id = fields.Many2one(
        string='Report Template',
        comodel_name='product.report.template',
    )

    version = fields.Boolean(
        string='Open the version',
        default=False,
    )

    version_label = fields.Char(string='Version Label')
    is_visible_pdf = fields.Boolean(default=True)

    @api.one
    def toggle_pdf(self):
        self.is_visible_pdf = not self.is_visible_pdf
