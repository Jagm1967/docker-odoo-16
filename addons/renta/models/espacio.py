# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields, models


class RecurringPlan(models.Model):
    _name = "espacio"
    _description = "Modelo para los espacios"
    nombre = fields.Char(string="Titulo", required=True)
    descripcion = fields.Text(string="Descripcion")
    precio = fields.Float("Precio")
    state = fields.Selection(string="Estado", selection=[('disponible', 'Disponible'), ('alquilado', 'Alquilado'), ('reservado', 'Reservado'), ('mantenimiento', 'Mantenimiento'), ('no_disponible', 'No disponible')], default='disponible')
    active = fields.Boolean(string="Activo", default=True)
    tipo = fields.Many2one("tipo_espacio", string="Tipo", ondelete="set null")
    ubicacion = fields.Many2one("ubicacion", string="Ubicacion", ondelete="set null")
    foto = fields.Binary(string="Foto")

    