from flask import Flask
from models import db
from controllers.restaurants_controller import restaurant_bp
from controllers.pizzas_controller import pizza_bp
from controllers.restaurant_pizzas_controller import restaurant_pizza_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register blueprints
app.register_blueprint(restaurant_bp)
app.register_blueprint(pizza_bp)
app.register_blueprint(restaurant_pizza_bp)

if __name__ == '__main__':
    app.run(debug=True)
