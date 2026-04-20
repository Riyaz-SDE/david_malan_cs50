from flask import  render_template, request, session, redirect, Blueprint
from sqlalchemy import select,text
from models.models import db, User
profileSearchRoute = Blueprint('profileSearchRoute',__name__)


@profileSearchRoute.route('', methods = ['GET','POST'])
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