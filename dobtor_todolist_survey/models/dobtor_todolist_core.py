# -*- coding: utf-8 -*-

from openerp import models, fields, api


class DobtorTodoListSurvey(models.Model):
    _inherit = 'dobtor.todolist.core'
    survey_id = fields.Many2one("survey.survey", "Survey")
    response_id = fields.Many2one(
        'survey.user_input', "Response", ondelete="set null", oldname="response")

    todolist_user_input_ids = fields.One2many(
        string='todolist',
        comodel_name='dobtor.todolist.user_input.ref',
        inverse_name='todolist_ids',
    )

    @api.multi
    def open_survey(self):
        if not self.response_id:
            response = self.env['survey.user_input'].create(
                {'survey_id': self.survey_id.id, 'partner_id': self.partner_id.id})
            self.response_id = response.id
            self.todolist_user_input_ids.create(
                {'todolist_ids': self.id, 'user_input_ids': response.id,
                    'user_input_name': self.partner_id.name}
            )
        else:
            response = self.response_id
        # grab the token of the response and start surveying
        return self.survey_id.with_context(survey_token=response.token).action_start_survey()

    @api.multi
    def reject_action(self):
        for record in self:
            record.response_id = None
