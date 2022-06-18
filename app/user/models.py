from app import app
from app import db
from app import ma

from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id         = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username   = db.Column(db.String(30), nullable = False, unique = True)
    password   = db.Column(db.String(128), nullable = False)
    email      = db.Column(db.String(128), nullable = False, unique = True)
    created_at = db.Column(db.DateTime, default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    def __init__(self, username, password, email):
        self.username = username
        self.set_password(password)
        self.email = email

    def __repr__(self):
        return 'name %s' %self.name

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class UserSchema(ma.Schema):
    class Meta:
        fields = (
            "username",
            "email"
        )