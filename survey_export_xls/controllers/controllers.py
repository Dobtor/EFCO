# -*- coding: utf-8 -*-

from datetime import datetime
import xlwt
from openerp import http
from openerp.http import request
from openerp.addons.survey.controllers.main import WebsiteSurvey


class WebsiteSurvey(WebsiteSurvey):

    @http.route('/web/<model("survey.survey"):survey>/export_xls2', auth="public")
    def index2(self, survey, **post):

        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet(survey.title, cell_overwrite_ok=True)
        j = 0
        worksheet.write(0, 0, 'partner')
        conut = 0
        temp = ''
        for page in survey.page_ids:
            for question in page.question_ids:
                # Question
                j = j + 1
                # print('Question', 0, j, question.question)
                worksheet.write(0, j, question.question)
                i = 0
                k = 0
                for user_line in http.request.env['survey.user_input'].search([('survey_id', '=', survey.id)], order="id"):
                    if user_line.state == 'done':
                        k = k + 1
                        if user_line.partner_id and j == 1:
                            # print('partner_id', k, j-1,
                            #       user_line.partner_id[0].name)
                            worksheet.write(k, j-1, user_line.partner_id[0].name)
                        i = i + 1
                        user_input_line = question.user_input_line_ids.search([('survey_id', '=', survey.id), ('question_id', '=', question.id), ('user_input_id', '=', user_line.id)], order="user_input_id")
                        conut = len(user_input_line)
                        for user_input in user_input_line:
                            if question.type in ['textbox', 'free_text', 'datetime']:
                                if not user_input.skipped:
                                    if question.type == 'free_text':
                                        # print('free_text', i, j,
                                        #       user_input.value_free_text)
                                        worksheet.write(
                                            i, j, user_input.value_free_text)
                                    if question.type == 'textbox':
                                        # print('textbox', i, j,
                                        #       user_input.value_text)
                                        worksheet.write(
                                            i, j, user_input.value_text)
                                    if question.type == 'datetime':
                                        # print('datetime', i, j,
                                        #       user_input.value_date)
                                        worksheet.write(
                                            i, j, user_input.value_date)
                                else:
                                    worksheet.write(i, j, '')
                            if question.type == 'numerical_box':
                                if not user_input.skipped:
                                    # print('numerical_box', i, j,
                                    #       user_input.value_number)
                                    worksheet.write(i, j, user_input.value_number)
                                else:
                                    worksheet.write(i, j, '')
                            if question.type in ['simple_choice', 'multiple_choice']:
                                if not user_input.skipped:
                                    choice_answer = user_input.value_suggested[0].value + temp
                                    # print(choice_answer)
                                    conut = conut - 1
                                    if conut == 0:
                                        worksheet.write(i, j, choice_answer)
                                        temp = ''
                                    else:
                                        temp = ',' + user_input.value_suggested[0].value
                                else:
                                    worksheet.write(i, j, '')

                            

                # for user_input in question.user_input_line_ids.search([('survey_id','=',survey.id),('question_id','=',question.id)], order="user_input_id"):
                #     if user_input.user_input_id[0].state == 'done':
                #         if question.type in ['textbox', 'free_text', 'datetime']:
                #             i = i + 1
                #             print(user_input)
                #             if not user_input.skipped:
                #                 if question.type == 'free_text':
                #                     print('free_text', i, j,
                #                         user_input.value_free_text)
                #                     worksheet.write(
                #                         i, j, user_input.value_free_text)
                #                 if question.type == 'textbox':
                #                     print('textbox', i, j, user_input.value_text)
                #                     worksheet.write(i, j, user_input.value_text)
                #                 if question.type == 'datetime':
                #                     print('datetime', i, j, user_input.value_date)
                #                     worksheet.write(i, j, user_input.value_date)
                #             else:
                #                 worksheet.write(i, j, '')
                #         if question.type == 'numerical_box':
                #             i = i + 1
                #             if not user_input.skipped:
                #                 print('numerical_box', i, j,
                #                     user_input.value_number)
                #                 worksheet.write(i, j, user_input.value_number)
                #             else:
                #                 worksheet.write(i, j, '')

        response = request.make_response(None,
                                         headers=[('Content-Type', 'application/vnd.ms-excel'),
                                                  ('Content-Disposition', 'attachment; filename=table.xls;')])
        workbook.save(response.stream)

        return response

    @http.route('/web/<model("survey.survey"):survey>/export_xls', auth="public")
    def index(self, survey, **post):

        style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
                             num_format_str='#,##0.00')
        style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

        survey_dict = self.prepare_result_dict(survey, [])

        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet(survey.title)

        j = -1
        for page_ids in survey_dict['page_ids']:
            for question_ids in page_ids['question_ids']:
                input_summary = question_ids['input_summary']
                question = question_ids['question']
                prepare_result = question_ids['prepare_result']
                # Question
                j = j + 1
                print('Question', 0, j, question.question)
                worksheet.write(0, j, question.question)
                token = ''
                i = 0
                if input_summary['answered'] != 0:
                    if question.type in ['textbox', 'free_text', 'datetime']:
                        for user_input in prepare_result:
                            i = i + 1
                            if question.type == 'free_text':
                                print('free_text', i, j,
                                      user_input.value_free_text)
                                worksheet.write(
                                    i, j, user_input.value_free_text)
                            if question.type == 'textbox':
                                print('textbox', i, j, user_input.value_text)
                                worksheet.write(i, j, user_input.value_text)
                            if question.type == 'datetime':
                                print('datetime', i, j, user_input.value_date)
                                worksheet.write(i, j, user_input.value_date)
                    if question.type in ['simple_choice', 'multiple_choice']:
                        for user_input in prepare_result['answers']:
                            i = i + 1
                            worksheet.write(i, j, user_input['text'])
                    if question.type == 'numerical_box':
                        for user_input in prepare_result['input_lines']:
                            i = i + 1
                            print('numerical_box', i, j,
                                  user_input.value_number)
                            worksheet.write(i, j, user_input.value_number)

                # if question.type != 'matrix' and question.type != 'multiple_choice':
                    # for text_result in question_ids.prepare_result

        # for survey_user_input in http.request.env['survey.survey_user_input'].search([('survey_id', '=', survey.id), ('state', '=', 'done')]):
        #     for answer in survey_user_input.user_input_line_ids:
        #         answer_tag = '%s_%s_%s' % (
        #             answer.survey_id.id, answer.page_id.id, answer.question_id.id)

        response = request.make_response(None,
                                         headers=[('Content-Type', 'application/vnd.ms-excel'),
                                                  ('Content-Disposition', 'attachment; filename=table.xls;')])
        workbook.save(response.stream)

        return response
