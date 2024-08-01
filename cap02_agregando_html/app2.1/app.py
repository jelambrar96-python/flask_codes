"""
Retorna una cadena de texto que contiene el código HTML
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    """
    Retorna una cadena de texto que contiene el código HTML
    """
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
