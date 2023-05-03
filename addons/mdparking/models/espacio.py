# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields, models


class RecurringPlan(models.Model):
    _name = "espacio"
    _description = "Modelo para los espacios"
    nombre = fields.Char(string="Titulo", required=True)
    descripcion = fields.Text(string="Descripcion")
    precio = fields.Float("Precio")
    estado = fields.Selection((0, 'Disponible'), (1, 'Alquilado'), (2, 'Reservado'), (3, 'Mantenimiento'), (4, 'No disponible'))
    tipo = fields.Many2one("tipo_espacio", string="Tipo", ondelete="set null")
    ubicacion = fields.Many2one("ubicacion", string="Ubicacion", ondelete="set null")
    foto = fields.Binary(string="Foto")

    