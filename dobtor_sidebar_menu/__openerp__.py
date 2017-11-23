# -*- coding: utf-8 -*-
{
    'name': "dobtor_sidebar_menu",
    'summary': """
        建立 sidebar menu
        """,
    'description': """
        建立 sidebar menu
    """,
    'author': "Dobtor SI",
    'website': "https://www.dobtor.com",
    'category': 'dobtor',
    'version': '0.1',
    'depends': ['website'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'demo/demo.xml',
    ],
    'demo': [
    ],
}
