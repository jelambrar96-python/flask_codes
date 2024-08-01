"""simple app"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    """return home on root route"""
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
