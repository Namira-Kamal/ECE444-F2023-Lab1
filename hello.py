from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.errorhandler(404) 
def page_not_found(e): 
    return render_template('404.html'), 404 

@app.errorhandler(500) 
def internal_server_error(e): 
    return render_template('500.html'), 500

@app.route('/') 
def index(): 
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

# example 2-1
# @app.route('/')
# def index():
#     return '<h1>Hello World!</h1>'

# example 2-2
# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, {}!</h1>'.format(name)

