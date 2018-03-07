# -*- coding: utf-8 -*-

import openerp
from openerp import models, fields, api
from openerp.addons.base.res import res_request
from openerp.tools import html_escape as escape
from openerp.exceptions import Warning as UserError
from openerp.tools.translate import _

TODO_STATES = {'done': 'Done',
                  'todo': 'TODO',
                  'waiting': 'Waiting',
                  'cancelled': 'Cancelled'}

def referencable_models(self):
    return res_request.referencable_models(
        self, self.env.cr, self.env.uid, context=self.env.context)

class DobtorTodoListCore(models.Model):
    _name = "dobtor.todolist.core"
    _inherit = ['ir.needaction_mixin']
    state = fields.Selection([(k, v) for k, v in TODO_STATES.items()],
                             'Status', required=True, copy=False, default='todo')
    name = fields.Char(required=True, string="Description")
    reviewer_id = fields.Many2one('res.users', 'Reviewer', readonly=True, default=lambda self: self.env.user)
    user_id = fields.Many2one('res.users', 'Assigned to', required=True)
    hide_button = fields.Boolean(compute='_compute_hide_button')
    recolor = fields.Boolean(compute='_compute_recolor')
    ref_model = fields.Reference(referencable_models, "Refer To")
    ref_id = fields.Integer(string='ref_id')
    parent_model = fields.Reference(referencable_models, "Parent")
    survey_id = fields.Many2one("survey.survey", "Survey")

    @api.multi
    def _compute_recolor(self):
        for record in self:
            if self.env.user == record.user_id and record.state == 'todo':
                record.recolor = True

    @api.multi
    def _compute_hide_button(self):
        for record in self:
            if self.env.user not in [record.reviewer_id, record.user_id]:
                record.hide_button = True

    @api.multi
    def _compute_reviewer_id(self):
        for record in self:
            record.reviewer_id = record.create_uid

    @api.model
    def _needaction_domain_get(self):
        if self._needaction:
            return [('state', '=', 'todo'), ('user_id', '=', self.env.uid)]
        return []

    @api.multi
    def write(self, vals):
        
        if 'ref_model' in vals:
            vals['ref_id'] = vals['ref_model'].split(',')[1]
        result = super(DobtorTodoListCore, self).write(vals)
        # for r in self:
        #     if (vals.get('state')):
        #         r.ref_model.send_todolist_email(r.name, r.state, r.reviewer_id.id, r.user_id)
        #         if self.env.user != r.reviewer_id and self.env.user != r.user_id:
        #             raise UserError(_('Only users related to that subtask can change state.'))
        #     if vals.get('name'):
        #         r.ref_model.send_todolist_email(r.name, r.state, r.reviewer_id.id, r.user_id.id, old_name=old_names[r.id])
        #         if self.env.user != r.reviewer_id and self.env.user != r.user_id:
        #             raise UserError(_('Only users related to that subtask can change state.'))
        #     if vals.get('user_id'):
        #         r.ref_model.send_todolist_email(r.name, r.state, r.reviewer_id.id, r.user_id.id)
            
        return result

    @api.model
    def create(self, vals):
        if 'ref_model' in vals:
            vals['ref_id'] = vals['ref_model'].split(',')[1]
        result = super(DobtorTodoListCore, self).create(vals)
        vals = self._add_missing_default_values(vals)
        # task = self.env['project.task'].browse(vals.get('task_id'))
        # task.send_subtask_email(vals['name'], vals['state'], vals['reviewer_id'], vals['user_id'])
        return result

    @api.multi
    def change_state_done(self):
        for record in self:
            record.state = 'done'

    @api.multi
    def change_state_todo(self):
        for record in self:
            record.state = 'todo'

    @api.multi
    def change_state_cancelled(self):
        for record in self:
            record.state = 'cancelled'

    @api.multi
    def change_state_waiting(self):
        for record in self:
            record.state = 'waiting'