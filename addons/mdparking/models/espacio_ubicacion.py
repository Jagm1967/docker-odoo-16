# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields, models


class RecurringPlan(models.Model):
    _name = "espacio.ubicacion"
    _description = "Modelo para las ubicaciones de espacios"
    nombre = fields.Char(string="Tipo", required=True)
    direccion = fields.Char(string="Direccion", required=True)
    codigo_postal = fields.Char(string="Codigo postal", required=True)