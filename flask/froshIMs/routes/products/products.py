from flask import Blueprint,session,redirect,request
from sqlalchemy import text
from models.models import db,Products
productsRoute = Blueprint('productsRoute',__name__)

@productsRoute.route('/', methods = ['GET','POST']) # get and add product
def get_product():
    # rate limeter
    if request.method == 'POST':
        # check session ====================================
        # auth('user')
        if not session.get('user'):
            return redirect('/login')
        # validation ====================================
        print('userID')
        if "productTitle" not in request.form or "productContent" not in request.form :
            return 'invalid form data'
        productContent = request.form['productContent']
        productTitle = request.form['productTitle']
        print(productContent)
        print(productTitle)
        if not productContent or not productTitle:
            return 'empty value'
        
        # insert query ====================================
        print(session.get('user').split('-')[0])
        # print()
        userID = db.session.execute(text('select User.id from User where name = :x_name'),
                                    {"x_name" : session.get('user').split('-')[0]}).first()
        print(userID)
        if not userID:
            return 'user name not available'
        productInsertion = db.session.execute(
            text('''
            insert into products (userId,productTitle,productContent)  
                  values(:uid,:pt,:pc)'''
            ),{'uid':userID[0],'pt':productTitle,
               'pc':productContent}
        )
        db.session.commit()
        print(userID[0])
        return 'done'
    
    return 'get command'
