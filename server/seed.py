from server.app import app
from server.models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="PizzaInn", address="100 Hurlingham Street")
    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")

    db.session.add_all([r1, p1])
    db.session.commit()

    rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
    db.session.add(rp1)
    db.session.commit()
