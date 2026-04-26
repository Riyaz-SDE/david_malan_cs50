from flask import Blueprint, request, render_template, session, redirect,jsonify
from ..util.util import checkFieldExist,isDataNull
from models.models import User
from flask_cors import cross_origin

loginRoute = Blueprint('logiRoute',__name__)

@loginRoute.route('', methods = ["GET","POST"])
@cross_origin(supports_credentials=True)
def loginApi(): 
    
    if request.method == 'POST':
        # 1 data field validation
        checkFieldExist( request= request)
        username = request.get_json().get('username')
        password = request.get_json().get('password')
        isDataNull(username,password)

        # query used to check credentials are true
        # select * from user where name = username and password = password
        isUser = User.query.filter_by(name = username, password = password).first()

        # this will intiate session if user exist
        if isUser:
            session['user'] = username+'-'+password
            print('session intiated',session.get('user'))
            return jsonify({
                'authenticated': True,
                    'user': {
                        'data' : 'user-data-comes-here'
                    }
            }),200
        
        return jsonify({
                'authenticated': False,
                    'user': {
                        'data' : 'USER ALREADY EXIST'
                    }
            }),401
            # redirect('http://localhost:5173/feed')
        # if wrong credential 
        # return "<h1> wrong credential </h1>  <a href='/login'> login </a>"
    if request.method == "GET":
        print('working',dict(session))
        if session.get("user"):
            return jsonify ({
                'authenticated': True,
                'user': {
                    'data' : 'user-data-comes-here'
                }
            }),200
        
        return jsonify({
            'authenticated' : False
        }),401