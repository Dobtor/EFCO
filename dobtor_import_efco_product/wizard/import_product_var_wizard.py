# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import api, fields, models, _
from datetime import datetime
from odoo.exceptions import UserError, AccessError
import csv
import base64
import xlrd
from odoo.tools import ustr
import requests
import codecs

try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO

class import_product_var_wizard(models.TransientModel):
    _name="import.product.var.wizard"

    import_type = fields.Selection([
        ('csv','CSV File'),
        ('excel','Excel File')
        ], default="csv", string="Import CSV", required=True)
    file = fields.Binary(string="File",required=True)
    
    @api.multi
    def show_success_msg(self,counter,skipped_line_no):
        
        #to close the current active wizard        
        action = self.env.ref('dobtor_import_efco_product.sh_import_product_var_action').read()[0]
        action = {'type': 'ir.actions.act_window_close'} 
        
        #open the new success message box    
        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False                                   
        context = dict(self._context or {})
        dic_msg = str(counter) + " Records imported successfully"
        if skipped_line_no:
            dic_msg = dic_msg + "\nNote:"
        for k,v in skipped_line_no.items():
            dic_msg = dic_msg + "\nRow No " + k + " " + v + " "
        context['message'] = dic_msg   
        return {
            'name': 'Success',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sh.message.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': context,
            }   

    
    @api.multi
    def import_product_var_apply(self):

        product_tmpl_obj = self.env['product.template']
        #perform import lead
        if self and self.file:
            #For CSV
            if self.import_type == 'csv':
                counter = 1
                skipped_line_no = {}
                try:
                    file = str(base64.decodestring(self.file))
                    myreader = csv.reader(file.splitlines())
                    total_count = len(list(myreader))
                    myreader = csv.reader(file.splitlines())
                    skip_header=True
                    running_tmpl = None     
                    created_product_tmpl = False   
                    has_variant = False   
                                                         
                    for row in myreader:
                        try:
                            print('Count: {} / {}'.format(counter,total_count))          
                            if skip_header:
                                skip_header=False
                                counter = counter + 1
                                continue
                            
                            if row[0] not in (None,""):
                                var_vals = {}
                                if row[0] != running_tmpl:
                                    running_tmpl = row[0]
                                    tmpl_vals = {}
     
                                    # product name  
                                    tmpl_vals.update({'name' : row[0]})
                                    tmpl_vals.update({'sale_ok' : True})        
                                    tmpl_vals.update({'purchase_ok' : True})         
                                    # product type  
                                    if row[1].strip() == 'Service':
                                        tmpl_vals.update({'type' : 'service'})                                          
                                    elif row[1].strip() == 'Stockable Product':
                                        tmpl_vals.update({'type' : 'product'})                                                                                                         
                                    else:
                                        tmpl_vals.update({'type' : 'consu'})    
                                    # internal reference
                                    if row[2] not in (None,""):                                         
                                        tmpl_vals.update({'default_code' : row[2]})   
                                    # Part Number
                                    if row[3].strip() not in (None,""):
                                        search_part_number = self.env['part.number'].search([('name','=',row[3].strip())], limit = 1)
                                        if search_part_number:
                                            tmpl_vals.update({'old_part_code' : search_part_number.id })                                             
                                        else:
                                            search_part_number = self.env['part.number'].create({"name":row[3].strip()})                             
                                            tmpl_vals.update({'old_part_code' : search_part_number.id })  
                                    # Article Number
                                    if row[4].strip() not in (None,""):
                                        search_article_number = self.env['article.number'].search([('name','=',row[4].strip())], limit = 1)
                                        if search_article_number:
                                            tmpl_vals.update({'new_part_code' : search_article_number.id })                                             
                                        else:
                                            search_article_number = self.env['article.number'].create({"name":row[4].strip()})                                       
                                            tmpl_vals.update({'new_part_code' : search_article_number.id })  
                                    # category
                                    if row[5].strip() in (None,""):
                                        search_category = self.env['product.category'].search([('name','=','All')], limit = 1)
                                        if search_category:
                                            tmpl_vals.update({'categ_id' : search_category.id })                                             
                                        else:
                                            skipped_line_no[str(counter)] = " - Category -  not found. "                                         
                                            counter = counter + 1
                                            continue   
                                    else:
                                        search_category = self.env['product.category'].search([('name','=',row[5].strip())], limit = 1)
                                        if search_category:
                                            tmpl_vals.update({'categ_id' : search_category.id })    
                                        else:
                                            skipped_line_no[str(counter)] = " - Category not found. " 
                                            counter = counter + 1
                                            continue  
                                    exist_product = product_tmpl_obj.search([('name','=',tmpl_vals['name'])])
                                    if not exist_product:
                                        product_tmpl_obj.create(tmpl_vals)      
                                    else:
                                        skipped_line_no[str(counter)] ="Exist Product {}".format(tmpl_vals['name'])
                                counter = counter + 1                                                
                            else:
                                skipped_line_no[str(counter)]=" - Name is empty. "  
                                counter = counter + 1                                   
                                
                            
                        except Exception as e:
                            skipped_line_no[str(counter)]=" - Value is not valid. " + ustr(e)   
                            counter = counter + 1 
                            continue          
                            
                except Exception as e:
                    raise UserError(_("Sorry, Your csv file does not match with our format" + ustr(e)))
                
                if counter > 1:
                    completed_records = (counter - len(skipped_line_no)) - 2
                    res = self.show_success_msg(completed_records, skipped_line_no)
                    return res

            
            #For Excel
            if self.import_type == 'excel':
                
                counter = 1
                skipped_line_no = {}                  
                try:
                    wb = xlrd.open_workbook(file_contents=base64.decodestring(self.file))
                    sheet = wb.sheet_by_index(0)     
                    skip_header = True    
                    running_tmpl = None     
                    created_product_tmpl = False   
                    has_variant = False              
                             
                    for row in range(sheet.nrows):
                        try:
                            if skip_header:
                                skip_header = False
                                counter = counter + 1
                                continue
                            
                            if sheet.cell(row,0).value not in (None,""):
                                var_vals = {}
                                if sheet.cell(row,0).value != running_tmpl:
                                    running_tmpl = sheet.cell(row,0).value
                                    tmpl_vals = {}
                                    
                                    tmpl_vals.update({'name' : sheet.cell(row,0).value })
                                    tmpl_vals.update({'sale_ok' : True})
                                    tmpl_vals.update({'purchase_ok' : True})   

                                    if sheet.cell(row,1).value.strip() == 'Service':
                                        tmpl_vals.update({'type' : 'service'})                                          
                                    elif sheet.cell(row,1).value.strip() == 'Stockable Product':
                                        tmpl_vals.update({'type' : 'product'})                                                                            
                                    else:
                                        tmpl_vals.update({'type' : 'consu'})    
                                        
                                    if sheet.cell(row,5).value.strip() in (None,""):
                                        search_category = self.env['product.category'].search([('name','=','All')], limit = 1)
                                        if search_category:
                                            tmpl_vals.update({'categ_id' : search_category.id })                                             
                                        else:
                                            skipped_line_no[str(counter)] = " - Category -  not found. "                                         
                                            counter = counter + 1
                                            continue   
                                    else:
                                        search_category = self.env['product.category'].search([('name','=',sheet.cell(row,5).value.strip())], limit = 1)
                                        if search_category:
                                            tmpl_vals.update({'categ_id' : search_category.id })    
                                        else:
                                            skipped_line_no[str(counter)] = " - Category not found. " 
                                            counter = counter + 1
                                            continue     

                                    if sheet.cell(row,2).value not in (None,""):                                         
                                            tmpl_vals.update({'default_code' : sheet.cell(row,2).value })   
                                    
                                    if sheet.cell(row,3).value not in (None,""):                                         
                                        search_part_number = self.env['part.number'].search([('name','=',sheet.cell(row,3).value)], limit = 1)
                                        if search_part_number:
                                            tmpl_vals.update({'old_part_code' : search_part_number.id })                                             
                                        else:
                                            search_part_number = self.env['part.number'].create({"name":sheet.cell(row,3).value})                             
                                            tmpl_vals.update({'old_part_code' : search_part_number.id })     
                                    
                                    if sheet.cell(row,4).value not in (None,""):                                         
                                        search_article_number = self.env['article.number'].search([('name','=',sheet.cell(row,4).value)], limit = 1)
                                        if search_article_number:
                                            tmpl_vals.update({'new_part_code' : search_article_number.id })                                             
                                        else:
                                            search_article_number = self.env['article.number'].create({"name":sheet.cell(row,4).value})                             
                                            tmpl_vals.update({'new_part_code' : search_article_number.id })  

                                    created_product_tmpl = product_tmpl_obj.create(tmpl_vals)       

                                counter = counter + 1                                                
                            else:
                                skipped_line_no[str(counter)]=" - Name is empty. "  
                                counter = counter + 1                                   
                                
                            
                        except Exception as e:
                            skipped_line_no[str(counter)]=" - Value is not valid. " + ustr(e)   
                            counter = counter + 1 
                            continue          
                            
                except Exception as e:
                    raise UserError(_("Sorry, Your excel file does not match with our format" + ustr(e)))
                
                if counter > 1:
                    completed_records = (counter - len(skipped_line_no)) - 2
                    res = self.show_success_msg(completed_records, skipped_line_no)
                    return res
                            