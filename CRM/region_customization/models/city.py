
from odoo import models, fields, api, _
class City(models.Model):
    _name = "city"
    name = fields.Char(string="Name")
    # salary_deduction=fields.Integer(string='Salary Deduction')
    # region_id= fields.One2many('region',string='Region')


