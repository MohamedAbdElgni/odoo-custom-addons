from odoo import fields, models
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    patient_id = fields.Many2one("hms.patient", string="Related Patient")

    def unlink(self):
        for rec in self:
            if rec.patient_id:
                raise UserError("Sorry, related patient's customer can't be deleted.")
        else:
            return super().unlink()

