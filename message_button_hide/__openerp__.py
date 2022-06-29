# -*- encoding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#
#    Author: Andrius Laukavičius. Copyright: JSC NOD Baltic
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
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
    'name': 'Message Button Hide',
    'version': '1.0',
    'category': 'Discuss',
    'description': """
Message Button Hide
==========================================
    """,
    'author': 'Dobtor',
    'website': 'www.dobtor.com',
    'depends': ['base', 'base_setup', 'bus'],
    'installable': True,
    'auto_install': False,
    'data': [
            'views/mail_templates.xml',
    ],
    'qweb': [
            'static/src/xml/chatter.xml',
    ],
}
