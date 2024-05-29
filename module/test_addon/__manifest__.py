# __manifest__.py

{
    # El nombre del módulo que se mostrará en la interfaz de usuario de Odoo
    'name': 'Test Addon',
    
    # Una breve descripción del propósito del módulo
    'summary': 'Este es un módulo de prueba para aprender a crear módulos en Odoo.',
    
    # Una descripción más detallada del módulo
    'description': """
        Este módulo es un ejemplo de cómo estructurar y crear un módulo en Odoo.
        Incluye los archivos básicos necesarios y la configuración inicial.
    """,
    
    # El autor del módulo
    'author': 'Carlos',
    
    # La versión del módulo
    'version': '1.0',
    
    # La categoría del módulo en el App Store de Odoo
    'category': 'Uncategorized',
    
    # Las dependencias del módulo, es decir, otros módulos que deben estar instalados para que este funcione
    'depends': ['base'],
    
    # Las localizaciones de los datos del módulo, como archivos XML, CSV, etc.
    'data': [
        # Aquí se pueden incluir vistas, reglas de seguridad, datos iniciales, etc.
        # 'views/test_addon_view.xml',
        # 'security/ir.model.access.csv',
    ],
    
    # Los archivos de demostración que solo se cargan en la base de datos de demostración
    'demo': [
        # 'demo/demo_data.xml',
    ],
    
    # Indica si el módulo puede instalarse en varias empresas
    'installable': True,
    
    # Indica si el módulo se carga automáticamente cuando Odoo inicia
    'auto_install': False,
    
    # Indica si el módulo está en la lista de aplicaciones de Odoo
    'application': True,
}
