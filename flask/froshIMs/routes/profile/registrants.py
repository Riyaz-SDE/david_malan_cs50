from flask import Blueprint,session, render_template, redirect
from models.models import User
from ..util.auth_middleware import auth
registrantsRoute = Blueprint('registrantsRoute',__name__)
@registrantsRoute.route('/', methods = ['GET', 'POST'])
@auth
def registrants():
    # it will check the session
    # if not session.get('user'):
    #     return redirect('/login')

    users = User.query.with_entities(User.name).all()
    print(users)
    # return users
    return render_template('index.html')