from flask import Blueprint,session,render_template,request, redirect, jsonify
from flask_cors import cross_origin
from models.models import User,db
registerRoute = Blueprint('registerRoute',__name__)

@registerRoute.route('', methods = ['GET', 'POST'])
@cross_origin(supports_credentials=True)
def registerApi():
    if request.method == 'GET' :
        return render_template("register.html")

    # 1.validate the data ------
    print('username' in request.get_json())
    if "username" not in request.get_json() or "password" not in request.get_json() :
        return jsonify({
            'message' : 'missing field'
        }),409
    username = request.get_json()['username']
    password = request.get_json()['password']
    print(username,password)
    if username == '' or password == '':
        return jsonify({
            'message' : 'field is empty'
        }),400
    # 1 user already exist or not 
    existing_user = User.query.filter_by(name = username).first()
    if existing_user:
        return jsonify({
            'message': 'user alredy exist'
        }),409
    # -------------------------------------------

    # 2. username,password data format validation 
    # lastly insert data into DB
    new_user = User(name = username, password = password)
    db.session.add(new_user)
    db.session.commit()
    session['user'] = username+'-'+password
    print('session intialized by register')
    return jsonify({
        'message' : 'account created'
    }),201