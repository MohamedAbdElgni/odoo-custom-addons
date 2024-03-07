from odoo import models, fields


class Doctor(models.Model):
    _name = 'hms.doctor'
    _description = 'Doctor Record'
    _rec_name = 'first_name'
    first_name = fields.Char(reqired=True)
    last_name = fields.Char(required=True)
    image = fields.Binary()
    patient_id = fields.One2many("hms.patient", "doctor_id")
    department_id = fields.Many2one("hms.department")
