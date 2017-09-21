# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################

from openerp import http, SUPERUSER_ID
from openerp.http import request

PPG = 12  # Partners Per Page
#PPR = 4  # Partners Per Row


class WebsiteGallery(http.Controller):

    @http.route(['/page/gallery',
                 '/page/gallery/page/<int:page>'], type='http', auth="public", website=True)
    def gallery(self, page=0, ppg=False, **post):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
        url = '/page/gallery'

        if ppg:
            try:
                ppg = int(ppg)
            except ValueError:
                ppg = PPG
            post["ppg"] = ppg
        else:
            ppg = PPG

        wg_obj = request.registry['website.gallery']
        domain = []
        if not wg_obj.check_access_rights(cr, uid, 'write', raise_exception=False):
            domain = [("website_published", "=", True)]
        gallery_count = wg_obj.search_count(
            cr, uid, domain, context=context)
        pager = request.website.pager(
            url=url, total=gallery_count, page=page, step=ppg, scope=7)
        galleries = wg_obj.search(
            cr, uid, domain, limit=ppg, offset=pager['offset'], order="write_date desc, website_published desc", context=context)

        values = {
            'galleries': wg_obj.browse(cr, uid, galleries, context),
            'pager': pager,
            #'rows': PPR
        }
        return request.website.render("website_image_gallery.ws_page_gallery", values)

    @http.route(['/page/gallery/images/<int:gallery_id>',
                 '/page/gallery/images/<int:gallery_id>/page/<int:page>'], type='http', auth="public", website=True)
    def images(self, gallery_id, page=0, ppg=False, **post):
        PPG = 18 #Update PPG per not div create (Add a gallery...)
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
        url = '/page/gallery/images/' + str(gallery_id)

        if ppg:
            try:
                ppg = int(ppg)
            except ValueError:
                ppg = PPG
            post["ppg"] = ppg
        else:
            ppg = PPG

        wg_obj = request.registry['website.gallery']
        gallery = wg_obj.browse(cr, uid, gallery_id, context)
        img_ids = gallery.child_ids.ids
        wi_obj = request.registry['website.image']
        domain = [("id", "in", img_ids)]
        if not wi_obj.check_access_rights(cr, uid, 'write', raise_exception=False):
            domain = [("website_published", "=", True), ("id", "in", img_ids)]
        img_count = wi_obj.search_count(
            cr, uid, domain, context=context)
        pager = request.website.pager(
            url=url, total=img_count, page=page, step=ppg, scope=7)
        images = wi_obj.search(
            cr, uid, domain, limit=ppg, offset=pager['offset'], order="write_date desc, website_published desc", context=context)

        values = {
            'images': wi_obj.browse(cr, uid, images, context),
            'gallery': gallery,
            'pager': pager,
            #'rows': PPR
        }
        return request.website.render("website_image_gallery.ws_page_images", values)
