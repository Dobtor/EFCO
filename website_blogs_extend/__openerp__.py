# -*- coding: utf-8 -*-
{
    'name': "website_blogs_extend",
    'summary': """部落格功能擴充和(Odoo10) Backports""",
    'description': """
        1. Backports 部落格選單, 顯示部分內文.
        2. Backports 部落格選單, 顯示圖片.
        3. Backports 部落格選單, 顯示author avatar.
        4. extend    部落格選單, 可以關閉或顯示內文.
    """,
    'author': "Dobtor SI",
    'website': "http://www.dobtor.com",
    'category': 'website',
    'version': '0.1',
    "license": "LGPL-3",
    'depends': ['website','website_blog'],
    'data': [
        'views/website_blog_templates.xml',
    ],
}
