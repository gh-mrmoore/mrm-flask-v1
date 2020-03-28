from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

from flask.ext.heroku import Heroku

app = Flask(__name__)
#db = SQLAlchemy(app)

app.secret_key = 'jpfsop0495nfuianrgp019283iuern0n87unrnub098346ounb'
"""
#create the model(s) for the tasks we need to add
class User(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    userEmail = db.Column(db.String(120))
    userTasks = db.relationship('Task', backref='owner')

    def __init__(self, usermail)
    self.userEmail = userEmail

class Task(db.Model):
    taskID = db.Column(db.Integer, primary_key=True)
    taskDescription = db.Column(db.String(120))
    taskCompletion = db.Column(db.Boolean)
    taskOwnerID = db.Column(db.Integer, db.ForeignKey('user.userID'))

    def __init__(self, description, owner):
        self.taskDescription = description
        self.taskCompletion = False
        self.taskOwnerID = owner
"""

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