# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields, models


class RecurringPlan(models.Model):
    _name = "espacio.tipo"
    _description = "Modelo para los tipos de espacios"
    nombre = fields.Char(string="Tipo", required=True)