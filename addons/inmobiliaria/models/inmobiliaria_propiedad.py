from odoo import fields, models

class PropiedadModel(models.Model):
    _name = "inmobiliaria.propiedad"
    _description = "Modelo de propiedades"

 

    name = fields.Char('Nombre',required=True, default="Desconocido")
    descripcion = fields.Char()
    codigo_postal = fields.Char('Código postal', size=5)
    disponible = fields.Date('Disponible desde',default=fields.Date.today().add(months=3))
    precio_esperado = fields.Float('Precio esperado',required=True)
    precio_venta = fields.Float('Precio de venta')
    dormitorios = fields.Integer('Dormitorios')
    habitables_m =fields.Integer('Metros habitables')
    fachadas = fields.Integer('Fachadas')
    garaje = fields.Boolean('Garaje')
    jardin_m = fields.Integer('Metros de jardin')
    jardin_orientacion = fields.Selection('Orientación del jardin',
        string='Type',
        selection=[('norte', 'Norte'), ('sur', 'Sur'), ('este', 'Este'), ('oeste', 'Oeste')],
        help="Orientación del jardin")
    visto = fields.Datetime("Visto el", default=lambda self:fields.Datetiem.now())
    active = fields.Boolean (default=False)
    state = fields.Selection('Estado',
        string='Type',
        selection=[('nuevo', 'Nuevo'), ('recibida', 'Oferta recibida'), ('aceptada', 'Oferta aceptada'), ('vendido', 'Vendido'), ('cancelado', 'Cancelado')],
    )

