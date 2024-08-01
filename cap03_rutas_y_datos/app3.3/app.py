"""ejemplo de una aplicacion que implemente el manejo de rutas"""

from flask import Flask, redirect, url_for, request

# Crea una instancia de la clase Flask.
# Esta instancia es nuestra aplicación WSGI.
app = Flask(__name__)

# Define la ruta para la URL raíz ('/').
# Cuando un usuario visita esta URL, se ejecuta la función 'index'.
@app.route('/')
def index():
    """# Retorna un mensaje de bienvenida para la página de índice."""
    return "Welcome to the Index Page!"

# Define una ruta con un parámetro variable 'name'.
# Cuando un usuario visita una URL que coincide con este patrón, se ejecuta la función 'hello'.
@app.route('/hello/<name>')
def hello(name):
    """# Retorna un mensaje personalizado usando el valor del parámetro 'name'."""
    return f"Hello, {name}!"

# Define una ruta con un parámetro entero 'post_id'.
# Cuando un usuario visita una URL que coincide con este patrón, se ejecuta la función 'show_post'.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    """# Retorna un mensaje que incluye el ID del post."""
    return f"Post ID: {post_id}"

# Define una ruta que acepta solicitudes GET y POST.
# Cuando un usuario visita esta URL, se ejecuta la función 'submit'.
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    """# Verifica el método HTTP de la solicitud."""
    if request.method == 'POST':
        # Si la solicitud es POST, retorna un mensaje indicando que el formulario ha sido enviado.
        return 'Form Submitted!'
    else:
        # Si la solicitud es GET, retorna un mensaje solicitando el envío del formulario.
        return 'Submit the form'

# Define una ruta que redirige a otra URL.
# Cuando un usuario visita esta URL, se ejecuta la función 'redirect_example'.
@app.route('/redirect-example')
def redirect_example():
    """# Redirige al usuario a la URL asociada con la función 'hello', 
    pasando 'Flask' como parámetro 'name'."""
    return redirect(url_for('hello', name='Flask'))

# Verifica si el archivo actual está siendo ejecutado directamente y no importado.
# Si es así, ejecuta la aplicación Flask.
if __name__ == '__main__':
    # Llama a la función run() para ejecutar la aplicación en el servidor de desarrollo de Flask.
    # El parámetro debug=True activa el modo de depuración, que es útil para el desarrollo.
    app.run(debug=True)
