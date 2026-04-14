from flask import Flask, render_template, request, session, redirect
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

#session config
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#sql config
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir,'demo_table.db')
app.config["SQLALCHEMY_TRACK_MODIFICATION"]  = False
db = SQLAlchemy(app)

# create model
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(25), unique = True)
    password = db.Column(db.String(30), nullable = False)
    createAt = db.Column(db.DateTime, server_default = db.func.now())
# trigger that
with app.app_context():
    db.create_all()

# APIs
@app.route('/', methods = ['Get','Post'])
def index():
    # this not involved any session
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
    # while post the session gets stored
    print(request.method)
    if request.method == "POST":
        fields = request.form
        if "name" in fields:
            session["name"] = fields.get("name")
            return redirect('/registrants')
    return render_template('login.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET' :
        return render_template("register.html")

    # validate the data
    if "user_name" not in request.form or "password" not in request.form :
        return 'invalid form data'
    username = request.form['user_name']
    password = request.form['password']

    if username == '' or password == '':
        return 'one of the form dat is null'
    # 1 user already exist or not 
    existing_user = User.query.filter_by(name = username).first()
    if existing_user:
        return 'username already exist'
    # 2 username,password data format validation 
    # lastly insert data into DB
    new_user = User(name = username, password = password)
    db.session.add(new_user)
    db.session.commit()
    session['name'] = username+password
    redirect('/registrants')
    return 'exe'

@app.route('/registrants')
def registrants():
    # it will check the session
    print(session.get('name'))
    if not session.get('name'):
        return redirect('/login')
    print(session.get('name'))
    return render_template('index.html')

@app.route('/logout', methods = ['POST'])
def logout():
    print(session.get('name'))
    if session.get('name') :
        session.clear() 
        print('session cleared')
    return render_template('index.html')
    
        
app.run(debug = True, port = '5000')