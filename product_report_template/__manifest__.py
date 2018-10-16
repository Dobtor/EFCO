# -*- coding: utf-8 -*-
{
    'name': "product_report_template",
    'summary': "Product report (PDF)",
    'description': "Product report (PDF)",
    'author': "dobtor SI",
    'website': "http://www.dobtor.com",
    'category': 'report',
    'version': '0.1',
    'depends': ['base', 'sale', 'report', 'website_sale', 'dobtor_website_sales', 'dobtor_product_setting'],
    'data': [
        'data/report_paperformat.xml',
        'views/layout_templates.xml',
        'views/product_views.xml',
        'views/product_report_template_views.xml',
        'views/report_template.xml',
        'views/product_template.xml',
    ],
}
