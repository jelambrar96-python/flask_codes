from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    """return home on root route"""
    return "Hello, World!"


@app.route('/search')
def search():
    """print keywords"""
    query = request.args.get('query')
    return f'You searched for: {query}'


@app.route('/login', methods=['GET', 'POST'])
def login():
    """login page, 
    behaivour changes depend on method"""
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
    """get data from json"""
    data = request.json
    return f'JSON received: {data}'


@app.route('/headers')
def headers():
    """headers"""
    user_agent = request.headers.get('User-Agent')
    return f'Your User-Agent is: {user_agent}'


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    """form to upload file"""
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
