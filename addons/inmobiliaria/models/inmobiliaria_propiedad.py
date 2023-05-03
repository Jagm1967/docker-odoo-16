from odoo import fields, models

class PropiedadModel(models.Model):
    _name = "inmobiliaria.propiedad"
    _description = "Modelo de propiedades"

 

    name = fields.Char(required=True, default="Desconocido")
    descripcion = fields.Char()
    codigo_postal = fields.Char()
    disponible = fields.Date(default=fields.Date.today().add(months=3))
    precio_esperado = fields.Float(required=True)
    precio_venta = fields.Float()
    dormitorios = fields.Integer()
    habitables_m =fields.Integer()
    fachadas = fields.Integer()
    garaje = fields.Boolean
    jardin_m = fields.Integer()
    jardin_orientacion = fields.Selection(
        string='Type',
        selection=[('norte', 'Norte'), ('sur', 'Sur'), ('este', 'Este'), ('oeste', 'Oeste')],
        help="Orientación del jardin")
    visto = fields.Datetime("Visti en", default=lambda self:fields.Datetiem.now())
    active = fields.Boolean (default=False)
    state = fields.Selection(
        string='Type',
        selection=[]
    )

