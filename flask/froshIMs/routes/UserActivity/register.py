from flask import Blueprint,session,render_template,request, redirect
from models.models import User,db
registerRoute = Blueprint('registerRoute',__name__)

@registerRoute.route('/', methods = ['GET', 'POST'])
def registerApi():
    if request.method == 'GET' :
        return render_template("register.html")

    # 1.validate the data ------
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
    # -------------------------------------------

    # 2. username,password data format validation 
    # lastly insert data into DB
    new_user = User(name = username, password = password)
    db.session.add(new_user)
    db.session.commit()
    session['user'] = username+'-'+password
    redirect('/registrants')
    print('session executed')
    return render_template('index.html')