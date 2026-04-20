from ini import db
# db = SQLAlchemy()
# migrate = Migrate(app,db)
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(25), unique = True)
    password = db.Column(db.String(30), nullable = False)
    role = db.Column(db.String(20), server_default = 'watchers')
    createAt = db.Column(db.DateTime, server_default = db.func.now())
class Products(db.Model):
    productId = db.Column(db.Integer, primary_key = True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    productTitle = db.Column(db.String(30), nullable = False)
    productContent = db.Column(db.String(300), nullable = False)
    productCreateAt = db.Column(db.DateTime, server_default = db.func.now())
class Reviews(db.Model):
    reviewId = db.Column(db.Integer, primary_key = True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    productId = db.Column(db.Integer, db.ForeignKey('products.productId'), nullable = False)
    reviewContent = db.Column(db.String(300), nullable = False)
    reviewCreatedOn = db.Column(db.DateTime, server_default = db.func.now())
    rating = db.Column(db.Integer)