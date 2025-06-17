from server.models import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from server.controllers import register_controllers

def create_app():
    app = Flask(__name__)
    app.config.from_object("server.config")

    db.init_app(app)
    migrate = Migrate(app, db)
    register_controllers(app)

    return app
