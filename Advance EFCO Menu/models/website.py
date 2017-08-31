# -*- coding: utf-8 -*-
# Part of AppJetty. See LICENSE file for full copyright and licensing details.

from openerp import api, fields, models
from openerp.http import request


class WebsiteMenu(models.Model):
    _inherit = "website.menu"

    is_dobtormenu = fields.Boolean(string='Is dobtormenu...?')
    dobtormenu_type = fields.Selection([('2_col', '2 Columns'),
                                      ('3_col', '3 Columns'),
                                      ('4_col', '4 Columns')],
                                     default='3_col',
                                     string="dobtormenu type")

    dobtormenu_bg = fields.Boolean(string='Want to set dobtormenu background', default=False)
    dobtormenu_bg_img_color = fields.Selection([('bg_img', 'Background image'),
                                              ('bg_color', 'Background color')],
                                              default='bg_img',
                                              string="dobtormenu background selection")
    dobtormenu_bg_image = fields.Binary(string="Background image for dobtormenu")
    dobtormenu_bg_color = fields.Char(string="Background color for dobtormenu",
                                    default='#ccc',
                                    help="Background color for dobtormenu, for setting background color you have to pass hexacode here.")

    dobtor_category_slider = fields.Boolean(string='Want to display category slider', default=False)
    dobtor_carousel_header_name = fields.Char(string="Slider label",
                                       default="Latest",
                                       help="Header name for carousel slider in dobtormenu")
    dobtor_category_slider_position = fields.Selection([('left', 'Left'), ('right', 'Right')],
        default='left', string="Category Slider Position")

    dobtor_menu_name = fields.Boolean(string='Want to display menu name', default=True)
    dobtor_menu_icon = fields.Boolean(string='Want to display menu icon', default=False)
    dobtor_menu_icon_image = fields.Binary(string="Menu Icon", help="Menu icon for your menu")

    dobtor_display_menu_footer = fields.Boolean(string="Display menu footer", default=False,
        help="For displaying footer in dobtormenu")
    dobtor_menu_footer = fields.Html(string="Footer content",
                              help="Footer name for dobtormenu")


    dobtor_customize_menu_colors = fields.Boolean(string='Want to customize menu colors', default=False)
    dobtor_main_category_color = fields.Char(string='Main category color',
        help="Set color for main category in dobtormenu")
    dobtor_sub_category_color = fields.Char(string='Sub category color',
        help="Set color for sab category in dobtormenu")
    include_in_dobtormenu = fields.Boolean(
        string="Include in dobtor menu", help="Include in dobtor menu")
    menu_id = fields.Many2one('website.menu', string="Main menu")


class Website(models.Model):
    _inherit = 'website'

    @api.multi
    def get_website_category(self, submenu):
        categories = self.env['website.menu'].search([
            ('include_in_dobtormenu', '=', True),
            ('menu_id', '=', submenu.id)
        ], order="sequence")

        return categories

    def get_website_child_category(self, children):
        categories = self.env['website.menu'].search([
                ('menu_id', '=', children),
                ('include_in_dobtormenu', '=', True)], 
                order="sequence")
        return categories

