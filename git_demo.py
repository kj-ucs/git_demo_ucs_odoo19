from odoo import fields, models


class GitDemo(models.Model):
    _name = 'git.demo'
    _description = 'Git Demo'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
