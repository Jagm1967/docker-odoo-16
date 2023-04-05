# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields, models


class RecurringPlan(models.Model):
    _name = "estate.property"
    _description = "Modelo para las propiedades"
    name = fields.Char(string="Titulo", required=True)
    description = fields.Text()
    postcode = fields.Char("Codigo postal")
    date_availability = fields.Date("Disponible",default=fields.Date.today)
    expected_price = fields.Float("Precio",required=True)
    selling_price = fields.Float("Precio de venta")
    bedrooms = fields.Integer("Dormitorios", default=1)
    living_area = fields.Integer("Tamaño (m2)")
    facades = fields.Integer("Fachadas")
    garage = fields.Boolean("Garaje")
    garden = fields.Boolean("Jardin")
    garden_area = fields.Integer("Jardin tamaño (m2)")
    garden_orientation = fields.Selection(
        [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],)
    active = fields.Boolean(default=True)
    state = fields.Selection(
        [('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')],)
    last_seen = fields.Datetime("Ultima visita",default=lambda self:fields.Datetime.now())
    type_id = fields.Many2one("estate.property.type", string="Tipo", ondelete="set null")
    salesperson_id = fields.Many2one("res.users", string="Agente", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Comprador")
    tag_ids = fields.Many2many("estate.property.tag", string="Etiquetas")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Ofertas")
    total_area = fields.Integer("Tamaño total", compute="_compute_total_area", store=True)
    best_price = fields.Float("Mejor precio", compute="_compute_best_price", store=True)

    @api.depends('garden_area', 'living_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area
    
    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            best_price = 0
            for offer in record.offer_ids:
                if offer.price > best_price:
                    best_price = offer.price
            record.best_price = best_price