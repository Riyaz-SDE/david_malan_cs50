from flask import Blueprint, session, render_template,jsonify
from flask_cors import cross_origin
logoutRoute = Blueprint('logoutRoute',__name__)

@logoutRoute.route('', methods = ['POST','OPTIONS'])
@cross_origin(supports_credentials=True)
def logoutApi():
    
    if session.get('user') :
        session.clear() 
        print('session cleared')
        return jsonify({
            'message' :'your are logged out'
        }),204
    print('not even logged in')
    return jsonify({
        'message' :'user not logged in'
    }),401
    print('session cleared')
    return render_template('index.html')