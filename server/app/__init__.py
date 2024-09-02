from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register blueprints/routes
    from .routes.item_routes import item_bp
    app.register_blueprint(item_bp)
    
    return app
