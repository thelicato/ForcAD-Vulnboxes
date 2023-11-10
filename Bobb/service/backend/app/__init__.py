import os
# Flask modules
from flask import Flask


def create_app(debug: bool = False):
    FLASK_ENV = os.environ.get("FLASK_ENV", 'development')
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

    from app.products import init_products
    init_products()

    # Register blueprints or routes
    from app.routes import rest_api

    if FLASK_ENV == 'production':
        print("Serving UI")
        from app.ui import ui
        app.register_blueprint(ui)

    app.register_blueprint(rest_api)

    return app
