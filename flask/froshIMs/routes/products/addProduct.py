from flask import Blueprint,session, jsonify,request
from flask_cors import cross_origin
from ..util.auth_middleware import auth
from models.models import Products,db
addProductRoute = Blueprint('addProduct', __name__)

@addProductRoute.route('',methods = ['POST'])
@cross_origin(supports_credentials=True)
@auth
def addProduct():
    ProductTitle = request.get_json().get('productTitle')
    ProductContent = request.get_json().get('productContent')
    id = session.get('user').split('-')[1]
    print(ProductContent,ProductTitle,id)
    if not ProductTitle or not ProductContent:
        return ({'message' : 'invalid data'}),409
    # validate data
    # check for dupicate in case needed
    # inseert query
    new_product = Products(
        userId = id,productTitle = ProductTitle,productContent = ProductContent)
    db.session.add(new_product)
    db.session.commit()
    return({'message' : 'product added'}),200