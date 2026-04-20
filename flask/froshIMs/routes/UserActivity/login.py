from flask import Blueprint, request, render_template, session
from ..util.util import checkFieldExist,isDataNull
from models.models import User

loginRoute = Blueprint('logiRoute',__name__)

@loginRoute.route('', methods = ["GET","POST"])
def loginApi(): 
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