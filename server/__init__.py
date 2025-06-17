from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db 
from .controllers import register_controllers  # This should import a function that registers all Blueprints

app = Flask(__name__)
app.config.from_object("server.config")  # Your config file (e.g., database URI)

db.init_app(app)
migrate = Migrate(app, db)

register_controllers(app)  # Register all controllers (blueprints)

if __name__ == "__main__":
    app.run(debug=True)
