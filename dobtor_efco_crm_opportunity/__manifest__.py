# -*- coding: utf-8 -*-
{
    'name': "dobtor_efco_crm_opportunity",
    'summary': """
        extend crm opportunity
    """,
    'description': """
        extend crm opportunity
    """,
    'author': "Dobtor SI",
    'website': "http://www.dobtor.com",
    'category': 'crm',
    'version': '0.1',
    'depends': [
        'base',
        'crm',
        'product',
        'sales_team',
        'dobtor_efco_rma'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
        'report/crm_expected_icome_report_views.xml'
        # 'views/assets.xml'
    ],
}
