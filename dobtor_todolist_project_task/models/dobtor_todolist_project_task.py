# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.tools import html_escape as escape
from openerp.exceptions import Warning as UserError
from openerp.tools.translate import _ 

TODO_STATES = {'done': 'Done',
                'todo': 'TODO',
                'waiting': 'Waiting',
                'cancelled': 'Cancelled'}

class DobtorTodoListCore(models.Model):
    _inherit = 'dobtor.todolist.core'

    @api.model
    def create(self, vals):
        record = super(DobtorTodoListCore, self).create(vals)
        #task = self.env['project.task'].browse(record.ref_model)
        if record.ref_model:
            task = record.ref_model
        else:
            task = None
        self.send_todolist_email(record.name, record.state, record.reviewer_id.id, record.user_id.id, task)
        return record
        

    @api.multi
    def write(self, vals):
        old_names = dict(zip(self.mapped('id'), self.mapped('name')))
        record = super(DobtorTodoListCore, self).write(vals)
        for r in self:
            if (vals.get('state')):
                self.send_todolist_email(r.name, r.state, r.reviewer_id.id, r.user_id.id, r.ref_model)
                if self.env.user != r.reviewer_id and self.env.user != r.user_id:
                    raise UserError(_('Only users related to that subtask can change state.'))
            if vals.get('name'):
                self.send_todolist_email(r.name, r.state, r.reviewer_id.id, r.user_id.id, r.ref_model, old_name=old_names[r.id])
                if self.env.user != r.reviewer_id and self.env.user != r.user_id:
                    raise UserError(_('Only users related to that subtask can change state.'))
            if vals.get('user_id'):
                self.send_todolist_email(r.name, r.state, r.reviewer_id.id, r.user_id.id, r.ref_model)
        return record

    @api.multi
    def send_todolist_email(self, todo_name, todo_state, todo_reviewer_id, todo_user_id, ref_model=None, old_name=None):
        reviewer = self.env["res.users"].browse(todo_reviewer_id)
        user = self.env["res.users"].browse(todo_user_id)
        state = TODO_STATES[todo_state]
        if todo_state == 'done':
            state = '<span style="color:#080">' + state + '</span>'
        if todo_state == 'todo':
            state = '<span style="color:#A00">' + state + '</span>'
        if todo_state == 'cancelled':
            state = '<span style="color:#777">' + state + '</span>'
        if todo_state == 'waiting':
            state = '<span style="color:#b818ce">' + state + '</span>'

        if ref_model:
            subtype='Dobtor_TodoList_Project_Task.todolist_project_task_subtype'
        else:
            subtype='Dobtor_TodoList_Core.todolist_core_subtype'

        body = ''
        partner_ids = []
        if user == self.env.user and reviewer == self.env.user:
            body = '<p>' + '<strong>' + state + '</strong>: ' + escape(todo_name)
            subtype = False
        elif self.env.user == reviewer:
            body = '<p>' + escape(user.name) + ', <br><strong>' + state + '</strong>: ' + escape(todo_name)
            partner_ids = [user.partner_id.id]
        elif self.env.user == user:
            body = '<p>' + escape(reviewer.name) + ', <em style="color:#999">I updated todolist item assigned to me:</em> <br><strong>' + state + '</strong>: ' + escape(todo_name)
            partner_ids = [reviewer.partner_id.id]
        else:
            body = '<p>' + escape(user.name) + ', ' + escape(reviewer.name) + ', <em style="color:#999">I updated todolist item, now its assigned to ' + escape(user.name) + ': </em> <br><strong>' + state + '</strong>: ' + escape(todo_name)
            partner_ids = [user.partner_id.id, reviewer.partner_id.id]
        if old_name:
            body = body + '<br><em style="color:#999">Updated from</em><br><strong>' + state + '</strong>: ' + escape(old_name) + '</p>'
        else:
            body = body + '</p>'

        if ref_model:
            for r in ref_model:
                if user == self.env.user and reviewer == self.env.user:
                    subtype = False
                
                r.message_post(message_type='comment',
                            subtype=subtype,
                            body=body,
                            partner_ids=partner_ids)
        else:
            self.message_post(message_type='comment',
                        subtype=subtype,
                        body=body,
                        partner_ids=partner_ids)
            

class Task(models.Model):
    _inherit = "project.task"
    default_user = fields.Many2one('res.users', compute='_compute_default_user')
    todolist_ids = fields.One2many(
        comodel_name='dobtor.todolist.core',
        inverse_name='ref_id', 
        domain=[('ref_model', 'like', 'project.task')],
        string='Todo Item'
    )
    kanban_todolists = fields.Text(
        compute='_compute_kanban_todolists'
    )

    @api.multi
    def _compute_default_user(self):
        for record in self:
            if self.env.user != record.user_id and self.env.user != record.create_uid:
                record.default_user = record.user_id
            else:
                if self.env.user != record.user_id:
                    record.default_user = record.user_id
                elif self.env.user != record.create_uid:
                    record.default_user = record.create_uid
                elif self.env.user == record.create_uid and self.env.user == record.user_id:
                    record.default_user = self.env.user

    @api.multi
    def _compute_kanban_todolists(self):
        for record in self:
            result_string1 = ''
            result_string2 = ''
            result_string3 = ''

            for todo in record.todolist_ids:
                bounding_length = 25
                tmp_list = (todo.name).split()
                for index in range(len(tmp_list)):
                    if (len(tmp_list[index]) > bounding_length):
                        tmp_list[index] = tmp_list[index][:bounding_length] + '...'
                tmp_todo_name = " ".join(tmp_list)
                if todo.state == 'todo' and record.env.user == todo.user_id and record.env.user == todo.reviewer_id:
                    tmp_string3 = escape(u': {0}'.format(tmp_todo_name))
                    result_string3 += u'<li><b>TODO</b>{}</li>'.format(tmp_string3)
                elif todo.state == 'todo' and record.env.user == todo.user_id:
                    tmp_string1_1 = escape(u'{0}'.format(todo.reviewer_id.name))
                    tmp_string1_2 = escape(u'{0}'.format(tmp_todo_name))
                    result_string1 += u'<li><b>TODO</b> from <em>{0}</em>: {1}</li>'.format(tmp_string1_1, tmp_string1_2)
                elif todo.state == 'todo' and record.env.user == todo.reviewer_id:
                    tmp_string2_1 = escape(u'{0}'.format(todo.user_id.name))
                    tmp_string2_2 = escape(u'{0}'.format(tmp_todo_name))
                    result_string2 += u'<li>TODO for <em>{0}</em>: {1}</li>'.format(tmp_string2_1, tmp_string2_2)
            record.kanban_todolists = '<ul>' + result_string1 + result_string3 + result_string2 + '</ul>'

    
            
