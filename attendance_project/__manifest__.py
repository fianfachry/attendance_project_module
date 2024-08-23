# -*- coding: utf-8 -*-

{
    'name': 'Attendance Project',
    'author': 'Fian',
    'version': '0.0.1',
    'category': 'HR',
    'summary': 'Enhance the existing Attendance module in Odoo',
    'depends': [
        'hr_attendance',
        'project',
    ],
    'data': [
        'views/attendance_view.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'attendance_project/static/src/components/**/*'
        ]
    },
    'installable': True
}
