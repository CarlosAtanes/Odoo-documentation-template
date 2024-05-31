import requests
from requests_aws4auth import AWS4Auth
from odoo import models, fields, api

class AmazonConnector(models.Model):
    _name = 'amazon.connector'
    _description = 'Amazon Connector'

    name = fields.Char(string='Name', required=True)
    amazon_api_key = fields.Char(string='Amazon API Key', required=True)
    amazon_secret_key = fields.Char(string='Amazon Secret Key', required=True)
    amazon_associate_tag = fields.Char(string='Amazon Associate Tag', required=True)
    amazon_marketplace = fields.Selection([
        ('na', 'North America'),
        ('eu', 'Europe'),
        ('fe', 'Far East')
    ], string='Amazon Marketplace', default='na', required=True)
    amazon_access_token = fields.Char(string='Amazon Access Token', required=True)

    @api.model
    def fetch_amazon_product(self, asin):
        """
        Obtiene detalles del producto de Amazon utilizando el ASIN proporcionado.

        Parámetros:
        asin (str): El Número de Identificación Estándar de Amazon (ASIN) del producto.

        Retorna:
        dict: Un diccionario que contiene los detalles del producto si la operación es exitosa, o un mensaje de error si ocurre un error.
        """
        marketplace_urls = {
            'na': 'https://sellingpartnerapi-na.amazon.com',
            'eu': 'https://sellingpartnerapi-eu.amazon.com',
            'fe': 'https://sellingpartnerapi-fe.amazon.com'
        }

        base_url = marketplace_urls.get(self.amazon_marketplace, 'https://sellingpartnerapi-na.amazon.com')
        url = '{}/products/v0/items/{}'.format(base_url, asin)

        awsauth = AWS4Auth(self.amazon_api_key, self.amazon_secret_key, 'eu-west-1', 'execute-api')

        headers = {
            'x-amz-access-token': self.amazon_access_token,
            'Content-Type': 'application/json'
        }

        try:
            response = requests.get(url, headers=headers, auth=awsauth)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return {'error': 'HTTP error occurred: {}'.format(http_err)}
        except Exception as err:
            return {'error': 'Other error occurred: {}'.format(err)}