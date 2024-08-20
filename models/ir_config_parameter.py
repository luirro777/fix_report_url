from odoo import models, fields

class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    def init(self):
        super(IrConfigParameter, self).init()

        # Crear los parámetros 'report.url' y 'report.url.freeze' con valores predeterminados
        self.set_param('report.url', 'http://localhost:8069', groups=["base.group_system"])
        self.set_param('report.url.freeze', 'True', groups=["base.group_system"])
