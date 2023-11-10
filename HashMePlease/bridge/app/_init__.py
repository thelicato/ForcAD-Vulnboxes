import os
# Flask modules
from flask import Flask


def create_app(debug: bool = False):
    # Create the Flask application instance
    app = Flask(__name__)

    # Initialize extensions
    from app.extensions import cors

    cors.init_app(app, resources={r"*": {"origins": "*"}}, support_credentials=True)

    # Register blueprints or routes
    from app.routes import rest_api

    app.register_blueprint(rest_api)

    return app
