# -*- coding: utf-8 -*-

from openerp import models, fields, api


class FixedTop(models.Model):
    _name = 'dobtor_theme.fixedtop'

    IsFixedTop = fields.Boolean(
        string='IsFixedTop',
        default=False,
        required=True,
    )

    @api.one
    def toggle_IsFixedTop(self):
        self.IsFixedTop = not self.IsFixedTop


# class customize(models.Model):
#     _name = 'dobtor_theme.customize'

#     Customize = fields.Boolean(
#         string='Customize',
#         default=False,
#         required=True,
#     )

#     Background_Color = fields.Char(
#         string='Background Color',
#         default='#FFF',
#         required=True
#     )

#     Font_Color = fields.Char(
#         string='Font Color',
#         default='#000',
#         required=True
#     )

#     Panel_Color = fields.Char(
#         string='Panel Color',
#         default='#EEE',
#         required=True
#     )

#     Panel_Font_Color = fields.Char(
#         string='Panel Font Color',
#         default='#000',
#         required=True
#     )

#     Element_Color = fields.Char(
#         string='Element Color',
#         default='#337ab7',
#         required=True
#     )

#     Element_Font_Color = fields.Char(
#         string='Element Font Color',
#         default='#FFF',
#         required=True
#     )

#     Layout_Font_Color = fields.Char(
#         string='Layout Font Color',
#         default='#FFF',
#         required=True
#     )

#     Layout_Hover_Color = fields.Char(
#         string='Layout Hover Color',
#         default='#777',
#         required=True
#     )

#     Layout_Background_Color = fields.Char(
#         string='Layout Background Color',
#         default='#000',
#         required=True
#     )

#     @api.one
#     def toggle_Customize(self):
#         self.Customize = not self.Customize

    # @api.one
    # def Update_Background_Color(self, color):
    #     self.Update_Background_Color = color

# class Website(models.Model):
#     _inherit = 'website'

#     @api.multi
#     def get_customize(self):
#         return self.env['dobtor_theme.customize'].search([])
