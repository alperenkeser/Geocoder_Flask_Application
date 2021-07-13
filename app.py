from flask import Flask

from geo_search import geo_search
from database import db
import logging


def create_app():
    app = Flask(__name__)

    # Database configuration and creating a database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///address.db'

    db.init_app(app)

    with app.app_context():
        #db.drop_all()
        db.create_all()

    return app

# Creating an app
app = create_app()

# Registering a geo_search blueprint
app.register_blueprint(geo_search)

if __name__ == "__main__":
    app.run(debug=True)


