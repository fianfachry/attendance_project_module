/* @odoo-module */

import { ActivityMenu } from "@hr_attendance/components/attendance_menu/attendance_menu";
import { patch } from "@web/core/utils/patch";

patch(ActivityMenu.prototype, {
    setup() {
        super.setup(...arguments);
        this.state.currentProject = false;
        this.state.currentTask = false;
        this.state.description = '';
        this.state.projects = [];
        this.state.tasks = [];
        this.setProjectRelated();
        this.setDescription();
    },

    /**
     * Fetches projects and sets the current project.
     * Also initializes tasks based on the selected project.
     */
    async setProjectRelated() {
        var [projects, currentProject] = await this.rpc("/attendance_project/projects");
        this.state.projects = projects;
        this.state.currentProject = currentProject;
        this.setTaskRelated();
    },

    /**
     * Fetches tasks related to the current project and sets the current task.
     * If no project is selected, clears tasks and current task.
     */
    async setTaskRelated() {
        if (this.state.currentProject) {
            var [tasks, currentTask] = await this.rpc("/attendance_project/tasks", {
                project_id: this.state.currentProject
            });
            this.state.tasks = tasks;
            this.state.currentTask = currentTask;
        } else {
            this.state.tasks = [];
            this.state.currentTask = false;
        }
    },

    /**
     * Fetches and sets the description for the current employee.
     */
    async setDescription() {
        this.state.description = await this.rpc("/attendance_project/description");
    },

    /**
     * Handles the change event for project selection.
     * Updates the current project and refreshes the tasks list.
     * 
     * @param {Event} ev - The event object from the change event.
     */
    onProjectChange(ev) {
        this.state.currentProject = ev.target.value;
        this.setTaskRelated();
    },

    /**
     * Handles the change event for task selection.
     * Updates the current task.
     * 
     * @param {Event} ev - The event object from the change event.
     */
    onTaskChange(ev) {
        this.state.currentTask = ev.target.value;
    },

    /**
     * Signs in or out the employee, updating project, task, and description if they are filled.
     * Alerts if any required fields are missing.
     */
    async signInOut() {
        if (!this.state.currentProject || !this.state.currentTask || !this.state.description) {
            alert("Project, Task, and Description must be filled.");
            return;
        }
        await this.rpc("/attendance_project/set_employee_value", {
            project_id: !this.state.checkedIn && this.state.currentProject || false,
            task_id: !this.state.checkedIn && this.state.currentTask || false,
            description: !this.state.checkedIn && this.state.description || '',
        });
        this.setProjectRelated();
        this.setDescription();
        super.signInOut();
    },
});
