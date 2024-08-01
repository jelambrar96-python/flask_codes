## Ejercicio 2.1

Construye una aplicacion sencilla en flask donde la raíz root tenga tres botones, uno rojo, uno amarillo y uno verde. Cada boton debe redirijir a las rutas "/rojo", "/amarillo" y "/verde" respectivamente, las cuales tienen páginas cuyo coolor de fonde es su respectivo color, en cada pagina de colores hay un boton "home" que nos devuelve a la ruta raíz.  

### Construyendo una Aplicación Flask con Botones de Redirección y Páginas de Colores

A continuación, te mostraré cómo construir una aplicación Flask que cumple con los requisitos especificados. La aplicación tendrá una página principal con tres botones que redirigen a páginas de colores, y cada página de colores tendrá un botón "Home" para volver a la página principal.

#### Paso 1: Estructura del Proyecto

Crea una estructura de proyecto como esta:
```
my_flask_app/
├── app.py
└── templates/
    ├── index.html
    ├── rojo.html
    ├── amarillo.html
    └── verde.html
```

#### Paso 2: Crear las Plantillas HTML

1. **index.html**:
   ```html
   <!doctype html>
   <html lang="en">
     <head>
       <meta charset="utf-8">
       <title>Home</title>
     </head>
     <body>
       <h1>Home</h1>
       <button onclick="location.href='/rojo'" style="background-color: red; color: white;">Rojo</button>
       <button onclick="location.href='/amarillo'" style="background-color: yellow; color: black;">Amarillo</button>
       <button onclick="location.href='/verde'" style="background-color: green; color: white;">Verde</button>
     </body>
   </html>
   ```

2. **rojo.html**:
   ```html
   <!doctype html>
   <html lang="en">
     <head>
       <meta charset="utf-8">
       <title>Rojo</title>
       <style>
         body {
           background-color: red;
           color: white;
         }
       </style>
     </head>
     <body>
       <h1>Rojo</h1>
       <button onclick="location.href='/'" style="background-color: white; color: black;">Home</button>
     </body>
   </html>
   ```

3. **amarillo.html**:
   ```html
   <!doctype html>
   <html lang="en">
     <head>
       <meta charset="utf-8">
       <title>Amarillo</title>
       <style>
         body {
           background-color: yellow;
           color: black;
         }
       </style>
     </head>
     <body>
       <h1>Amarillo</h1>
       <button onclick="location.href='/'" style="background-color: white; color: black;">Home</button>
     </body>
   </html>
   ```

4. **verde.html**:
   ```html
   <!doctype html>
   <html lang="en">
     <head>
       <meta charset="utf-8">
       <title>Verde</title>
       <style>
         body {
           background-color: green;
           color: white;
         }
       </style>
     </head>
     <body>
       <h1>Verde</h1>
       <button onclick="location.href='/'" style="background-color: white; color: black;">Home</button>
     </body>
   </html>
   ```

#### Paso 3: Crear el Archivo `app.py`

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rojo')
def rojo():
    return render_template('rojo.html')

@app.route('/amarillo')
def amarillo():
    return render_template('amarillo.html')

@app.route('/verde')
def verde():
    return render_template('verde.html')

if __name__ == '__main__':
    app.run(debug=True)
```

#### Paso 4: Ejecutar la Aplicación

1. Abre tu terminal.
2. Navega al directorio `my_flask_app`.
3. Ejecuta la aplicación:
   ```bash
   python app.py
   ```
4. Abre tu navegador web y visita `http://127.0.0.1:5000/`.



### Explicación

- **Plantillas HTML**: Cada plantilla define la estructura y el estilo de las páginas. Los botones están configurados para redirigir a las rutas especificadas.
- **Rutas en Flask**: `@app.route('/')`, `@app.route('/rojo')`, `@app.route('/amarillo')` y `@app.route('/verde')` definen las rutas que corresponden a cada página. Las funciones asociadas a estas rutas renderizan las plantillas HTML correspondientes.
- **Botones de Navegación**: Los botones en las plantillas utilizan `onclick="location.href='/ruta'"` para redirigir a las diferentes rutas de la aplicación.

Con esta estructura, has creado una aplicación Flask que redirige entre diferentes páginas de colores, cada una con un botón para volver a la página principal.

______

Made with Love ❤️ by [@jelambrar96](https://github.com/jelambrar96)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/jelambrar1)

