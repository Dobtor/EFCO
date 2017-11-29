# -*- coding: utf-8 -*-
{
    'name': "dobtor_theme_efco",
    'summary': """
        dobtor custom theme
    """,
    'description': """
    將模版整合為單一模組，並可以由設計師自定要套用哪一個模版
        色調的顏色控制欄位需可以填入色碼，網站內容的Block會套用同樣色調，理想位置最好是在前台Customize Theme的子介面上
        客製化按鈕的超連結，需要有可以設定的後台欄位，理想位置在Website admin/configuration的頁面裡
        隨頁移動的箭頭，其上方可以增加圖片，滑鼠移至圖片時會顯示第二張圖片，此圖片效果需可以從後台新增，項目數量可以新增
    """,
    'author': "dobtor SI",
    'website': "http://www.yourcompany.com",
    'category': 'dobtor',
    'version': '0.1',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        # 'demo/demo.xml',
        'views/template.xml',
        'views/snippet.xml',
    ],
    'demo': [

    ],
}
