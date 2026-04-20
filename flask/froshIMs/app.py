from flask import Flask, render_template, request, session, redirect
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select,text
import os
from models.models import  User, Products
from flask_migrate import Migrate
from routes.UserActivity.login import loginRoute
from routes.UserActivity.logout import logoutRoute
from routes.UserActivity.register import registerRoute
from routes.profile.profileSearch import profileSearchRoute
from routes.profile.registrants import registrantsRoute
from routes.products.products import productsRoute
from routes.products.getProductById import productById
from routes.products.getProductsOfUser import productsOfUser
from routes.reviews.addReview import addReview
from routes.reviews.getUserReview import getUserReview
from routes.reviews.getProductReview import getProductReview
from ini import create_app

app = create_app()

#session config
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# APIs
@app.route('/', methods = ['Get','Post'])
def index():
    # this not involved any session
    if request.method == 'POST':
        return 'hi'
    return render_template('login.html')
    # return 'api  working'

# login logout register
app.register_blueprint(loginRoute, url_prefix = '/login')
app.register_blueprint(logoutRoute, url_prefix = '/logout')
app.register_blueprint(registerRoute, url_prefix = '/register')
# get registrants and profile of user
app.register_blueprint(registrantsRoute, url_prefix = '/registrants')
app.register_blueprint(profileSearchRoute, url_prefix = '/profile/<username>')
# post product and get product by it id or user name
app.register_blueprint(productsRoute, url_prefix = '/products')
app.register_blueprint(productById, url_prefix = '/product/<int:id>')
app.register_blueprint(productsOfUser, url_prefix = '/product/<username>')
#  review
app.register_blueprint(addReview, url_prefix = '/review/add')
app.register_blueprint(getUserReview, url_prefix = '/review/user')
app.register_blueprint(getProductReview, url_prefix = '/productreview')


if __name__ == '__main__':
    app.run(debug = True, port = '5000')