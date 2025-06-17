from flask import Blueprint

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas')
def get_restaurant_pizzas():
    return {'message': 'List of restaurant_pizzas'}
