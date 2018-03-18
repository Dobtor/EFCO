# -*- coding: utf-8 -*-

from openerp import models, fields, api



class SurveyHistory(models.Model):
    _name = 'dobtor.todolist.user_input.ref'
    @api.depends('todolist_ids')
    def _compute_response_id(self):
        for recode in self:
            recode.reject = recode.todolist_ids.response_id

    todolist_ids = fields.Many2one(
        comodel_name='dobtor.todolist.core',
        string='ToDoList'
    )
    user_input_ids = fields.Many2one(
        comodel_name='survey.user_input',
        string='history survey',
    )
    user_input_name = fields.Char(string="user input")


    reject = fields.Integer(string="reject", 
                            compute='_compute_response_id'
    )
    # @api.multi
    # def _todolist_score(self):
    #     ret = dict()
    #     for user_input in self.browse([]):
    #         ret[user_input.id] = sum(
    #             [uil.todo_mark for uil in user_input.todolist_ids] or [0.0])
    #     return ret

    # todolist_score = fields.Float(compute=_todolist_score, string="Score for the todo")
    # todo_mark= fields.Float("Score given for this choice")
    @api.multi
    def reject_action(self):
        for record in self:
            record.todolist_ids.response_id = None
                
class SurveyUserInput(models.Model):

    _inherit = 'survey.user_input'
    todolist_user_input_ids = fields.One2many(
        string='user_input',
        comodel_name='dobtor.todolist.user_input.ref',
        inverse_name='user_input_ids',
    )
