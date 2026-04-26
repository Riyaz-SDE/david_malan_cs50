from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os
# app = Flask(__name__)
# print('inilized sql')

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config["SECRET_KEY"]  = 'XXX'
    app.config["SESSION_COOKIE_SAMESITE"] = None
    app.config["SESSION_COOKIE_SECURE"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir,'demo_table.db')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]  = False
    db.init_app(app)
    migrate.init_app(app,db)
    cors.init_app(app,resources={r'/*' : {"origins" : 'http://localhost:5173'}},
                  supports_credentials=True )
    # with app.app_context(): # this wil create db if doesnt exist
    #     db.create_all()
    return app