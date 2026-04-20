from flask import Blueprint
from sqlalchemy import text
from ini import db
productById = Blueprint('productById',__name__)

@productById.route('')
def getProductsByUser(id):
    if id<=0 or not id:
        return 'invalid id fro product'
    query = text('select * from products where productId = :pid')
    result = db.session.execute(query,{'pid' : id})
    for res in result:
        print(res)
        if res:
            result = res
        print('result',result)
    return 'get api'