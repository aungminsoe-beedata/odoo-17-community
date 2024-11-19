from odoo import api,fields,models

class State(models.Model):
    _name = "state"
    name = fields.Char(string="State/Region Name")


