# Retornando Código HTML desde una Aplicación Flask

En Flask, puedes retornar HTML de dos maneras principales:
1. Directamente desde el código Python utilizando cadenas de texto.
2. Utilizando plantillas HTML externas para separar la lógica de la presentación.

#### 1. Código HTML Embebido en Python

En este método, se retorna el HTML directamente desde la función de vista en el código Python. Aunque es útil para aplicaciones simples o pruebas rápidas, no es recomendable para aplicaciones más grandes debido a problemas de mantenimiento y legibilidad.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Retorna una cadena de texto que contiene el código HTML
    return """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>Hello, Flask!</title>
      </head>
      <body>
        <h1>Welcome to Flask!</h1>
        <p>This is a simple HTML page returned directly from a Flask route.</p>
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
```

#### 2. Utilizando Plantillas HTML Externas

Para proyectos más grandes, es mejor utilizar plantillas HTML externas con el motor de plantillas Jinja2, que viene integrado con Flask. Esto permite separar la lógica de la aplicación y la presentación de las páginas web.

##### Paso a Paso:

1. **Estructura del Proyecto**:
   Crea una estructura de proyecto como esta:
   ```
   my_flask_app/
   ├── app.py
   └── templates/
       └── home.html
   ```

2. **Crear la Plantilla HTML**:
   Dentro del directorio `templates`, crea un archivo llamado `home.html` con el siguiente contenido:
   ```html
   <!doctype html>
   <html lang="en">
     <head>
       <meta charset="utf-8">
       <title>Hello, Flask!</title>
     </head>
     <body>
       <h1>Welcome to Flask!</h1>
       <p>This is a simple HTML page rendered from a template.</p>
     </body>
   </html>
   ```

3. **Modificar el Código de Flask para Usar la Plantilla**:
   Actualiza `app.py` para renderizar la plantilla HTML usando `render_template`:
   ```python
   from flask import Flask, render_template

   app = Flask(__name__)

   @app.route('/')
   def home():
       # Renderiza la plantilla 'home.html' y la retorna como respuesta
       return render_template('home.html')

   if __name__ == '__main__':
       app.run(debug=True)
   ```

4. **Ejecutar la Aplicación**:
   Ejecuta tu aplicación de Flask:
   ```bash
   python app.py
   ```
   Luego, abre tu navegador web y visita `http://127.0.0.1:5000/` para ver la página HTML renderizada desde la plantilla.

### Resumen

- **HTML Embebido en Python**: Útil para aplicaciones pequeñas o pruebas rápidas, pero no recomendable para aplicaciones más grandes debido a la falta de separación entre la lógica y la presentación.
- **Plantillas HTML Externas**: Utiliza Jinja2 para mantener la lógica y la presentación separadas, lo que mejora la mantenibilidad y la legibilidad del código.
______

### Material Recomendado

- **miguelgringerg.com: Flask Mega-Tutorial, Part II: Templates**
  - [Click aqui](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates)

- **riptutorial.com: Learning Flask Chapter 2, 14, 15, 16**
  - [Click aquí](https://riptutorial.com/Download/flask.pdf)

______

Made with Love ❤️ by [@jelambrar96](https://github.com/jelambrar96)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/jelambrar1)

