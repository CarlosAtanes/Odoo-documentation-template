# __manifest__.py
{
    'name': 'Test Addon',
    'summary': 'Este es un módulo de prueba para aprender a crear módulos en Odoo.',
    'description': """
        Este módulo es un ejemplo de cómo estructurar y crear un módulo en Odoo.
        Incluye los archivos básicos necesarios y la configuración inicial.
    """,
    'author': 'Carlos',
    'version': '1.0',
    'category': 'Uncategorized',
    'depends': ['base'],
    'data': [
        # 'views/test_addon_view.xml',
        # 'security/ir.model.access.csv',
    ],    
    'installable': True,
    'auto_install': False,
    'application': True,
}
