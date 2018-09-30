# -*- coding: utf-8 -*-
{
    'name': "website_EFCO_layout",
    'summary': "EFCO 公司頁首頁尾",
    'description': "EFCO 公司頁首頁尾",
    'author': "Dobtor SI",
    "license": "LGPL-3",
    'website': "https://www.dobtor.com",
    'category': 'website',
    'version': '0.1',
    'depends': ['website', 'Advance Dobtor Menu'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/assets.xml',
        'views/layout_extend.xml',
        'views/snippets.xml',
        'views/template.xml',
        'views/language.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
