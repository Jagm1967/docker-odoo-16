# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class RecurringPlan(models.Model):
    _name = "estate.property.type"
    _description = "Modelo tipo de propiedades"
    name = fields.Char(string="Tipo", required=True)