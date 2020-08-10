from flask import Flask
from flask_wtf import CSRFProtect
from webapp.config.Config import Dev, Prod
from flask_sqlalchemy import SQLAlchemy
from logging import FileHandler, WARNING
db = SQLAlchemy()

app = Flask("webapp", template_folder='templates', static_folder='static')
app.config.from_object(Dev)
csrf = CSRFProtect()

#Config and load CSRF
csrf.init_app(app)

#init db
db.init_app(app)
with app.app_context():
    db.create_all()

from webapp.controllers import *