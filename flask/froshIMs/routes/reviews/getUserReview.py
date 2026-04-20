from flask import Blueprint,session,redirect,request
from sqlalchemy import text
from models.models import db,Products
getUserReview = Blueprint('getUserReview',__name__)

@getUserReview.route('/') # get and add product
def get_user_review():
    # rate limeter
    # check session ====================================
    # auth('user')
    if not session.get('user'):
        return redirect('/login')
    # validation ====================================
    print('userID')

    # find user id query ====================================
    print(session.get('user').split('-')[0])
    userID = db.session.execute(text('select User.id from User where name = :x_name'),
                                {"x_name" : session.get('user').split('-')[0]}).first()
    print(userID)
    if not userID:
        return 'user name not available'
    # insert query ====================================
    getUserReviews = db.session.execute(
        text('''
        select * from reviews where userId = :id'''
        ), {'id' : userID[0]}
    )
    result = getUserReviews
    print(result,'============')
    for x in result:
        print(x)
    # result = db.session.commit(getUserReview)
    # result = db.session.mapping(getUserReviews)
    print(userID[0])
    print(result)
    return 'done'
    
    return 'get command'
