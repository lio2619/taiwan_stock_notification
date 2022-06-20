from app import app
from app import db
from app import ma

from app.utils.get_stock_price import read_csv_dict

class UserTargetPrice(db.Model):
    __tablename__ = 'users_target_price'

    id           = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username     = db.Column(db.Integer, db.ForeignKey("users_email.id"))
    email        = db.Column(db.Integer, db.ForeignKey("users_email.id"))
    already_send = db.Column(db.Integer, nullable = False)
    stock_name   = db.Column(db.String(30), nullable = False)
    stock_code   = db.Column(db.String(30), nullable = False)
    target_price = db.Column(db.String(30), nullable = False)
    created_at   = db.Column(db.DateTime, default = db.func.now())
    updated_at   = db.Column(db.DateTime, onupdate = db.func.now())

    def __init__(self, username, email, stock_name, target_price):
        self.username = username
        self.email = email
        self.already_send = 0
        self.stock_name = stock_name
        self.target_price = target_price
        self.stock_code = read_csv_dict(stock_name)

    def __repr__(self):
        return 'name %s' %self.name

class UserEmail(db.Model):
    __tablename__ = 'users_email'

    id           = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username     = db.Column(db.String(30), nullable = False, unique = True)
    email        = db.Column(db.String(100), nullable = False, unique = True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return 'name %s' %self.name

class UserTargetPriceSchema(ma.Schema):
    class Meta:
        fields = (
            "username",
            "email",
            "stock_name",
            "target_price"
        )

class UserEmailSchema(ma.Schema):
    class Meta:
        fields = (
            "username",
            "email",
        )