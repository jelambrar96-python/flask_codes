# Construyendo un "Hello, World!" en Flask.

Flask es un microframework muy accesible para crear aplicaciones web en Python. A continuación, te guiaré paso a paso para construir y ejecutar un sencillo "Hello, World!" utilizando Flask.

Este es el primer paso para construir aplicaciones web más complejas con Flask. 

### Pasos:

#### Paso 1: Crear la aplicación Flask

1. **Crear un archivo Python**:
   Crea un archivo llamado `app.py` en tu directorio de proyecto.

2. **Escribir el código de la aplicación**:
   Abre `app.py` con tu editor de texto favorito y escribe el siguiente código:
   ```python
   from flask import Flask

   app = Flask(__name__)

   @app.route('/')
   def home():
       return "Hello, World!"

   if __name__ == '__main__':
       app.run(debug=True)
   ```

   - **Importar Flask**: La primera línea importa la clase Flask desde el paquete `flask`.
   - **Crear la aplicación**: La instancia `app` es nuestra aplicación Flask.
   - **Definir una ruta y una función**: El decorador `@app.route('/')` define la ruta de la URL raíz ('/'). Por medio de los decoradores se enlazan las rutas con las funciones que contienen las subrutinas donde ocurre la lógica de la aplicación. Para este caso, la función `home` retorna el texto "Hello, World!" cuando se accede a la ruta raíz. Adicionalmente, las funciones deben devolver la respuesta que será mostrada en el navegador. 
   - **Ejecutar la aplicación**: `app.run(debug=True)` ejecuta la aplicación en modo de depuración.

Para acceder a una versión mejor documentada del archivo `app.py` accede [aquí](app/app.py).

#### Paso 2: Ejecutar la aplicación Flask

1. **Ejecutar el script**:
   En tu terminal, asegúrate de estar en el directorio donde se encuentra `app.py` y ejecuta:
   ```bash
   python app.py
   ```

2. **Acceder a la aplicación**:
   Una vez que la aplicación esté en ejecución, debería mostrarse un mensaje indicando que el servidor está corriendo en `http://127.0.0.1:5000/`. Abre tu navegador web y visita esta URL.

   Deberías ver la frase "Hello, World!" en tu navegador.

### Notas Adicionales

- **Modo de Depuración**: El modo de depuración (`debug=True`) es muy útil durante el desarrollo, ya que proporciona mensajes de error detallados y reinicia automáticamente el servidor cuando se realizan cambios en el código. No se recomienda usar el modo debug en entornos de producción.
- **Decoradores**: Los decoradores (`@app.route`) son una forma de vincular URLs con funciones en Flask, facilitando la creación de rutas y vistas.



### Resumen

Crear y ejecutar un "Hello, World!" en Flask implica los siguientes pasos:
1. Preparar el entorno instalando Python y Flask.
2. Escribir el código básico de la aplicación en `app.py`.
3. Ejecutar el script y acceder a la aplicación a través del navegador.

____

### Material Complementario

- **Geeksforgeeks: Flask Tutorial** 
  - Flask Tutorial: [Click aquí](https://www.geeksforgeeks.org/flask-tutorial/)
  - Flask - (Creating first simple application): [Click aquí](https://www.geeksforgeeks.org/flask-creating-first-simple-application/?ref=lbp)

- **j2logo.com: Tutorial Flask en español**
  -  Tutorial Flask – Lección 1: La primera aplicación Flask [Click aquí](https://j2logo.com/leccion-1-la-primera-aplicacion-flask/) 

- **miguelgringerg.com: Flask Mega-Tutorial, Part I: Hello World**
  - [Click aqui](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
  
- **riptutorial.com: Learning Flask Chapter 1**
  - [Click aquí](https://riptutorial.com/Download/flask.pdf)

______

Made with Love ❤️ by [@jelambrar96](https://github.com/jelambrar96)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/jelambrar1)

