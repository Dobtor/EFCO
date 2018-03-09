# -*- coding: utf-8 -*-

from openerp.addons.website.models.website import slug
from openerp import models, api


class survey_export_xls(models.Model):
    _inherit='survey.survey'

    @api.multi
    def action_expoert_survey_xlsx(self):
        survey = self.search([('id','=',self.id)])[0]
        return {
            'type': 'ir.actions.act_url',
            'name': "Results of the Survey Excel",
            'target': 'self',
            'url': '/web/%s/export_xlsx' % (slug(survey))
        }
