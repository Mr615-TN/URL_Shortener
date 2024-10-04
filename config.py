import os 
class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///urlshort.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False