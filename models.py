from flask_sqlalchemy import SQLAlchemy
import random
import string

# Import db from app module when needed, not at module level
db = None

class URL:
    def __init__(self, db_instance):
        global db
        db = db_instance
        
        class URLModel(db.Model):
            __tablename__ = 'url'
            id = db.Column(db.Integer, primary_key=True)
            original_url = db.Column(db.String(500), nullable=False)
            short_url = db.Column(db.String(6), unique=True, nullable=False)

            @staticmethod
            def generate_shortUrl():
                characters = string.ascii_letters + string.digits
                return ''.join(random.choice(characters) for _ in range(6))
        
        self.Model = URLModel
        return URLModel

# Better approach - revised models.py
from flask_sqlalchemy import SQLAlchemy
import random
import string

# This will be initialized in app.py
db = SQLAlchemy()

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(6), unique=True, nullable=False)

    @staticmethod
    def generate_shortUrl():
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(6))
