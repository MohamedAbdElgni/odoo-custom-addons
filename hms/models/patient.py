from odoo import models, fields


class Patient(models.Model):
    _name = 'hms.patient'
    _description = 'Patient Record'
    _rec_name = 'first_name'
    first_name = fields.Char()
    last_name = fields.Char()
    birth_date = fields.Date()
    cr_ratio = fields.Float()
    blood_type = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('O', 'O'),
    ])
    pcr = fields.Boolean()
    image = fields.Binary()
    address = fields.Text()
    age = fields.Integer()
    history = fields.Html()
    states = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ], default='undetermined')
    department_id = fields.Many2one("hms.department")
    department_capacity = fields.Integer(related="department_id.capacity")
    doctor_id = fields.Many2one("hms.doctor")
