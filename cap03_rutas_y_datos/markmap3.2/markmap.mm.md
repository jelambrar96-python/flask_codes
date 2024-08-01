---
title: Manejo de Rutas y Datos en Flask
markmap:
  colorFreezeLevel: 2
---

## Flask

- **Framework**: Microframework para aplicaciones web en Python

## Acceso a Datos de la Solicitud

### Importar `request`

```python
from flask import request
```

### Parámetros de la URL

- **`request.args`**
  ```python
  @app.route('/search')
  def search():
      query = request.args.get('query')
      return f'You searched for: {query}'
  ```

### Datos del Formulario

- **`request.form`**
  ```python
  @app.route('/login', methods=['GET', 'POST'])
  def login():
      if request.method == 'POST':
          username = request.form.get('username')
          password = request.form.get('password')
          return f'Username: {username}, Password: {password}'
  ```

### Datos JSON

- **`request.json`**
  ```python
  @app.route('/api/data', methods=['POST'])
  def get_data():
      data = request.json
      return jsonify(data)
  ```

### Encabezados de la Solicitud

- **`request.headers`**
  ```python
  @app.route('/headers')
  def headers():
      user_agent = request.headers.get('User-Agent')
      return f'Your User-Agent is: {user_agent}'
  ```

### Archivos Subidos

- **`request.files`**
  ```python
  @app.route('/upload', methods=['GET', 'POST'])
  def upload_file():
      if request.method == 'POST':
          file = request.files['file']
          file.save(f'./uploads/{file.filename}')
          return f'File {file.filename} uploaded successfully.'
  ```

## Made with Love ❤️ by [@jelambrar96](https://github.com/jelambrar96)
  - ["Buy Me A Coffee"](https://www.buymeacoffee.com/jelambrar1)
