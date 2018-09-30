# -*- coding: utf-8 -*-
{
    'name': "dobtor_todolist_survey",
    'summary': """
        1. Todolist with survey functionality
        2. Management todolist survey input
        """,
    'description': """
        Todolist with survey functionality
    """,
    'author': "Dobtor SI",
    "license": "LGPL-3",
    'website': "http://www.dobtor.com",
    'category': 'survey',
    'version': '0.1',
    'depends': ['survey','dobtor_todolist_core','dobtor_todolist_project_task'],
    'data': [
        'views/todolist_views.xml',
        'views/history_survey.xml',
    ]
}
