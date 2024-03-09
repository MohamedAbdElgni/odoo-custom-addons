from dateutil.relativedelta import relativedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Patient(models.Model):
    _name = 'hms.patient'
    _description = 'Patient Record'
    _rec_name = 'first_name'
    _sql_constraints = [
        ('email_unique', 'unique(email)', 'This email is already exist!'),
    ]
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    birth_date = fields.Date(required=True)
    email = fields.Char(required=True)
    cr_ratio = fields.Float()
    blood_type = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('O', 'O'),
    ])
    pcr = fields.Boolean(default=False)
    image = fields.Binary()
    address = fields.Text()
    age = fields.Integer(compute="_compute_age", readonly=True)
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

    def action_add_log(self):
        """Link to wizard to add log to patient from patient form"""
        action = self.env['ir.actions.actions']._for_xml_id('hms.action_add_log_wizard') # noqa
        action['context'] = {
            'default_patient_id': self.id, # noqa
        }
        return action

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

    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            if rec.birth_date:
                rec.age = relativedelta(fields.Date.today(), rec.birth_date).years
            else:
                rec.age = 0

    @api.constrains('email')
    def _check_email(self):
        for rec in self:
            if rec.email:
                if "@" not in rec.email and "." not in rec.email:
                    raise ValidationError("Invalid email")
