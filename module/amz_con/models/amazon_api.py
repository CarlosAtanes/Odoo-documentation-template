import requests
from odoo import models, fields

class AmazonApi(models.AbstractModel):
    _name = 'amazon.api'
    _description = 'Amazon API'

    def _get_amazon_data(self, endpoint, params = None):
        url = f'https://api.amazon.com/{endpoint}'
        headers = {
            'Authorization': 'Bearer ' + self._get_access_token(),
            'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    
    def _get_access_token(self):
        access_token = ''
        # Lógica para obtener el token de acceso
        return access_token
    
    def import_product(self):
        endpoint = 'products'
        products = self._get_amazon_data(endpoint)
        # Logica para procesar los productos desde Amazon y guardarlos en Odoo
        for product in products:
            self.env['amazon.product'].create({
                'name': product['name'],
                'amazon_id': product['id'],
                'description': product['description'],
                'price': product['price'],
                'stock': product['stock'],
                'image': product['image'],
                })
            