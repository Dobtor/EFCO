# -*- coding: utf-8 -*-

from openerp import models, fields, api


class dobtor_sidebar_menu(models.Model):
    _name = 'dobtor_sidebar_menu.dobtor_sidebar_menu'
    _order = 'sequence, id desc'
    sequence = fields.Integer(
        string='sequence',
    )
    shape = fields.Selection(
        [('rectangle', 'rectangle'), ('circle', 'circle')],
        default="rectangle",
        string="shape",
        required=True
    )
    iconType = fields.Selection(
        [('iconic', 'iconic font'), ('img', 'image')],
        default="",
        string="icon type",
        required=True
    )
    # img
    icon_img = fields.Binary(string="image")
    width = fields.Integer(
        string='width',
        default='32',
    )
    height = fields.Integer(
        string='height',
        default='32',
    )
    # font
    icon_font = fields.Char(
        string="iconic font",
    )
    size = fields.Integer(
        string="size",
        default='24'
    )
    font_color = fields.Char(
        string='font color',
        default='#FFF'
    )
    # display name
    display_name = fields.Boolean(
        string="display name",
        default=False
    )
    name = fields.Char(
        string='name',
    )
    # background
    background = fields.Char(
        string="background color",
        default='#333'
    )
    background_hover = fields.Char(
        string="hover color",
        default='#444'
    )
    background_width = fields.Integer(
        string="background width",
        default='44'
    )
    background_height = fields.Integer(
        string="background height",
        default='44'
    )
    # content or Url
    linkType = fields.Selection(
        string='link type',
        selection=[('url', 'Url '), ('content', 'Html Content')],
        required=True
    )
    # Content
    description = fields.Html("Content")
    content_background = fields.Char(
        string="content background",
        default='#FFF'
    )
    content_size = fields.Integer(
        string="content width",
        default='100'
    )
    url = fields.Char(
        string='Url',
        default='#'
    )


class Website_dobtor_sidebarmenu(models.Model):
    _inherit = 'website'

    @api.multi
    def get_dobtor_sidebarmenu(self):
        res = self.env['dobtor_sidebar_menu.dobtor_sidebar_menu'].search([],order='sequence, id desc')
        return res
