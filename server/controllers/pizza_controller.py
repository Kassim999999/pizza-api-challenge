from flask import Blueprint

pizza_bp = Blueprint('pizza_bp', __name__)

@pizza_bp.route('/pizzas')
def get_pizzas():
    return {'message': 'List of pizzas'}
