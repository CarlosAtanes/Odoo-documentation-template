# __init__.py

# Este archivo se utiliza para inicializar el módulo de Odoo.
# Aquí puedes importar otros submódulos y paquetes que forman parte de tu módulo principal.

# Importa el submódulo `models` donde se definirán los modelos de datos
from . import models

# Puedes importar datos iniciales que deseas cargar al instalar el módulo, como datos predefinidos
from . import controllers
from . import views
from . import data
from . import security

# # Ejemplo de una función de inicialización que se ejecutará al instalar el módulo
# def _initialize_module(cr, registry):
#     """
#     Función de inicialización que se ejecuta al instalar el módulo.
#     Aquí puedes agregar lógica para preparar datos iniciales o configurar el entorno.
#     """
#     # Ejemplo de ejecución de una consulta SQL inicial para configurar algo en la base de datos
#     cr.execute("""
#         INSERT INTO res_partner (name, company_type)
#         VALUES ('Initial Partner', 'company')
#     """)

# # Si necesitas que una función se ejecute al instalar o actualizar el módulo, puedes definirla así:
# from odoo import api, SUPERUSER_ID

# def post_init_hook(cr, registry):
#     """
#     Esta función se ejecutará después de que el módulo se haya instalado.
#     """
#     # Puedes agregar lógica personalizada para configurar algo después de la instalación
#     env = api.Environment(cr, SUPERUSER_ID, {})
#     # Ejemplo: Crear un registro inicial
#     env['res.partner'].create({
#         'name': 'Post Install Partner',
#         'company_type': 'company',
#     })

# def uninstall_hook(cr, registry):
#     """
#     Esta función se ejecutará antes de que el módulo sea desinstalado.
#     """
#     # Puedes agregar lógica para limpiar datos o realizar tareas de limpieza
#     cr.execute("DELETE FROM res_partner WHERE name = 'Initial Partner'")

# # Registrar los hooks de instalación y desinstalación
# from odoo import modules

# modules.module.post_load.append(_initialize_module)
# modules.module.pre_uninstall.append(uninstall_hook)
