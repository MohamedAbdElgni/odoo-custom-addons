from odoo import models, fields, api
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    patient_id = fields.Many2one("hms.patient", string="Related Patient")

    def unlink(self):
        for rec in self:
            if rec.patient_id:
                raise UserError("Sorry, related patient's customer can't be deleted.")
        else:
            return super().unlink()

    @api.constrains('vat')
    def mandatory_vat(self):
        for rec in self:
            if not rec.vat:
                raise UserError("Sorry, VAT is mandatory.")

