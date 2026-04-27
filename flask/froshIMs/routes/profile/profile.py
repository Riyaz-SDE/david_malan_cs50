from flask import Blueprint, session, jsonify
from flask_cors import cross_origin
from ..util.auth_middleware import auth
from models.models import User
profileRoute = Blueprint('profile',__name__)

@profileRoute.route('')
@cross_origin(supports_credentials=True)
@auth
def profile():
    sessionList = session.get('user').split('-')
    # userData = {for data in session}
    print(sessionList)
    userDetail = User.query.filter_by(id = sessionList[1]).first()
    print(userDetail)
    print((userDetail.id))
    print((userDetail.name))
    return jsonify({
        'authenticate' : True   ,
        'userDetails' : {
            'id':userDetail.id,
            'name':userDetail.name,
            'password':userDetail.password,
            'role':userDetail.role,
            'createAt':userDetail.createAt,
        }
    }),200