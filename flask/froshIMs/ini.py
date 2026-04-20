from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
# app = Flask(__name__)
# print('inilized sql')

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir,'demo_table.db')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]  = False
    db.init_app(app)
    migrate.init_app(app,db)
    # with app.app_context(): # this wil create db if doesnt exist
    #     db.create_all()
    return app