import os
from flask import Flask
from .config import Config
from .db import db
from .models import Constellation

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True,
                static_folder='static', template_folder='templates')

    app.config.from_object(Config)
    if test_config:
        app.config.update(test_config)

    # Ensure instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    # Init DB
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Blueprints
    from .routes.home import bp as home_bp
    from .routes.generate import bp as gen_bp
    from .routes.api import bp as api_bp
    from .routes.game import bp as game_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(gen_bp, url_prefix="/generate")
    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(game_bp, url_prefix="/game")

    return app
