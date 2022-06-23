from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from flask_apscheduler import APScheduler
from flask_mail import Mail

from config import config
from config import mail_config
from config import apscheduler_job_config

app = Flask(__name__)

app.config.from_object(apscheduler_job_config())
app.config['SERVER_NAME'] = config.SERVER_NAME
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS = False'] = config.SQLALCHEMY_TRACK_MODIFICATIONS

app.config['MAIL_SERVER'] = mail_config.MAIL_SERVER
app.config['MAIL_PROT'] = mail_config.MAIL_PROT
app.config['MAIL_USE_TLS'] = mail_config.MAIL_USE_TLS
app.config['MAIL_USERNAME'] = mail_config.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = mail_config.MAIL_PASSWORD

db = SQLAlchemy(app, use_native_unicode = "utf-8")

ma = Marshmallow(app)

migrate = Migrate(app, db)
manager = Manager(db)
manager.add_command('db', MigrateCommand)

scheduler = APScheduler()
scheduler.init_app(app)

mail = Mail()
mail.init_app(app)

from app.user import models
from app.user import controllers

from app.utils import request_schema
from app.utils import send_mail