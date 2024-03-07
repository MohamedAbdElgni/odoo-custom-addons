from odoo import models, fields


class Patient(models.Model):
    _name = 'hms.patient'
    _description = 'Patient Record'
    _rec_name = 'first_name'
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
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
    doctor_id = fields.Many2many("hms.doctor")
    log = fields.One2many("hms.log", "patient_id")

    def action_undetermined(self):
        for rec in self:
            rec.write({"states": "undetermined"})
            rec.log.create({
                "patient_id": rec.id,
                "description": "The patient's state has been changed to undetermined."
            })

    def action_good(self):
        for rec in self:
            rec.write({"states": "good"})
            rec.log.create({
                "patient_id": rec.id,
                "description": "The patient's state has been changed to good."
            })

    def action_fair(self):
        for rec in self:
            rec.write({"states": "fair"})
            rec.log.create({
                "patient_id": rec.id,
                "description": "The patient's state has been changed to fair."
            })

    def action_serious(self):
        for rec in self:
            rec.write({"states": "serious"})
            rec.log.create({
                "patient_id": rec.id,
                "description": "The patient's state has been changed to serious."
            })
