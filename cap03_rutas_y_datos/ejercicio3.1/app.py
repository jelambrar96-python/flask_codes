"""
### Ejercicio: Desarrollar una Aplicación Flask 
con Manejo de Datos de la Solicitud y Rutas

El objetivo de este ejercicio es crear una aplicación Flask 
que demuestre cómo manejar diferentes tipos de datos de la 
solicitud y cómo gestionar rutas. 

La aplicación tendrá las siguientes características:

1. **Página Principal**: Muestra enlaces a otras rutas.
2. **Búsqueda de Usuario**: Usa parámetros de la URL 
    para buscar un usuario.
3. **Formulario de Ingreso**: Maneja datos del formulario 
    para autenticar un usuario.
4. **API JSON**: Recibe y procesa datos JSON.
5. **Subida de Archivos**: Permite subir archivos y los 
    guarda en el servidor.


PASO 1: crea una estructura con plantillas para index, busqueda,
inicio_sesion y cargar


PASO 2: crea las plantillas html, 
- la plantilla index debe tener enlaces
- la plantilla busqueda debe tener un campo donde se 
    pueda ingresar el usuario
- la plantilla login debe tener un formulario con usuario y contraseña
- la plantilla upload debe tener un formulario con un campo para subir archivos

PASO 3. En el archivo app.py agrega las rutas
1. **Página Principal** (`/`):
   - Muestra enlaces a otras rutas.
   - Utiliza la plantilla `index.html`.

2. **Búsqueda de Usuario** (`/search`):
   - Accede a los parámetros de la URL utilizando `request.args`.
   - Muestra el resultado de la búsqueda utilizando la plantilla `search.html`.

3. **Formulario de Ingreso** (`/login`):
   - Maneja datos del formulario utilizando `request.form`.
   - Si se accede mediante GET, muestra el formulario de ingreso utilizando 
     la plantilla `login.html`.
   - Si se accede mediante POST, procesa los datos del formulario.

4. **API JSON** (`/api/data`):
   - Accede a los datos JSON enviados en la solicitud utilizando `request.json`.
   - Retorna los datos JSON como respuesta utilizando `jsonify`.

5. **Subida de Archivos** (`/upload`):
   - Maneja archivos subidos utilizando `request.files`.
   - Si se accede mediante GET, muestra el formulario de subida utilizando 
     la plantilla `upload.html`.
   - Si se accede mediante POST, guarda el archivo subido en el servidor.

PASO 4. Ejecuta tu aplicación

    
"""
