# Módulo template Odoo - por [@xXcarlos117Xx2](https://github.com/xXcarlos117Xx2)
## Introducción

El objetivo de este template es tener un documento en Español para ayudarnos a realizar los modulos en Odoo de una manera rápida, o al menos tener una referencia donde mirar que hace cada archivo, para que sirve, como se comporta, que es posible con ese módulo.

Este módulo esta orientado a desarolladores Junior que desean empezar en Odoo pero no tienen ni idea de por donde empezar. Recomiendo echarle una lectura al menos a la [documentacion oficial](https://www.odoo.com/documentation/master/) primero y/o ver [algun video en youtube sobre cursos de programación en Odoo](https://www.youtube.com/playlist?list=PLXwzJRuH--eYHB3OD2wATjzJ83UAp2WQs) para empezar a entender primero que es Odoo y las bases de este.

En concreto este tutorial/template tiene ejemplos y texto extraido de [esta lista de reproducción](https://www.youtube.com/playlist?list=PLXwzJRuH--eYHB3OD2wATjzJ83UAp2WQs) del creador de contenido [Josuhe Uh](https://www.youtube.com/@jos.uh.e)

## Estructura de un módulo en Odoo

```bash
test_addon/
├── __init__.py # Archivo para inicializar el módulo y los submódulos.
├── __manifest__.py # Archivo de configuración del módulo como nombre, versión, dependencias, etc.
│
├── controllers/ # Carpeta que contiene los controladores Python para manejar las rutas HTTP.
│   ├── __init__.py
│   └── main.py
│
├── data/ # Carpeta para archivos de datos, como datos iniciales o de configuración.
│   ├── data_file.xml
│   └── demo_data.xml
│
├── demo/ # Carpeta para datos de demostración que se cargan en la base de datos de demostración.
│   └── demo.xml
│
├── models/ # Carpeta que contiene los modelos de datos definidos en Python.
│   ├── __init__.py
│   └── test_addon_model.py
│
├── security/ # Carpeta para archivos de seguridad, como reglas de acceso y permisos.
│   ├── ir.model.access.csv
│   └── security.xml
│
├── static/ # Carpeta para archivos estáticos, como imágenes, CSS y JavaScript.
│   ├── description/
│   │   └── icon.png #Icono del módulo.
│   └── src/
│       ├── css/
│       │   └── styles.css
│       ├── img/
│       │   └── image.png
│       └── js/
│           └── script.js
│
├── views/ # Carpeta para archivos de vistas definidos en XML.
│   ├── test_addon_view.xml
│   ├── test_addon_search_view.xml
│   ├── ...
│
└── wizards/ # Carpeta para asistentes (wizards) definidos en Python.
    ├── __init__.py
    └── test_addon_wizard.py
```

### Explicación de la estructura

- **`__init__.py`**: Archivo para inicializar el módulo y los submódulos.
- **`__manifest__.py`**: Archivo de configuración del módulo, contiene metadatos como nombre, versión, dependencias, etc.
- **`controllers/`**: Carpeta que contiene los controladores Python para manejar las rutas HTTP.
  - `__init__.py`: Inicializa el submódulo de controladores.
  - `main.py`: Archivo de controladores donde defines las rutas y lógica del backend.
- **`data/`**: Carpeta para archivos de datos, como datos iniciales o de configuración.
  - `data_file.xml`: Archivo de datos.
  - `demo_data.xml`: Archivo de datos de demostración.
- **`demo/`**: Carpeta para datos de demostración que se cargan en la base de datos de demostración.
  - `demo.xml`: Archivo de datos de demostración.
- **`models/`**: Carpeta que contiene los modelos de datos definidos en Python.
  - `__init__.py`: Inicializa el submódulo de modelos.
  - `test_addon_model.py`: Archivo donde defines los modelos de datos.
- **`security/`**: Carpeta para archivos de seguridad, como reglas de acceso y permisos.
  - `ir.model.access.csv`: Archivo CSV que define los permisos de acceso a los modelos.
  - `security.xml`: Archivo XML para definir reglas de seguridad.
- **`static/`**: Carpeta para archivos estáticos, como imágenes, CSS y JavaScript.
  - `description/`: Carpeta para archivos de descripción, como el icono del módulo.
    - `icon.png`: Icono del módulo.
  - `src/`: Carpeta para recursos fuente.
    - `css/`: Carpeta para archivos CSS.
      - `styles.css`: Archivo CSS.
    - `img/`: Carpeta para imágenes.
      - `image.png`: Imagen de ejemplo.
    - `js/`: Carpeta para archivos JavaScript.
      - `script.js`: Archivo JavaScript.
- **`views/`**: Carpeta para archivos de vistas definidos en XML.
  - `test_addon_view.xml`: Vista de formulario y lista.
  - `test_addon_search_view.xml`: Vista de búsqueda.<br>
  - ...
- **`wizards/`**: Carpeta para asistentes (wizards) definidos en Python.
  - `__init__.py`: Inicializa el submódulo de asistentes.
  - `test_addon_wizard.py`: Archivo donde defines los asistentes.

## Consideraciones al crear archivos XML en Odoo
- El nombre del archivo debe ser en **minúscula**. Por ejemplo: `purchase_order_views.xml`
- El nombre del archivo debe iniciar con el nombre del modelo, sustituir los puntos del nombre del modelo con guiones bajos `_`.
- El nombre del archivo debe terminar con `_views`.
- Un modelo puede tener varias vistas, que son diferentes maneras de mostrar los datos
- En un mismo archivo pueden existir varias vistas
- Odoo **no va a marcar error** al tener vistas de modelos diferentes en el mismo XML, sin embargo se recomienda tener vistas del mismo modelo en un único XML 
- Sobre el mismo XML se deberia declarar todas las vistas, acciones y menús relacionados al mismo modelo.
- Se deberia declarar en el siguiente orden:
  - Vistas
  - Acciopnes de venta
  - Acciones del servidor
  - Menús

### Ejemplo
<img src="xml_example.png" style="width: 45vw;max-width:450px;" />

## Herencias en Odoo
El código base de Odoo **nunca** debería de modificarse.

En lugar de sobreescribir las vistas o modelos existentes para agregar eliminar o modificar funcionalidades existentes, deberemos de usar **herencias**. Estas modificaciones pueden ser a nivel de modelo, vista o lógica de negocio.<br>
En el archivo `__manifest__.py` en la sección `depends` se deberá indicar los módulos o aplicaciones que se heredan.<br>
En **la clase** del archivo que queramos hacer que herede, sustituimos la palabra reservada `_name` por `_inhert` doonde pondremos el nombre del modelo ya existente.

### Cosas que podemos lograr heredando **de un modelo existente**:
- Agregar campos nuevos
- Anular la definición de campos
- Agregar restricciones o funcionalidades adicionales
- Agregar métodos y funcionalidades nuevas
- Anular médotos o procesos

