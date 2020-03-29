import os
import jinja2

import requests
from flask import Flask, request, redirect, render_template, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
from flask_heroku import Heroku

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
heroku = Heroku(app)
#db = SQLAlchemy(app)


#define any global-level variables that might be needed
app.secret_key = 'jpfsop0495nfuianrgp019283iuern0n87unrnub098346ounb'


#create the main starting page for the application
@app.route('/', methods=['POST', 'GET', 'PUT'])   #PUT method is used for updates from form data
def index():
    return render_template('index.html', title="A Little Project")

#create a path for tasks that need to be completed
@app.route('/tasks', methods=['GET'])
def taskList():
    if request.method == 'POST':
        return render_template('tasks.html', title="Tasks Post")
    else:
        return render_template('tasks.html', title="Tasks Get")

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()