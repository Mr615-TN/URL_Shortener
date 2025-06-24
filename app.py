from flask import Flask
from extensions import db
from config import Config
import logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)

    # Configure logging
    if not app.debug:
        logging.basicConfig(level=logging.INFO)
    app.logger.setLevel(logging.INFO)

    # Register blueprints
    from routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app 

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
