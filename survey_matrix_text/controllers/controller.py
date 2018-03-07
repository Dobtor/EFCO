# -*- coding: utf-8 -*-

import json

from openerp.addons.web import http
from openerp.addons.survey.controllers.main import WebsiteSurvey


class WebsiteSurvey(WebsiteSurvey):
    """extend or override website survey"""


    @http.route(['/survey/prefill/<model("survey.survey"):survey>/<string:token>',
                 '/survey/prefill/<model("survey.survey"):survey>/<string:token>/<model("survey.page"):page>'],
                type='http', auth='public', website=True)
    def prefill(self, survey, token, page=None, **post):
        """AJAX prefilling of a survey
        Arguments:
            survey {[model]} -- survey.survey model
            token {[string]} -- token for this user_line
            **post {[dict]} -- model binding
        Keyword Arguments:
            page {[model]} -- current survey.page model (default: {None})
        Returns:
            [json] -- return { ' answer_tag' : [answer] }
        """

        ret = http.request.env['survey.user_input'].sudo().get_the_answer(token, page)
        return json.dumps(ret)
