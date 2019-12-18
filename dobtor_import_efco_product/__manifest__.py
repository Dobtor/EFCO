# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name" : "Import EFCO Product from CSV file - Advance",
    "author" : "Dobtor SI",
    "website": "https://www.dobtor.com",
    "category": "Product",
    "summary": "This module useful to import product.",
    "description": """
    
This module useful to import product .

                    """,    
    "version":"10.0.2",
    "depends" : ["base","sale","sh_message","product","stock","account","sales_team","dobtor_efco_rma"],
    "application" : True,
    "data" : ['security/import_product_var_security.xml',

            'wizard/import_product_var_wizard.xml',
            'views/sale_view.xml',
            ],         
    'external_dependencies' : {
        'python' : ['xlrd'],
    },                  
    "images": ["static/description/background.png",],              
    "auto_install":False,
    "installable" : True,

}
