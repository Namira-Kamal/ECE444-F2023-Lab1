from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.errorhandler(404) 
def page_not_found(e): 
    return render_template('404.html'), 404 

@app.errorhandler(500) 
def internal_server_error(e): 
    return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')

        session['name'] = form.name.data

        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

# @app.route('/user/<name>')
# def user(name):
#     return render_template('user.html', name=name)

# @app.route('/user/<name>')
# def user(name):
#     return render_template('user.html', name=name)


#### Previous examples #####

# example 2-1
# @app.route('/')
# def index():
#     return '<h1>Hello World!</h1>'

# example 2-2
# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, {}!</h1>'.format(name)

# without time
# @app.route('/')
# def index():
#     return render_template('index.html')

# example 3-7
# @app.route('/') 
# def index(): 
#     return render_template('index.html', current_time=datetime.utcnow())