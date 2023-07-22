from flask import Flask
from app.blueprints import blueprints
from app import extensions

def create_app(config_file='config.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    # register blueprints 
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    extensions.db.init_app(app)

    return app