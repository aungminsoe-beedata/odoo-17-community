from odoo import models, fields

    
class SchoolClassName(models.Model):
    _name = 'school.classname'
    _description = 'Class Name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Class Name", required=True,track_visibility = "always")
    class_teacher_name = fields.Many2one('hr.employee', string="Class Teacher", required=True,track_visibility = "always")
