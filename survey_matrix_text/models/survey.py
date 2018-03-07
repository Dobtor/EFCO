# -*- encoding: utf-8 -*-

from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp import SUPERUSER_ID
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT as DF
from openerp.addons.website.models.website import slug
from urlparse import urljoin
from itertools import product
from collections import Counter
from collections import OrderedDict
from openerp.exceptions import UserError

import datetime
import logging
import re
import uuid


class survey_question(osv.Model):
    
    _inherit = 'survey.question'

    _columns = {
        #'type': fields.Selection(selection_add=[('matrix_text', 'Matrix Text')]),
        #'matrix_subtype': fields.Selection(selection_add=[('matrix_text', 'Multiple text per row')])
        'type': fields.selection([('free_text', 'Multiple Lines Text Box'),
                ('textbox', 'Single Line Text Box'),
                ('numerical_box', 'Numerical Value'),
                ('datetime', 'Date and Time'),
                ('simple_choice', 'Multiple choice: only one answer'),
                ('multiple_choice', 'Multiple choice: multiple answers allowed'),
                ('matrix', 'Matrix'), ('matrix_text', 'Matrix Text')], 
                'Type of Question', size=15, required=1),
        'matrix_subtype': fields.selection(
            [
                ('simple', 'One choice per row'),
                ('multiple', 'Multiple choices per row'),
                ('matrix_text', 'Multiple text per row')
            ], 'Matrix Type'),
    }
    
