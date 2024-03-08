from odoo import fields, models, api


class AddLogWizard(models.TransientModel):
    _name = 'add.log.wizard'
    _description = 'Add Log Wizard'

    description = fields.Text(required=True)
    patient_id = fields.Many2one("hms.patient", readonly=True)

    def action_add_log(self): # noqa
        """Add log to patient from wizard"""
        self.patient_id.log.create({
            "patient_id": self.patient_id.id,
            "description": self.description,
        })

