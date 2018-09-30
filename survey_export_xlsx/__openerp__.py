# -*- coding: utf-8 -*-
{
    'name': "survey_export_xlsx",
    'summary': """export survey answer excel""",
    'description': """export survey answer exce""",
    'author': "Dobtor SI",
    "license": "LGPL-3",
    'website': "http://www.dobtor.com",
    'category': 'survey',
    'version': '0.1',
    'depends': ['base', 'survey', 'survey_matrix_text'],
    'external_dependencies': {'python': ['xlsxwriter']},
    'data': [
        'views/views.xml',
    ]
}
