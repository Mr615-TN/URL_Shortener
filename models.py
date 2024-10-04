from app import db 
import random
import string

class URL(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    original_url = db.Column(db.String(500), nullable = False)
    short_url = db.Column(db.String(6), unique = True, nullable = False)

    @staticmethod
    def generate_shortUrl():
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(6))
