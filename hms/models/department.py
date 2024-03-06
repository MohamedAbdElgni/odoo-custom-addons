from odoo import models, fields


class Department(models.Model):
    _name = 'hms.department'
    _description = 'Hospital Department'
    _rec_name = 'name'
    name = fields.Char()
    capacity = fields.Integer()
    is_opened = fields.Boolean()
    patient_ids = fields.One2many("hms.patient", "department_id")

