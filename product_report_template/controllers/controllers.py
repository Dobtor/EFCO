# -*- coding: utf-8 -*-
from openerp import http
from openerp.http import request

class ProductReportTemplates(http.Controller):

    @http.route(['/product_report/print/<model("product.template"):product>'],
                type='http', auth="public", website=True)
    def view(self, product, **post):
        """print product to pdf
        Arguments:
            product {[model]} -- product.template model
            **post {[dict]} -- other parameter
        Returns:
            [application/pdf] -- print pdf or http status code 404
        """
        if product:
            pdf = http.request.env['report'].sudo().with_context(
                set_viewport_size=True).get_pdf(product, 'product_report_template.product_report_print')
            pdfhttpheaders = [('Content-Type', 'application/pdf'),
                              ('Content-Length', len(pdf))]
            return request.make_response(pdf, headers=pdfhttpheaders)
        return request.not_found()
