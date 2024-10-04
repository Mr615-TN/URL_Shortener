from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from config import Config
import logging
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    #TODO figure out why logging isn't working
    app.logger.setLevel(logging.INFO)

    from routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app 

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)

