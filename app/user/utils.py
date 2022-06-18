from app import app
from app import db
from app import ma

from app.user.models import User
from app.user.models import UserSchema

user_schema = UserSchema()
user_schema = UserSchema(many = True)