# -*- coding: utf-8 -*-

import csv
import io
import logging
import base64
from odoo import fields, models, api, _

_logger = logging.getLogger(__name__)

try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO



class import_products(models.TransientModel):
    _name = "import.products"
   
    file_path = fields.Binary(type='binary', string="File To Import")

    def _read_csv_data(self, binary_data):
        """
            Reads CSV from given path and Return list of dict with Mapping
        """
        data = csv.reader(StringIO(base64.b64decode(self.file_path).decode('utf-8')), quotechar='"', delimiter=',')

        # Read the column names from the first line of the file
        fields = next(data)
        data_lines = []
        for row in data:
            items = dict(zip(fields, row))
            data_lines.append(items)
        return fields, data_lines

    def do_import_product_data(self):
        file_path = self.file_path
        if not file_path or file_path == "":
            _logger.warning("Import can not be started. Configure your schedule Actions.")
            return True
        fields = data_lines = False

        try:
            fields, data_lines = self._read_csv_data(file_path)
        except:
            _logger.warning("Can not read source file(csv) '%s', Invalid file path or File not reachable on file system."%(file_path))
            return True
        if not data_lines:
            _logger.info("File '%s' has no data or it has been already imported, please update the file."%(file_path))
            return True
        _logger.info("Starting Import Product Process from file '%s'."%(file_path))
        product_tmpl_obj = self.env['product.template']
        product_attribute = self.env['product.attribute']

        bounced_cust = [tuple(fields)]
        error_lst=[]
        product_tmpl_id = False

        rem_product_tmpl_desc = []
        duplicate_product_template = []
        
        
        variant_list = []
        stock_move_line_list = []
        stock_inventory_obj = self.env['stock.inventory']
        location_id = stock_inventory_obj._default_location_id()


        record = 0

        for data in data_lines:
            
            # Product
            name = data['Product Name']
            # categ_id = data['Product Category'] or False # Internal Category
            # default_code = data['Internal Reference'] or False # Internal Reference
            # color = data['Color'] or False # Color
            # size = data['Size'] or False # Size
            # list_price = data['Sale price'] or False # Sales price
            # barcode = data['EAN'] or False # Barcode
            # quantity = data['Stock'] or False # Stock
            article_number = data['Article Number'] or False
            part_number = data['Part Number']  or False
            
            # Remove extra spaces
            name = name.strip()
            # categ_id = categ_id.strip()
            # color = color.strip()
            # size = size.strip()
            # default_code = default_code.strip()
            # barcode = barcode.strip()
            article_number = article_number.strip()
            part_number = part_number.strip()

            ir_model_data_obj = self.env['ir.model.data']
            product_category_obj = self.env['product.category']
            attribute_value_obj = self.env['product.attribute.value']

            try:
                internal_categ_id = False
                internal_categ_id = product_category_obj.search([('name', '=', 'All')])
                if not internal_categ_id:
                    internal_categ_id = product_category_obj.create({'name': 'All'})
                
                # Product Attributes get
                # attribute_color_id = product_attribute.search([('name', '=', 'Color')])
                # if not attribute_color_id:
                #     attribute_color_id = product_attribute.create({'name': 'Color'})

                # attribute_size_id = product_attribute.search([('name', '=', 'Size')])
                # if not attribute_size_id:
                #     attribute_size_id = product_attribute.create({'name': 'Size'})

                # attribute_color_value_id_lis = []
                # attribute_color_value_id = False
                # if color:
                #     for cl in color.split('/'):
                #         attribute_color_value_id = attribute_value_obj.search([('name', '=', cl), ('attribute_id', '=', attribute_color_id.id)])
                #         if attribute_color_value_id:
                #             attribute_color_value_id_lis.append(attribute_color_value_id.id)
                #         else:
                #             attribute_color_value_id = attribute_value_obj.create({'attribute_id': attribute_color_id.id, 'name': cl})
                #             attribute_color_value_id_lis.append(attribute_color_value_id.id)
                            
                # attribute_size_value_id_lis = []
                # attribute_size_value_id = False
                # if size:
                #     for sz in size.split('/'):
                #         attribute_size_value_id = attribute_value_obj.search([('name', '=', sz), ('attribute_id', '=', attribute_size_id.id)])
                #         if attribute_size_value_id:
                #             attribute_size_value_id_lis.append(attribute_size_value_id.id)
                #         else:
                #             attribute_size_value_id = attribute_value_obj.create({'attribute_id': attribute_size_id.id, 'name': sz})
                #             attribute_size_value_id_lis.append(attribute_size_value_id.id)
              
                # attribute_value_list = []
                # if attribute_color_value_id:
                #     attribute_value_list.append([0, 0, {'attribute_id': attribute_color_id.id, 'value_ids': [(6,0, attribute_color_value_id_lis)]}])
                # if attribute_size_value_id:
                #     attribute_value_list.append([0, 0, {'attribute_id': attribute_size_id.id, 'value_ids': [(6,0, attribute_size_value_id_lis)]}])

                exist_product_template = product_tmpl_obj.search([('name', '=', name),('new_part_code','=',article_number),('old_part_code','=',part_number)])
                
                product_barcode = False
                # if barcode:
                #     product_barcode = self.env['product.product'].search([('barcode', '=', barcode)])
                #     if not product_barcode:
                #         barcode_search = '0' + str(barcode)
                #         product_barcode = self.env['product.product'].search([('barcode', '=', barcode_search)])

                if article_number:
                    product_new_part_code =  self.env['article.number'].search([('name', '=', article_number)],limit = 1)
                    if not product_new_part_code:
                        product_new_part_code = self.env['article.number'].create({"name":part_number})
                
                if part_number:
                    product_old_part_code =  self.env['part.number'].search([('name', '=', part_number)],limit = 1)
                    if not product_old_part_code:
                        product_old_part_code = self.env['part.number'].create({"name":part_number})

                if len(exist_product_template.ids) != 1:
                    for dup in exist_product_template:
                        duplicate_product_template.append({'default_code': dup.default_code})
                    exist_product_template_test = product_tmpl_obj.search([('name', '=', name),('new_part_code','=',article_number),('old_part_code','=',part_number)])
                    if not exist_product_template_test and exist_product_template:
                        exist_product_template = exist_product_template[0]
                    else:
                        exist_product_template = exist_product_template_test
                
                if exist_product_template:
  
                    # if attribute_color_id:
                    #     exist_color_line = exist_product_template.attribute_line_ids.filtered(lambda a: a.attribute_id.id == attribute_color_id.id)
                    #     exist_color_line.value_ids = attribute_color_value_id_lis
                    #     exist_product_template.create_variant_ids()
                    # if attribute_size_id:
                    #     exist_size_line = exist_product_template.attribute_line_ids.filtered(lambda a: a.attribute_id.id == attribute_size_id.id)
                    #     exist_size_line.value_ids = attribute_size_value_id_lis
                    #     exist_product_template.create_variant_ids()
                    # for variant in exist_product_template.product_variant_ids.filtered(lambda self: self.id not in variant_list):
                    #     stock_move_line_list.append([0, 0, {'product_id': variant.id, 'product_qty': quantity, 'location_id': location_id}])
                    #     variant_list.append(variant.id)
                    print('Exist')
                else:
                    product_template_vals = {
                        'name': name,
                        'old_part_code':product_old_part_code.id if product_old_part_code else False,
                        'new_part_code':product_new_part_code.id if product_new_part_code else False,
                        'categ_id':internal_categ_id.id,
                        'type': 'product',
                    }
                    
                    # if attribute_value_list:
                    #     product_template_vals['attribute_line_ids'] = attribute_value_list
                    product_tmpl_id = product_tmpl_obj.create(product_template_vals)
                    # for variant in product_tmpl_id.product_variant_ids:
                    #     stock_move_line_list.append([0, 0, {'product_id': variant.id, 'product_qty': quantity, 'location_id': location_id}])
                    #     variant_list.append(variant.id)
                record += 1
                print ("Successfully", record)
            except Exception as e:
                error_lst.append(e)
                reject = [data.get(f, '') for f in fields]
                bounced_cust.append(reject)
                continue

        # if stock_move_line_list:
        #     stock_inventory = stock_inventory_obj.create({'name': 'Bulk Import', 'filter': 'partial', 'line_ids': stock_move_line_list})
        #     stock_inventory.action_start()
        #     for line in stock_inventory.line_ids:
        #         line._onchange_product_id()
        #     stock_inventory.action_done()

        context = self.env.context.copy()
        self.env.context = context
        return {
                'name': _('Notification'),
                'context': context,
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'output',
                'type': 'ir.actions.act_window',
                'target':'new'
                }

class output(models.TransientModel):
    _name = 'output'
    _description = "Bounce file Output"

    file_path = fields.Char('File Location', size=128)
    file = fields.Binary(type='binary', string="Download File",readonly=True)
    flag = fields.Boolean('Flag')
    note = fields.Text('Note')