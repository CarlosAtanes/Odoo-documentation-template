# test_addon_wizard.py
from odoo import models, fields, api

class TestAddonWizard(models.TransientModel):
    """
    Esta clase representa un asistente de prueba en Odoo.
    Hereda de models.TransientModel y se usa para crear un asistente personalizado.
    """

    _name = 'test.addon.wizard'
    _description = 'Asistente de Prueba de Addon'

    name = fields.Char('Name')
    description = fields.Text('Description')

    @api.multi
    def action_confirm(self):
        """
        Este método se llama cuando se hace clic en el botón de confirmación en el asistente.
        Imprime un mensaje y cierra el asistente.

        Returns:
            dict: Un diccionario que representa una acción para cerrar el asistente.
        """
        print("Asistente confirmado")
        return {'type': 'ir.actions.act_window_close'}
