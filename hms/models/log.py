from odoo import models, fields


class Log(models.Model):
    _name = 'hms.log'
    _description = 'Log Record'
    _rec_name = 'date'

    patient_id = fields.Many2one("hms.patient", required=True, readonly=True)
    date = fields.Date(default=fields.Date.today, readonly=True)
    description = fields.Text(required=True)
    created_by = fields.Many2one("res.users", default=lambda self: self.env.user, readonly=True)
