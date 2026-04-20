from flask import Flask, render_template, request, session, redirect
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select,text
import os
from models.models import db, User, Products
from flask_migrate import Migrate
from routes.login.login import loginRoute
from routes.logout.logout import logoutRoute
from routes.register.register import registerRoute
from routes.profile.profileSearch import profileSearchRoute
from routes.profile.registrants import registrantsRoute
app = Flask(__name__)

#session config
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#sql config
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir,'demo_table.db')
app.config["SQLALCHEMY_TRACK_MODIFICATION"]  = False
# db = SQLAlchemy(app)
# migrate = Migrate(app,db)
# # create model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(25), unique = True)
#     password = db.Column(db.String(30), nullable = False)
#     role = db.Column(db.String(20), server_default = 'watchers')
#     createAt = db.Column(db.DateTime, server_default = db.func.now())
# class Products(db.Model):
#     productId = db.Column(db.Integer, primary_key = True)
#     userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     productTitle = db.Column(db.String(30), nullable = False)
#     productContent = db.Column(db.String(300), nullable = False)
#     productCreateAt = db.Column(db.DateTime, server_default = db.func.now())
# trigger that
db.init_app(app)
migrate = Migrate(app,db)
with app.app_context():
    db.create_all()
#util func
def checkFieldExist(request = request, *fields, method = None):
    # def f():
    #     cond = False
    #     for field in fields:
    #         cond = cond or field not in request.form
    #     return cond
    # if f():
    #     return 'invalid data'
    if "user_name" not in request.form or "password" not in request.form :
        return 'invalid form data'
def isDataNull(*data):
    for value in data:
        if value:
            # break
            return ' one of the value is null' 
def auth(fieldName):
    if not session.get(fieldName):
        return redirect('/login')

# APIs
@app.route('/', methods = ['Get','Post'])
def index():
    # this not involved any session
    if request.method == 'POST':
        return 'hi'
    return render_template('login.html')
    # return 'api  working'

@app.route('/_login', methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    
    # 1 while post the session gets stored
    # 2 field validation
    checkFieldExist( request= request)
    username = request.form['user_name']
    password = request.form['password']
    isDataNull(username,password)

    # lookup
    # select * from user where name = username and password = password
    isUser = User.query.filter_by(name = username, password = password).first()

    # check user data and intiate session 
    if isUser:
        session['user'] = username+'-'+password
        #     return redirect('/registrants')
        print('session intiated')
        return render_template('index.html')
    return "<h1> wrong credential </h1>  <a href='/login'> login </a>"
        # fields = request.form
        # if 
        #     session["name"] = fields.get("name")
        #     return redirect('/registrants')

app.register_blueprint(loginRoute, url_prefix = '/login')
app.register_blueprint(logoutRoute, url_prefix = '/logout')
app.register_blueprint(registerRoute, url_prefix = '/logout')
app.register_blueprint(profileSearchRoute, url_prefix = '/profile/<username>')
app.register_blueprint(registrantsRoute, url_prefix = '/registrants')
@app.route('/_register', methods = ['GET', 'POST'])
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
    session['user'] = username+password
    redirect('/registrants')
    print('session executed')
    return render_template('index.html')

@app.route('/_profile/<username>', methods = ['GET','POST'])
def profile(username):
    # validate user name
    print(type(username))
    if not isinstance(username,str) :
        return 'check username type'
    if len(username) < 3 :
        return 'check username'
    # check user exist
    # isUserExist = User.query.filter_by(name = username)
    query = select(User.id,User.name,User.createAt).where(
        User.name == username
    )
    result = db.session.execute(query).first()
    print('before',result)
    if not result:
        return 'user not found'
    for field in result._fields:
        print(field )
    print(result)
    # return result
    return 'success'
    # look up data
@app.route('/__registrants')
def registrants():
    # it will check the session
    if not session.get('user'):
        return redirect('/login')

    users = User.query.with_entities(User.name).all()
    print(users)
    # return users
    return render_template('index.html')

@app.route('/__logout', methods = ['POST'])
def logout():
    
    if session.get('user') :
        session.clear() 
        print('session cleared')
    print('session cleared')
    return render_template('index.html')

@app.route('/products', methods = ['GET','POST']) # get and add product
def get_product():
    # rate limeter
    if request.method == 'POST':
        # check session ====================================
        # auth('user')
        if not session.get('user'):
            return redirect('/login')
        # validation ====================================
        if "productTitle" not in request.form or "productContent" not in request.form :
            return 'invalid form data'
        productContent = request.form['productContent']
        productTitle = request.form['productTitle']
        print(productContent)
        print(productTitle)
        if not productContent or not productTitle:
            return 'empty value'
        
        # insert query ====================================
        print(session.get('user').split('-')[0])
        userID = db.session.execute(text('select User.id from User where name = :x_name'),
                                    {"x_name" : session.get('user').split('-')[0]}).first()
        productInsertion = db.session.execute(
            text('''
            insert into products (productId,userId,productTitle,productContent)  
                  values(:pid,:uid,:pt,:pc)'''
            ),{'pid':0,'uid':userID[0],'pt':productTitle,
               'pc':productContent}
        )
        db.session.commit()
        print(userID[0])
        return 'done'

@app.route('/product/<int:id>')
def productById():
    return
@app.route('/product/<username>')
def productByUserId():
    return

if __name__ == '__main__':
    app.run(debug = True, port = '5000')