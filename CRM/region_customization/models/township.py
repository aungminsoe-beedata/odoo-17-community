from odoo import api, fields, models

class Township(models.Model):
    _name = "township"
    name = fields.Char('Township Name')
    state_id = fields.Many2one('state', 'State/Region', required=True)