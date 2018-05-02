# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.tools import html2plaintext

class WebsiteBlogs(models.Model):
    _inherit = 'blog.post'

    teaser = fields.Text(
        'Teaser', compute='_compute_teaser', inverse='_set_teaser')
    teaser_manual = fields.Text(string='Teaser Content')
    @api.multi
    @api.depends('content', 'teaser_manual')
    def _compute_teaser(self):
        for blog_post in self:
            if blog_post.teaser_manual:
                blog_post.teaser = blog_post.teaser_manual
            else:
                content = html2plaintext(blog_post.content).replace('\n', ' ')
                blog_post.teaser = content[:150] + '...'

    @api.multi
    def _set_teaser(self):
        for blog_post in self:
            blog_post.teaser_manual = blog_post.teaser
