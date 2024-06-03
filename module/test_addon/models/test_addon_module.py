# test_addon_module.py
from odoo import api, fields, models

class TestAddon(models.Model):

    _name = 'test.addon' # Nombre de la clase
    _description = 'Test Addon' # Descripción de la clase

    name = fields.Char(string='Name', required=True) # Field de odoo

    @api.model
    def get_name(self):
        return self.name # Retorna el nombre de la clase
    
