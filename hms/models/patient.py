from odoo import models, fields, api
from odoo.exceptions import ValidationError


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
    pcr = fields.Boolean(default=False)
    image = fields.Binary()
    address = fields.Text()
    age = fields.Integer(default=False, required=True)
    history = fields.Html()
    states = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('fair', 'Fair'),
        ('good', 'Good'),
        ('serious', 'Serious'),
    ], default='undetermined')
    department_id = fields.Many2one("hms.department", default=False)
    department_capacity = fields.Integer(related="department_id.capacity")
    doctor_id = fields.Many2one("hms.doctor", readonly=True)
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

    @api.onchange('age')
    def _onchange_age(self):
        for rec in self:
            if rec.age < 30:
                rec.pcr = True
            else:
                rec.pcr = False

    @api.constrains('pcr', 'cr_ratio')
    def _check_pcr(self):
        for rec in self:
            if rec.pcr and not rec.cr_ratio:
                raise ValidationError("CR ratio is mandatory if PCR is checked")

    @api.constrains('age')
    def _check_age(self):
        for rec in self:
            if rec.age < 1:
                raise ValidationError("Age must be a positive number")
