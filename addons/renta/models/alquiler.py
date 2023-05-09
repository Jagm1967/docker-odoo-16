# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields, models


class RecurringPlan(models.Model):
    _name = "alquiler"
    _description = "Modelo para los alquileres"
    inicio = fields.Date(string="Fecha de inicio", required=True)
    fin = fields.Date(string="Fecha de fin")
    cliente = fields.Many2one("res.partner", string="Cliente", ondelete="set null")
    espacio = fields.Many2one("espacio", string="Espacio", ondelete="set null")