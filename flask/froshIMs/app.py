from flask import Flask, render_template, request, session, redirect
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir,'demo_table.db')
app.config["SQLALCHEMY_TRACK_MODIFICATION"]  = False
db = SQLAlchemy(app)
Session(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(25), unique = True)
    password = db.Column(db.String(30), nullable = False)
    createAt = db.Column(db.DateTime, server_default = db.func.now())
with app.app_context():
    db.create_all()

@app.route('/', methods = ['Get','Post'])
def index():
    if request.method == 'POST':
        fields = request.form
        for field in fields:
            print(field +":"+fields.get(field) )
        print('end')
        return 'hi'
    
    print(request.method)
    return render_template('login.html')
    # return 'api  working'

@app.route('/login', methods = ["GET","POST"])
def login():
    print('debug')
    print(request.method)
    if request.method == "POST":
        fields = request.form
        if "name" in fields:
            session["name"] = fields.get("name")
            return redirect('/registrants')
    return render_template('login.html')

@app.route('/registrants')
def registrants():
    if not session.get('name'):
        return redirect('/login')
    print(session.get('name'))
    return render_template('index.html')
        
app.run(debug = True, port = '5000')