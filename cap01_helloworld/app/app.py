"""
Aplicación que ejecuca un Hello World
"""

# Importa la clase Flask desde el paquete flask.
# Flask es el microframework que usaremos para crear nuestra aplicación web.
from flask import Flask

# Crea una instancia de la clase Flask.
# Esta instancia es nuestra aplicación WSGI.
# El argumento __name__ es el nombre del módulo actual,
# se utiliza para determinar la ruta de los archivos y la configuración.
app = Flask(__name__)

# Utiliza el decorador route() para decirle a Flask qué URL debe activar nuestra función.
# Aquí estamos definiendo la ruta raíz de nuestra aplicación, es decir, '/'.
@app.route('/')
def home():
    """
    Esta función será llamada cuando un usuario visite la URL raíz ('/') de nuestra aplicación.
    La función devuelve el texto "Hello, World!", que se mostrará en el navegador del usuario.    
    """
    return "Hello, World!"

# Verifica si el archivo actual está siendo ejecutado directamente y no importado.
# Si es así, ejecuta la aplicación Flask.
if __name__ == '__main__':
    # Llama a la función run() para ejecutar la aplicación en el servidor de desarrollo de Flask.
    # El parámetro debug=True activa el modo de depuración, que es útil para el desarrollo.
    # En el modo de depuración, el servidor se reiniciará automáticamente si se detectan cambios
    # en el código.
    app.run(debug=True)
