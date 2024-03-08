from odoo import models, fields, api


class Log(models.Model):
    _name = 'hms.log'
    _description = 'Log Record'
    _rec_name = 'date'
    _order = 'id desc'

    patient_id = fields.Many2one("hms.patient", required=True, readonly=True, ondelete="cascade")
    date = fields.Date(default=fields.Date.today, readonly=True)
    description = fields.Text(required=True)
    created_by = fields.Many2one("res.users")

    @api.model
    def create(self, vals):
        vals["created_by"] = self.env.user.id
        return super(Log, self).create(vals)
