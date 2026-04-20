from flask import Blueprint,session,redirect,request
from sqlalchemy import text
from models.models import db,Products
addReview = Blueprint('addReview',__name__)

@addReview.route('/<productId>', methods = ['GET','POST']) # get and add product
def add_review(productId):
    # rate limeter
    if request.method == 'POST':
        # check session ====================================
        # auth('user')
        if not session.get('user'):
            return redirect('/login')
        # validation ====================================
        print('userID')
        if  "reviewContent" not in request.form :
            return 'invalid form data'
        reviewContent = request.form['reviewContent']
        
        print(reviewContent)
        
        if not reviewContent:
            return 'empty value'
        if not productId and productId >= 0:
            return 'not valid product'
        # find user id query ====================================
        product = text('select * from Products where productId = :pid')
        productId = db.session.execute(product, {'pid' : productId}).first()
        if productId:
            print('product exist', productId)
            productId = productId[0]
        else:
            print('product not exist')
            return 'null'
        print(session.get('user').split('-')[0])
        # print()
        userID = db.session.execute(text('select User.id from User where name = :x_name'),
                                    {"x_name" : session.get('user').split('-')[0]}).first()
        print(userID)
        if not userID:
            return 'user name not available'
        # insert query ====================================
        productInsertion = db.session.execute(
            text('''
            insert into Reviews (userId,productId,reviewContent)  
                  values(:uid,:pid,:pc)'''
            ),{'uid':userID[0],
               'pid':productId,
               'pc':'reviewContent'}
        )
        db.session.commit()
        print(userID[0])
        return 'done'
    
    return 'get command'
