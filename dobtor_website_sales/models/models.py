# -*- coding: utf-8 -*-
from openerp import models, fields, api


# class product_class_inhert(models.Model):
#     _inherit = 'dobtor_products_extend.products_class'
#     ClassObject = fields.One2many(
#         'dobtor_products_extend.products_relational', 'FKClass')


# class products_info_inhert(models.Model):
#     _inherit = 'dobtor_products_extend.products_info'
#     InfoObject = fields.One2many(
#         'dobtor_products_extend.products_relational', 'FKInfo')


# class products_content_inhert(models.Model):
#     _inherit = 'dobtor_products_extend.products_content'
#     ContentObject = fields.One2many(
#         'dobtor_products_extend.products_relational', 'FKContent')


# class Website(models.Model):
#     _inherit = 'website'

#     @api.multi
#     def get_class_rowspan(self, product):
#         sqlstr = (
#             'select c."name", c."FKClass",Count(c."FKClass") "Count" from (select a.product_id, a."FKClass" , b.name  from dobtor_products_extend_products_relational a '
#             'left JOIN  dobtor_products_extend_products_class b '
#             'on a."FKClass" = b.id where "product_id" = %s and "isvisible" = TRUE) c '
#             'where c."product_id" = %s '
#             'GROUP BY  c."FKClass", c."name" '
#             'ORDER BY c."FKClass" '
#         )
#         self._cr.execute(
#             sqlstr,
#             (product.id, product.id,)
#         )
#         res = []
#         for item in self._cr.fetchall():
#             res = res + [{
#                 'name': str(item[0]),
#                 'fkclass': int(item[1]),
#                 'count': int(item[2])
#             }]
#         return res

#     @api.multi
#     def get_info_rowspan(self, product):
#         sqlstr = (
#             'select "FKClass","FKInfo",Count("FKInfo") count from dobtor_products_extend_products_relational '
#             'where "FKClass" in  (select "FKClass" from dobtor_products_extend_products_relational '
#             'where "product_id" = %s '
#             'GROUP BY  "FKClass") AND "product_id" = %s '
#             'GROUP BY  "FKInfo","FKClass" '
#             'ORDER BY "FKClass","FKInfo" '
#         )
#         self._cr.execute(
#             sqlstr, (product.id, product.id,)
#         )
#         res = []
#         for item in self._cr.fetchall():
#             res = res + [{
#                 'fkclass': int(item[0]),
#                 'fkinfo': int(item[1]),
#                 'count': int(item[2])
#             }]
#         return res

#     @api.multi
#     def get_table_rowspan(self, product):
#         sqlstr = (
#             'WITH ClassData AS ( '
#             'select c."name", c."FKClass",Count(c."FKClass") "Count" from (select a.product_id, a."FKClass" , b.name  from dobtor_products_extend_products_relational a '
#             'left JOIN  dobtor_products_extend_products_class b '
#             'on a."FKClass" = b.id where "product_id" = %s and "isvisible" = TRUE) c '
#             'where c."product_id" = %s '
#             ' GROUP BY  c."FKClass", c."name" '
#             'ORDER BY c."FKClass" '
#             '), InfoData AS( '
#             'SELECT '
#             '"FKClass", array_to_string(ARRAY(SELECT unnest(array_agg("total"))), \',\') as infodata '
#             'FROM(select "FKClass", "FKInfo" || \'-\' || y.name || \'-\' || Count("FKInfo") "total" from dobtor_products_extend_products_relational x, dobtor_products_extend_products_info y '
#             '     where "FKClass" in (select "FKClass" from dobtor_products_extend_products_relational '
#             'where "product_id"=%s and "isvisible" = TRUE '
#             'GROUP BY  "FKClass") AND "product_id"=%s AND x."FKInfo"=y."id" '
#             'GROUP BY  "FKInfo", "FKClass", y.name '
#             'ORDER BY "FKClass", "FKInfo") d '
#             'GROUP BY "FKClass" '
#             ') '
#             'SELECT A.*, B.infodata  FROM ClassData A, InfoData B '
#             'WHERE A."FKClass" = B."FKClass" '
#         )
#         self._cr.execute(
#             sqlstr, (product.id, product.id, product.id, product.id,)
#         )
#         res = []
#         for item in self._cr.fetchall():
#             temp = []
#             for items in item[3].split(','):
#                 t = items.split('-')
#                 temp = temp + [{
#                     'fkinfo': int(t[0]),
#                     'infoname': t[1],
#                     'count':  int(t[2])
#                 }]
#             res = res + [{
#                 'name': item[0],
#                 'fkclass': int(item[1]),
#                 'infodata': list(temp)
#             }]
#         return res
