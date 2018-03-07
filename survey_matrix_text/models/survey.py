# -*- coding: utf-8 -*-

import logging

from openerp import models, fields, api
from openerp.tools.translate import _
from openerp import SUPERUSER_ID
from openerp.addons.survey.controllers.main import dict_soft_update
from openerp.addons.survey.survey import dict_keys_startswith


_logger = logging.getLogger(__name__)

class SurveyQuestion(models.Model):
    """extend survey.question model"""

    _inherit = 'survey.question'

    type = fields.Selection(selection_add=[('matrix_text', 'Matrix Text')])
    matrix_subtype = fields.Selection(selection_add=[('matrix_text', 'Multiple text per row')])
    display_filter = fields.Selection([
        ('none', 'None'),
        ('column', 'Column'),
        ('row', 'Row'),
        ('all', 'All')
    ], default='none',)

    def validate_matrix_text(self, cr, uid, question, post, answer_tag, context=None):
        return {}

class SurveyUserInputLine(models.Model):
    """extend suervey.user_input_line model"""

    _inherit = 'survey.user_input_line'

    answer_type = fields.Selection(selection_add=[('matrix_text', "Matrix Text")])

    def save_line_matrix_text(self, cr, uid, user_input_id, question, post, answer_tag, context=None):
        vals = {
            'user_input_id': user_input_id,
            'question_id': question.id,
            'page_id': question.page_id.id,
            'survey_id': question.survey_id.id,
            'skipped': False
        }
        old_uil = self.search(cr, uid, [('user_input_id', '=', user_input_id),
                                        ('survey_id', '=', question.survey_id.id),
                                        ('question_id', '=', question.id)],
                              context=context)
        if old_uil:
            self.unlink(cr, SUPERUSER_ID, old_uil, context=context)

        no_answers = True
        ca = dict_keys_startswith(post, answer_tag+"_")
        
        for col in question.labels_ids:
            for row in question.labels_ids_2:
                a_tag = "%s_%s_%s" % (answer_tag, row.id, col.id)
                if a_tag in ca and post[a_tag].strip() != '':
                    no_answers = False
                    vals.update({'answer_type': 'matrix_text', 'value_suggested': col.id, 'value_suggested_row': row.id, 'value_free_text': post[a_tag]})
                    self.create(cr, uid, vals, context=context)
                    

        if no_answers:
            vals.update({'answer_type': 'matrix_text', 'skipped': True})
            self.create(cr, uid, vals, context=context)

        return True


class SurveyUserInput(models.Model):
    """extend survey user input"""

    _inherit = 'survey.user_input'

    @api.multi
    def get_the_answer(self, token, page):

        ret = {}
        # Fetch previous answers
        try:
            if page:
                ids = self.search([('token', '=', token), ('page_id', '=', page.id)])
            else:
                ids = self.search([('token', '=', token)])
        except ValueError:
            return ret
        for answer in ids.user_input_line_ids:
            if not answer.skipped:
                answer_tag = '%s_%s_%s' % (
                    answer.survey_id.id, answer.page_id.id, answer.question_id.id)
                answer_value = None
                if answer.answer_type == 'free_text':
                    answer_value = answer.value_free_text
                elif answer.answer_type == 'text' and answer.question_id.type == 'textbox':
                    answer_value = answer.value_text
                elif answer.answer_type == 'text' and answer.question_id.type != 'textbox':
                    # here come comment answers for matrices, simple choice and multiple choice
                    answer_tag = "%s_%s" % (answer_tag, 'comment')
                    answer_value = answer.value_text
                elif answer.answer_type == 'number':
                    answer_value = answer.value_number.__str__()
                elif answer.answer_type == 'date':
                    answer_value = answer.value_date
                elif answer.answer_type == 'suggestion' and not answer.value_suggested_row:
                    answer_value = answer.value_suggested.id
                elif answer.answer_type == 'suggestion' and answer.value_suggested_row:
                    answer_tag = "%s_%s" % (
                        answer_tag, answer.value_suggested_row.id)
                    answer_value = answer.value_suggested.id
                elif answer.answer_type == 'matrix_text' and answer.value_suggested_row:
                    answer_tag = "%s_%s_%s" % (
                        answer_tag, answer.value_suggested_row.id, answer.value_suggested.id)
                    answer_value = answer.value_free_text
                if answer_value:
                    dict_soft_update(ret, answer_tag, answer_value)
                else:
                    _logger.warning(
                        "[survey] No answer has been found for question %s marked as non skipped" % answer_tag)
        return ret
