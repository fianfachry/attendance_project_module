from odoo import models, fields, api

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    project_id = fields.Many2one(
        'project.project',
        compute='_get_employee_value',
        store=True,
        string='Project',
        help='The project of the attendance'
    )
    task_id = fields.Many2one(
        'project.task',
        compute='_get_employee_value',
        store=True,
        string='Task',
        help='The task of the attendance'
    )
    description = fields.Text(
        compute='_get_employee_value',
        store=True,
        string='Description',
        help='Activity description of the attendance'
    )

    @api.depends('employee_id')
    def _get_employee_value(self):
        """
        Compute the project, task, and description based on the employee's current details.
        This method is triggered when the `employee_id` field is changed, i.e. in the begining of attendance creation.
        """
        for rec in self:
            employee_id = rec.employee_id
            if employee_id:
                rec.project_id = employee_id.project_id
                rec.task_id = employee_id.task_id
                rec.description = employee_id.description
            else:
                # Clear the values if employee_id is not set
                rec.project_id = False
                rec.task_id = False
                rec.description = False
