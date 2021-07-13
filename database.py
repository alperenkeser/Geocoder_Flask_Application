from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Database table
class geocode_table(db.Model):
    """
        geocode_table gathering information searched address

        id = id -> Integer Primary Key
        name = address -> String Not Null
        longitude = longitude -> Float
        latitude = latitude -> Float
        distance = distance to Moscow Ring Road -> Float
        date_created = datetime.utcnow -> DateTime

        Example:
            >>> new_data = geocode_table(name="your_address",
                                            longitude=42.024012,
                                            latitude=38.75919,
                                            distance=118.05)

    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    distance = db.Column(db.Float)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<geocode_table %r>' % self.id
