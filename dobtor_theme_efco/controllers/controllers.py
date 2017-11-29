# -*- coding: utf-8 -*-
from openerp import http
import json


class DobtorTheme(http.Controller):
    # @http.route('/dobtor_theme/customize/read/', auth='public', type='json', website=True, method=['POST'])
    # def read_theme_color(self, **kw):
    #     res = http.request.env['dobtor_theme.customize'].search([])
    #     jsondata = []
    #     if len(res) > 0:
    #         for val in res:
    #             jsondata.append({
    #                 'Customize': val.Customize,
    #                 'Background_Color': val.Background_Color,
    #                 'Font_Color': val.Font_Color,
    #                 'Panel_Color': val.Panel_Color,
    #                 'Panel_Font_Color': val.Panel_Font_Color,
    #                 'Element_Color': val.Element_Color,
    #                 'Element_Font_Color': val.Element_Font_Color,
    #                 'Layout_Font_Color': val.Layout_Font_Color,
    #                 'Layout_Hover_Color': val.Layout_Hover_Color,
    #                 'Layout_Background_Color': val.Layout_Background_Color,
    #                 'status': 'Done'
    #             })
    #         return json.dumps(jsondata[-1])
    #     return json.dumps({'status': 'nothing'})

    # @http.route('/dobtor_theme/customize/write/', auth='public', type='json', website=True, method=['POST'])
    # def write_background_color(self, **kw):
    #     res = http.request.env['dobtor_theme.customize'].search([])
    #     if len(res) > 0:
    #         http.request.env['dobtor_theme.customize'].search([])[-1].write({
    #             'Customize': True,
    #             'Background_Color': kw.get('Background_Color'),
    #             'Font_Color': kw.get('Font_Color'),
    #             'Panel_Color': kw.get('Panel_Color'),
    #             'Panel_Font_Color': kw.get('Panel_Font_Color'),
    #             'Element_Color': kw.get('Element_Color'),
    #             'Element_Font_Color': kw.get('Element_Font_Color'),
    #             'Layout_Font_Color': kw.get('Layout_Font_Color'),
    #             'Layout_Hover_Color': kw.get('Layout_Hover_Color'),
    #             'Layout_Background_Color': kw.get('Layout_Background_Color'),
    #         })
    #     else:
    #         http.request.env['dobtor_theme.customize'].create({
    #             'Customize': kw.get('Customize'),
    #             'Background_Color': kw.get('Background_Color'),
    #             'Font_Color': kw.get('Font_Color'),
    #             'Panel_Color': kw.get('Panel_Color'),
    #             'Panel_Font_Color': kw.get('Panel_Font_Color'),
    #             'Element_Color': kw.get('Element_Color'),
    #             'Element_Font_Color': kw.get('Element_Font_Color'),
    #             'Layout_Font_Color': kw.get('Layout_Font_Color'),
    #             'Layout_Hover_Color': kw.get('Layout_Hover_Color'),
    #             'Layout_Background_Color': kw.get('Layout_Background_Color'),
    #         })
    #     return json.dumps({'status': 'Done!'})

    # @http.route('/dobtor_theme/customize/toggle/', auth='public', type='json', website=True, method=['POST'])
    # def write_Customize(self, **kw):
    #     res = http.request.env['dobtor_theme.customize'].search([])
    #     if len(res) > 0:
    #         http.request.env['dobtor_theme.customize'].search(
    #             [])[-1].toggle_Customize()
    #     else:
    #         http.request.env['dobtor_theme.customize'].search([]).create({
    #             'Customize': kw.get('Customize'),
    #         })
    #     return json.dumps({'status': 'Done'})

    @http.route('/dobtor_theme/fixedtop/toggle/', auth='public', type='json', website=True, method=['POST'])
    def write_IsFixedTop(self, **kw):
        res = http.request.env['dobtor_theme.fixedtop'].search([])
        if len(res) > 0:
            http.request.env['dobtor_theme.fixedtop'].search(
                [])[-1].toggle_IsFixedTop()
        else:
            http.request.env['dobtor_theme.fixedtop'].search([]).create({
                'IsFixedTop': kw.get('fixedtop'),
            })
        return json.dumps({'status': 'Done'})

    @http.route('/dobtor_theme/fixedtop/read/', auth='public', type='json', website=True, method=['POST'])
    def read_fixedtop(self, **kw):
        res = http.request.env['dobtor_theme.fixedtop'].search([])
        jsondata = []
        if len(res) > 0:
            for val in res:
                jsondata.append({
                    'IsFixedTop': val.IsFixedTop,
                    'status': 'Done'
                })
            return json.dumps(jsondata[-1])
        return json.dumps({'status': 'nothing'})
