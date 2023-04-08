# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields, models


class RecurringPlan(models.Model):
    _name = "estate.property.offer"
    _description = "Modelo ofertas de propiedades"
    price = fields.Float("Precio", required=True)
    status = fields.Selection(
        [('accepted', 'Acceptada'), ('rejected', 'Rechazada'), ('canceled', 'Cancelada')],)
    partner_id = fields.Many2one("res.partner", string="Comprador")
    property_id = fields.Many2one("estate.property", string="Propiedad", ondelete="cascade")
    validity = fields.Integer("Validez (dias)")
    date_deadline = fields.Date("Fecha limite", compute="_compute_date_deadline", inverse="_inverse_date_deadline")

    @api.depends('validity','create_date')
    def _compute_date_deadline(self):
        for record in self:
            if record.validity and record.create_date:
                record.date_deadline = record.create_date + timedelta(days=record.validity)
            else:
                record.date_deadline = False
    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline:
                record.validity = (record.date_deadline - record.create_date).days
            else:
                record.validity = False

    def action_accept(self):
        self.status = 'accepted'
        self.property_id.state = 'offer_accepted'
        self.property_id.buyer_id = self.partner_id
        self.property_id.selling_price = self.price
        return True
    def action_reject(self):
        self.status = 'rejected'
        return True
