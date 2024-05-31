{
    'name': 'Amazon Connector Cesumin SL',
    'version': '0.1',
    'summary': 'Conector de Amazon para Odoo',
    'description': 'conector de Amazon para Odoo',
    'author': 'Cesumin SL',
    'website': 'https://www.cesumin.com',
    'category': 'dev_module',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/amz_con_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
