# main.py
from odoo import http

class TestAddon(http.Controller):
    """
    Esta clase representa un addon de prueba para Odoo.
    Contiene un método para manejar solicitudes HTTP con fines de prueba.
    """

    @http.route('/test/addon', auth='public', methods=['GET'], type='http')
    def test_addon(self, **kw):
        """
        Este método maneja solicitudes HTTP GET a la ruta '/test/addon'.
        Devuelve un simple mensaje de hola mundo.

        Parámetros:
        - **kw** (dict): Argumentos de palabra clave pasados a la ruta.

        Returns:
        - str: Un mensaje de hola mundo.
        """
        return "¡Hola mundo!"
