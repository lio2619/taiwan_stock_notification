from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

from config import config
from config import mail_config

app = Flask(__name__)
app.config['SERVER_NAME'] = config.SERVER_NAME

app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app, use_native_unicode = "utf-8")

manager = Manager(db)