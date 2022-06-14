from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_migrate import MigrateCommand

from config import config
from config import mail_config

app = Flask(__name__)

app.config['SERVER_NAME'] = config.SERVER_NAME
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS = False'] = config.SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app, use_native_unicode = "utf-8")

ma = Marshmallow(app)

migrate = Migrate(app, db)
manager = Manager(db)
manager.add_command('db', MigrateCommand)

from app.save_stock_code import models