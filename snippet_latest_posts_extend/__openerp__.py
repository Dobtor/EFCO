# -*- coding: utf-8 -*-
{
    'name': "snippet_latest_posts_extend",
    'summary': """部落格功能擴充和(Odoo10) Backports""",
    'description': """
        1. Backports 部落格選單, 顯示部分內文.
        2. Backports 部落格選單, 顯示圖片.
        3. Backports 部落格選單, 顯示author avatar.
        4. extend    部落格選單, 可以關閉或顯示內文.
    """,
    'author': "Dobtor SI",
    'website': "http://www.dobtor.com",
    'category': 'website_blog',
    'version': '0.1',
    'depends': ['snippet_latest_posts'],
    'data': [
        'views/s_latest_posts.xml',
        'views/options.xml',
    ],
}
