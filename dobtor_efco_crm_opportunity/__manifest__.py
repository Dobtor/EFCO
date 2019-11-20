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
        'data/ir_seqence.xml',
        'security/crm_security.xml',
        'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
        'report/forecast_report_views.xml'
        # 'views/assets.xml'
    ],
}
