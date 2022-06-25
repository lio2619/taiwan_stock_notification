from app import app
from app import db
from app import ma

class UserTargetPrice(db.Model):
    __tablename__ = 'users_target_price'

    id           = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username     = db.Column(db.Integer, db.ForeignKey("users_email.id"))
    email        = db.Column(db.Integer, db.ForeignKey("users_email.id"))
    stock_name   = db.Column(db.String(30), nullable = False)
    stock_code   = db.Column(db.String(30), nullable = False)
    target_price = db.Column(db.String(30), nullable = False)
    created_at   = db.Column(db.DateTime, default = db.func.now())
    updated_at   = db.Column(db.DateTime, onupdate = db.func.now())

    def __init__(self, username, email, stock_name, target_price, stock_code):
        self.username = username
        self.email = email
        self.stock_name = stock_name
        self.target_price = target_price
        self.stock_code = stock_code

    def __repr__(self):
        return 'email：%s    stock_name：%s   target_price：%s' %(self.email, self.stock_name, self.target_price)

class UserEmail(db.Model):
    __tablename__ = 'users_email'

    id           = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username     = db.Column(db.String(30), nullable = False, unique = True)
    email        = db.Column(db.String(100), nullable = False, unique = True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return 'username：%s  email：%s' %(self.username, self.email)

class UserStockPrice(db.Model):
    __tablename__ = 'users_stock_price'

    stock_code     = db.Column(db.String(30), nullable = False, unique = True, primary_key = True)
    stock_price    = db.Column(db.String(100), nullable = False, unique = True)

    def __init__(self, stock_code, stock_price):
        self.stock_code = stock_code
        self.stock_price = stock_price

    def __repr__(self):
        return 'stock_code：%s  stock_price：%s' %(self.stock_code, self.stock_price)

class UserTargetPriceSchema(ma.Schema):
    class Meta:
        fields = (
            "stock_name",
            "target_price"
        )

class UserEmailSchema(ma.Schema):
    class Meta:
        fields = (
            "username",
            "email",
        )

class UserStockPriceSchema(ma.Schema):
    class Meta:
        fields = (
            "stock_code",
            "stock_price",
        )