# library_management/__manifest__.py
# -*- coding: utf-8 -*-

{
    'name': 'Library Management',
    'version': '1.0',
    'description': "Test module to learn about Odoo",
    'author': "Carlos Atanes Vences",
    'category': 'Library',
    'website': 'https://www.campigroup.es',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/book_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
