# -*- coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Website image gallery',
    'description': 'Create page image gallery in website',
    'summary': 'Create page image gallery in website and pubilc image gallery in website.',
    'category': 'Website',
    'version': '1.0',
    'website': 'http://www.bitodoo.com/',
    "license": "AGPL-3",
    'author': 'BuildFish, Bitodoo',
    'depends': [
        'website_prettyPhoto',
    ],
    'data': [
        'data/data.xml',
        'views/website_gallery_view.xml',
        'views/template_gallery.xml',
        'security/ir.model.access.csv',
        'security/access_gallery.xml'
    ],
    'demo': [
        'galley_image_demo.xml'
    ],
    'price': 40.00,
    'currency': 'EUR',
    'images': ['images/main_screenshot.png'],
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
