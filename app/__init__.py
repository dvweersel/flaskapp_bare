from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from .views.main.main import main
# from .config import *
# from .extensions import *


def create_app():
    app = Flask(__name__)

    register_blueprints(app)

    return app


def register_blueprints(app):
    app.register_blueprint(main)
