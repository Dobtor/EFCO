# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name" : "Import Product Variant from CSV/Excel file - Advance",
    "author" : "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "category": "Product",
    "summary": "This module useful to import product with product variant.",
    "description": """
    
This module useful to import product with product variant.

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
    "price": 25,
    "currency": "EUR"   
}
