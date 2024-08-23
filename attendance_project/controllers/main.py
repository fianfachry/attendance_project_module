# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

class HrAttendance(http.Controller):
    @http.route('/attendance_project/projects', type="json", auth="user")
    def attendance_projects(self):
        """
        Retrieve a list of all projects and the current employee's project ID.
        
        Returns:
            list: A list of dictionaries containing project ID and name.
            int: The ID of the project associated with the current employee.
        """
        result = request.env['project.project'].search([])
        employee = request.env.user.employee_id
        return [{
            'id': res.id,
            'name': res.name
        } for res in result], employee.project_id.id

    @http.route('/attendance_project/tasks', type="json", auth="user")
    def attendance_tasks(self, project_id):
        """
        Retrieve a list of tasks for a specific project and the current employee's task ID.

        Args:
            project_id (int): The ID of the project for which tasks are to be retrieved.

        Returns:
            list: A list of dictionaries containing task ID and name.
            int: The ID of the task associated with the current employee.
        """
        result = request.env['project.task'].search([('project_id', '=', int(project_id))])
        employee = request.env.user.employee_id
        return [{
            'id': res.id,
            'name': res.name
        } for res in result], employee.task_id.id

    @http.route('/attendance_project/description', type="json", auth="user")
    def attendance_description(self):
        """
        Retrieve the description of the current employee.

        Returns:
            str: The description of the current employee.
        """
        return request.env.user.employee_id.description

    @http.route('/attendance_project/set_employee_value', type="json", auth="user")
    def set_employee_value(self, project_id, task_id, description):
        """
        Update the project, task, and description for the current employee.

        Args:
            project_id (int): The ID of the project to set.
            task_id (int): The ID of the task to set.
            description (str): The description to set for the employee.
        """
        employee = request.env.user.employee_id
        employee.write({
            'project_id': int(project_id),
            'task_id': int(task_id),
            'description': description
        })
