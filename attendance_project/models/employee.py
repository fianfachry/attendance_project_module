from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    project_id = fields.Many2one(
        'project.project',
        string='Project',
        help="The project of the employee's latest attendance"
    )
    task_id = fields.Many2one(
        'project.task',
        string='Task',
        help="The task of the employee's latest attendance"
    )
    description = fields.Text(
        string='Description',
        help="The activity description of the employee's latest attendance"
    )