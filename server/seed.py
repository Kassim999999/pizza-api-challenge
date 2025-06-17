from server.app import app
from server.models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="Mario's Pizza", address="123 Main Street")
    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    rp1 = RestaurantPizza(price=10, restaurant=r1, pizza=p1)

    db.session.add_all([r1, p1, rp1])
    db.session.commit()
