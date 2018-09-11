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

    # any module necessary for this one to work correctly
    'depends': ['mrp_repair'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/ctw_form.xml',
        'views/field_form.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
