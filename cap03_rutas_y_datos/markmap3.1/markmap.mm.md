---
title: Manejo de Rutas y Datos en Flask
markmap:
  colorFreezeLevel: 2
---

## Flask

- **Framework**: Microframework para aplicaciones web en Python

## Manejo de Rutas

### Decorador `@app.route`

- Define la URL y la función correspondiente
- Ejecuta la función cuando se accede a la URL

### Ejemplo Básico

```python
@app.route('/')
def home():
    return "Hello, World!"
```

### Parámetros en la URL

- **Parámetros Variables**
  ```python
  @app.route('/user/<username>')
  def show_user_profile(username):
      return f'User: {username}'
  ```
- **Tipos de Datos**
  ```python
  @app.route('/post/<int:post_id>')
  def show_post(post_id):
      return f'Post ID: {post_id}'
  ```

### Métodos HTTP

- **GET y POST**
  ```python
  @app.route('/submit', methods=['GET', 'POST'])
  def submit():
      if request.method == 'POST':
          return 'Form Submitted!'
      return 'Submit the form'
  ```

### Redireccionamientos

- **`redirect` y `url_for`**
  ```python
  @app.route('/')
  def index():
      return redirect(url_for('home'))
  ```

## Made with Love ❤️ by [@jelambrar96](https://github.com/jelambrar96)
  - ["Buy Me A Coffee"](https://www.buymeacoffee.com/jelambrar1)
