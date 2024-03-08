from odoo import models, fields, api


class Department(models.Model):
    _name = 'hms.department'
    _description = 'Hospital Department'
    _rec_name = 'name'

    name = fields.Char(required=True)
    capacity = fields.Integer(required=True)
    is_opened = fields.Boolean()
    patient_ids = fields.One2many("hms.patient", "department_id")

    available_capacity = fields.Integer(compute='_compute_available_capacity', store=True)

    @api.depends('capacity', 'patient_ids')
    def _compute_available_capacity(self):
        for department in self:
            assigned_patients = len(department.patient_ids)
            department.available_capacity = department.capacity - assigned_patients
            print("="*50)
            print(department.available_capacity)
