from odoo import api, fields, models

class TestModel(models.Model):
    _name = "test.model"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Test Model"

    name = fields.Char(string='Name', tracking=True)
    date = fields.Date(string='Date', tracking=True)
    desc = fields.Char(string='Description', tracking=True)
    active = fields.Boolean(default=True, string='Active')

    priority = fields.Selection([
        ('0', 'Very Low'),
        ('1', 'Low'),
        ('2', 'Normal'),
        ('3', 'High')], string="Priority")

