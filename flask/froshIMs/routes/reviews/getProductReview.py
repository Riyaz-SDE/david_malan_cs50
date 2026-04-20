from flask import Blueprint,session,redirect,request
from sqlalchemy import text
from models.models import db,Products
getProductReview = Blueprint('getProductReview',__name__)

@getProductReview.route('/<int:productId>') # get and add product
def get_user_review(productId):
    # rate limeter
    # check session ====================================
    # auth('user')
    if not session.get('user'):
        return redirect('/login')
    # validation ====================================
    # insert query ====================================
    print(f' productId {productId}')
    if not productId:
        return 'productId is none'
    getUserReviews = db.session.execute(
        text('''
        select * from reviews where productId = :id'''
        ), {'id' : productId}
    )
    result = getUserReviews
    print(result,'============')
    for x in result:
        print(x)
    # result = db.session.commit(getUserReview)
    # result = db.session.mapping(getUserReviews)
    print(result)   
    return 'done'
    
    return 'get command'
