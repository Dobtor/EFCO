# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################

from openerp import fields, models, api, tools
import openerp


class WebsiteGallery(models.Model):
    _name = 'website.gallery'
    _description = 'Website image gallery'
    _inherit = ['website.published.mixin']

    @api.model
    def _get_default_image(self, is_company, colorize=False):
        img_path = openerp.modules.get_module_resource(
            'website_image_gallery', 'static/src/img', 'gallery.png')
        with open(img_path, 'rb') as f:
            image = f.read()

        # colorize user avatars
        if not is_company and colorize:
            image = tools.image_colorize(image)

        return tools.image_resize_image_big(image.encode('base64'))

    @api.multi
    def _get_qty_images(self):
        for item in self:
            item.qty_images = len(item.child_ids)


    name = fields.Char(string='Name')
    active = fields.Boolean(string='Active', default=True)

    image = fields.Binary(
        "Variant Image", attachment=True,
        default=lambda self: self._get_default_image(False, True),
        help="This field holds the image used as image for the gallery, limited to 1024x1024px.")

    image_medium = fields.Binary("Medium-sized image", attachment=True,
        help="Medium-sized image of this gallery. It is automatically "\
             "resized as a 128x128px image, with aspect ratio preserved. "\
             "Use this field in form views or some kanban views.")
    image_small = fields.Binary("Small-sized image", attachment=True,
        help="Small-sized image of this gallery. It is automatically "\
             "resized as a 64x64px image, with aspect ratio preserved. "\
             "Use this field anywhere a small image is required.")
    child_ids = fields.Many2many('website.image', 'image_gallery_rel', 'image_id', 'gallery_id', 'Images')
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.user.company_id)
    user_id = fields.Many2one('res.users', string='Responsible', required=False, default=lambda self: self.env.user)
    qty_images = fields.Integer(string="Qty. Images", compute="_get_qty_images")

    @api.model
    def create(self, vals):
        tools.image_resize_images(vals)
        return super(WebsiteGallery, self).create(vals)

    @api.multi
    def write(self, vals):
        tools.image_resize_images(vals)
        return super(WebsiteGallery, self).write(vals)


class WebsiteImage(models.Model):
    _name = 'website.image'
    _description = 'Website image'
    _inherit = ['website.published.mixin']

    @api.model
    def _get_default_image(self, is_company, colorize=False):
        img_path = openerp.modules.get_module_resource(
            'website_image_gallery', 'static/src/img', 'gallery.png')
        with open(img_path, 'rb') as f:
            image = f.read()

        # colorize user avatars
        if not is_company and colorize:
            image = tools.image_colorize(image)

        return tools.image_resize_image_big(image.encode('base64'))


    name = fields.Char(string='Name')
    active = fields.Boolean(string='Active', default=True)

    image = fields.Binary(
        "Variant Image", attachment=True,
        default=lambda self: self._get_default_image(False, True),
        help="This field holds the image used as image for the gallery,"\
        "limited to 1024x1024px.")

    image_medium = fields.Binary("Medium-sized image", attachment=True,
        help="Medium-sized image of this gallery. It is automatically "\
             "resized as a 128x128px image, with aspect ratio preserved. "\
             "Use this field in form views or some kanban views.")
    image_small = fields.Binary("Small-sized image", attachment=True,
        help="Small-sized image of this gallery. It is automatically "\
             "resized as a 64x64px image, with aspect ratio preserved. "\
             "Use this field anywhere a small image is required.")
    company_id = fields.Many2one('res.company', string='Company',\
        required=True, default=lambda self: self.env.user.company_id)
    user_id = fields.Many2one('res.users', string='Responsible',\
        required=False, default=lambda self: self.env.user)
    gallery_ids = fields.Many2many(comodel_name='website.gallery',\
        relation='image_gallery_rel', column1='gallery_id',\
        column2='image_id', string='Galleries')

    @api.model
    def create(self, vals):
        tools.image_resize_images(vals)
        return super(WebsiteImage, self).create(vals)

    @api.multi
    def write(self, vals):
        tools.image_resize_images(vals)
        return super(WebsiteImage, self).write(vals)