from flask import Flask, render_template, request
from forms import SignUpForm
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def home():
    return 'Welcome to FaceBook'

@app.route('/about')
def about():
    posts = [{'Name':"Puran", 'Friends':'10'},
             {'Name':'Sahan', 'Friends':'999'}]
    return render_template('about.html', author = 'Bisharath', coauthor = False, posts = posts )

@app.route('/about/<string:userid>')
def username(userid):
    return 'Name: ' + userid

@app.route('/signup', methods = ['GET','POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result = result)
    return render_template('signup.html', form = form)

if __name__ == '__main__':
    app.run()
