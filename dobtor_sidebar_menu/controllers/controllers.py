# -*- coding: utf-8 -*-
from openerp import http
import json


class DobtorSidebarMenu(http.Controller):
    @http.route('/dobtor_sidebar_menu/dobtor_sidebar_menu/', auth='public', type='json', website=True, method=['POST'])
    def read_sidebar_menu(self, **kw):
        res = http.request.env['dobtor_sidebar_menu.dobtor_sidebar_menu'].search([],order='sequence, id desc')
        jsondata = []
        if len(res) > 0:
            for val in res:
                jsondata.append({
                    'id': val.id,
                    'shape': val.shape,
                    'iconType': val.iconType,
                    'width': val.width,
                    'height': val.height,
                    'size': val.size,
                    'font_color': val.font_color,
                    'background': val.background,
                    'background_hover': val.background_hover,
                    'background_width': val.background_width,
                    'background_height': val.background_height,
                    'linkType': val.linkType,
                    'url': val.url,
                    'description': val.description,
                    'display_name': val.display_name,
                    'name': val.name,
                    'content_size': val.content_size,
                })
        return json.dumps(jsondata)
