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