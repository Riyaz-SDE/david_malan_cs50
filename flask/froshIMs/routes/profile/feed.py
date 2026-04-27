from flask import Blueprint, jsonify,session,request
from ..util.auth_middleware import auth
from models.models import User,Products

feedRoute = Blueprint('feed',__name__)

@feedRoute.route('')
@auth
def feed():
    print(session.get('user').split('-')[1])
    id = session.get('user').split('-')[1]
    # pagination params 
    page = request.args.get('page',1,type=int)
    per_page = request.args.get('limit',10,type=int)
    # select * from posts where userID = id
    products = Products.query.filter_by(userId = id)\
    .paginate(page=page,per_page=per_page,error_out=False)
    print(products)
    productsList = [{
        'productId' : items.productId,
        'userId' : items.userId,
        'productTitle' : items.productTitle,
        'productContent' : items.productContent,
        'productCreateAt' : items.productCreateAt
    } for items in products]
    print((productsList))
    return jsonify({
        'message' : 'success',
        'data' : productsList,
        'authenticated' : True
    }),200