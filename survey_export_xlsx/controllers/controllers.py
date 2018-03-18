# -*- coding: utf-8 -*-

import logging
import urllib
from openerp import http
from openerp.http import request

_logger = logging.getLogger(__name__)
try:
    import xlsxwriter
except ImportError:
    _logger.debug('Can not import xlsxwriter`.')
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO


class ExportXlsx(http.Controller):
    """Exoirt Excel"""

    @http.route('/web/<model("survey.survey"):survey>/export_xlsx', auth="public")
    def index(self, survey, **post):
        """export survey answer excel
        Arguments:
            survey {recordset} -- current survey to export
        Returns:
            [application/vnd.ms-excel] -- export the .xls file
        """
        # create new workbook and worksheet
        output = StringIO.StringIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet(survey.title)
        # initialization
        j = 0
        conut = 0
        temp = ''
        worksheet.write(0, 0, 'partner')
        # Question
        for page in survey.page_ids:
            for question in page.question_ids:
                if question.type in ['matrix', 'matrix_text']:
                    for labels in question.labels_ids:
                        j = j + 1
                        worksheet.write(0, j, question.question +
                                        " [" + labels.value + "]")
                        self.pull_value_to_cell(
                            worksheet, j, survey.id, question, temp, conut, labels)
                else:
                    j = j + 1
                    worksheet.write(0, j, question.question)
                    self.pull_value_to_cell(
                        worksheet, j, survey.id, question, temp, conut, None)
        # response
        workbook.close()
        output.seek(0)
        filename_parm = 'Survey'
        if isinstance(survey.title,unicode):
            filename_parm = urllib.quote(survey.title.encode('utf-8'))
        else:
            filename_parm = urllib.quote(survey.title)
        response_headers = [('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                            ('Content-Disposition', "attachment; filename*=UTF-8''%s.xlsx;" % filename_parm)]
        response = request.make_response(output.read(), headers=response_headers)
        return response

    def pull_value_to_cell(self, worksheet, j, survey_id, question, temp, conut, labels):
        """pull value to cell
        Arguments:
            worksheet {worksheet} -- worksheet
            j {int} -- col number
            survey {record} -- currently servey.survey.id
            question {record} -- currently servey.question information
            temp {string} -- Temporarily save this message for the next time
            conut {int} -- How many multiple choices
        Returns:
            [worksheet] -- worksheet
        """
        i = 0
        k = 0
        for user_line in http.request.env['survey.user_input'].search([('survey_id', '=', survey_id)], order="id"):
            if user_line.state == 'done':
                # Partner
                k = k + 1
                if user_line.partner_id and j == 1:
                    worksheet.write(
                        k, j-1, user_line.partner_id[0].name)
                # Answer
                i = i + 1
                if question.type in ['matrix', 'matrix_text']:
                    user_input_line = question.user_input_line_ids.search([('survey_id', '=', survey_id),
                                                                           ('question_id',
                                                                            '=', question.id),
                                                                           ('user_input_id',
                                                                            '=', user_line.id),
                                                                           ('value_suggested', '=', labels.id)], order="user_input_id")
                    conut = len(user_input_line)
                    for user_input in user_input_line:
                        if not user_input.skipped:
                            martix_answer = (
                                user_input.value_suggested_row[0].value if
                                question.type == 'matrix' else
                                user_input.value_free_text) + temp
                            conut = conut - 1
                            if conut == 0:
                                worksheet.write(i, j, martix_answer)
                                temp = ''
                            else:
                                temp = ',' + \
                                    (user_input.value_suggested_row[0].value if
                                     question.type == 'matrix' else
                                     user_input.value_free_text)
                else:
                    user_input_line = question.user_input_line_ids.search([('survey_id', '=', survey_id), (
                        'question_id', '=', question.id), ('user_input_id', '=', user_line.id)], order="user_input_id")
                    conut = len(user_input_line)
                    for user_input in user_input_line:
                        if not user_input.skipped:
                            if question.type == 'free_text':
                                worksheet.write(
                                    i, j, user_input.value_free_text)
                            if question.type == 'textbox':
                                worksheet.write(
                                    i, j, user_input.value_text)
                            if question.type == 'datetime':
                                worksheet.write(
                                    i, j, user_input.value_date)
                            if question.type == 'numerical_box':
                                worksheet.write(
                                    i, j, user_input.value_number)
                            if question.type in ['simple_choice', 'multiple_choice']:
                                choice_answer = user_input.value_suggested[0].value + temp
                                conut = conut - 1
                                if conut == 0:
                                    worksheet.write(i, j, choice_answer)
                                    temp = ''
                                else:
                                    temp = ',' + \
                                        user_input.value_suggested[0].value
                        else:
                            worksheet.write(i, j, '')
        return worksheet
