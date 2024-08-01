"""
Aplicación Flask de Ejemplo

Esta aplicación Flask demuestra cómo manejar diferentes tipos de solicitudes HTTP,
acceder a parámetros de la URL, manejar formularios, procesar datos JSON,
acceder a encabezados de solicitudes y manejar la subida de archivos.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    """Ruta raíz que retorna un mensaje de bienvenida."""
    return 'Welcome to the Flask app!'

@app.route('/search')
def search():
    """
    Ruta de búsqueda que accede a los parámetros de la URL.
    
    Retorna el valor del parámetro 'query' de la URL.
    """
    query = request.args.get('query')
    return f'You searched for: {query}'

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Ruta de login que maneja solicitudes GET y POST.
    
    En solicitudes POST, obtiene el nombre de usuario y contraseña del formulario.
    En solicitudes GET, muestra un formulario de login.
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        return f'Username: {username}, Password: {password}'
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/api/data', methods=['POST'])
def get_data():
    """
    Ruta de API que recibe datos en formato JSON.
    
    Retorna los datos JSON recibidos.
    """
    data = request.json
    return jsonify(data)

@app.route('/headers')
def headers():
    """
    Ruta que accede a los encabezados de la solicitud.
    
    Retorna el valor del encabezado 'User-Agent'.
    """
    user_agent = request.headers.get('User-Agent')
    return f'Your User-Agent is: {user_agent}'

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    """
    Ruta que maneja la subida de archivos.
    
    En solicitudes POST, guarda el archivo subido en el servidor.
    En solicitudes GET, muestra un formulario para subir archivos.
    """
    if request.method == 'POST':
        file = request.files['file']
        file.save(f'./uploads/{file.filename}')
        return f'File {file.filename} uploaded successfully.'
    return '''
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file"><br>
            <input type="submit" value="Upload">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
