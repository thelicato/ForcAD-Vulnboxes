# Flask modules
from flask import Flask


def create_app(debug: bool = False):
    # Create the Flask application instance
    app = Flask(__name__)

    # Set current_app context
    app.app_context().push()

    from app.config import ApplicationConfig
    app.config.from_object(ApplicationConfig)

    # Initialize extensions
    from app.extensions import cors, bcrypt, server_session

    server_session.init_app(app)
    cors.init_app(app, resources={r"*": {"origins": "*"}}, support_credentials=True)
    bcrypt.init_app(app)

    # Import all models and Create database tables
    from app.db import database, User, Coupon, Product

    database.connect()
    database.create_tables([User, Coupon, Product])

    # Register blueprints or routes
    from app.routes import rest_api

    app.register_blueprint(rest_api)

    return app
