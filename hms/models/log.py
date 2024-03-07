from odoo import models, fields


class Log(models.Model):
    _name = 'hms.log'
    _description = 'Log Record'
    _rec_name = 'date'
    patient_id = fields.Many2one("hms.patient")
    date = fields.Datetime()
    description = fields.Text()

