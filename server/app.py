from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db 
from .controllers import register_controllers

app = Flask(__name__)
app.config.from_object("server.config")

db.init_app(app)
migrate = Migrate(app, db)

register_controllers(app)


app.config.from_object("server.config")


if __name__ == "__main__":
    app.run()
