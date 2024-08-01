"""routing management"""

from flask import Flask
from flask import redirect, request, url_for


app = Flask(__name__)


# basic
@app.route('/')
def home():
    """return home on root route"""
    return "Hello, World!"


# parameter
@app.route('/user/<username>')
def show_user_profile(username):
    """return nome of usename"""
    return f'User: {username}'


# setting type of parameter
@app.route('/post/<int:post_id>')
def show_post(post_id):
    """return the post id"""
    return f'Post ID: {post_id}'


# requests
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    """this route reponse on a different way depend 
    on http method"""
    if request.method == 'POST':
        return 'Form Submitted!'
    else:
        return 'Submit the form'


# basic redirect
@app.route('/home')
def index():
    """redirect to home"""
    return redirect(url_for('/'))


# redirect with data
@app.route('/profile/<username>')
def profile(username):
    """profile username page"""
    return f'Profile page of {username}'

@app.route('/JohnDoe')
def johndoue():
    """johndoe's profile"""
    return redirect(url_for('profile', username='JohnDoe'))




if __name__ == '__main__':
    app.run(debug=True)
