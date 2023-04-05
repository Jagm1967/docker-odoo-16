# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class RecurringPlan(models.Model):
    _name = "estate.property.tag"
    _description = "Modelo etiquetas de propiedades"
    name = fields.Char(string="Tipo", required=True)