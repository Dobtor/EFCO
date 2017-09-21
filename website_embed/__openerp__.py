# -*- coding: utf-8 -*-
# © 2015 Nedas Žilinskas <nedas.zilinskas@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Embed HTML Building Block",
    "summary": "Allows to easily embed HTML into website",
    "version": "9.0.1.0.0",
    "category": "Website",
    "website": "http://nedaszilinskas.com/",
    "author": "Nedas Žilinskas <nedas.zilinskas@gmail.com>",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "website",
    ],
    "data": [
        "data/x_website_embed.xml",
        "security/ir.model.access.csv",
        "views/assets.xml",
        "views/snippet.xml",
        "views/x_website_embed.xml",
    ],
    "images": [
        "static/description/main_screenshot.png",
    ],
    "price": 19.99,
    "currency": "EUR"
}
