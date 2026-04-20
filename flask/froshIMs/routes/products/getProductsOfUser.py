from flask import Blueprint
from sqlalchemy import text
from ini import db

productsOfUser = Blueprint('productOfuser',__name__)

@productsOfUser.route('')
def getProductsByUser(username):
    if not username :
        return 'invalid username fro product'
    print(username)
    query = text('select id from user where name = :username')
    result = db.session.execute(query,{'username' : username})
    for res in result:
        print(res)
    print(result)
    return 'get api'