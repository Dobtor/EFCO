# -*- coding: utf-8 -*-
{
    'name': "dobtor_efco_rma",
    'summary': """
        add mrp repair freature
    """,
    'description': """
        add mrp repair freature
    """,
    'author': "Dobtor SI",
    'website': "http://www.dobtor.com",
    'category': 'mra',
    'version': '0.1',
    "license": "LGPL-3",
    'depends': ['mrp_repair'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/ctw_form.xml',
        'views/field_form.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
