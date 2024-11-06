from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')# Set the secret key using env. If not found, use default

  with app.app_context():
    from . import routes # Importing routes after setting up the app context ensures that the routes are properly associated with the Flask application instance.
  

  app.register_blueprint(routes.main) # Registering the blueprint to make it accessible from the app object. This allows us to use the routes defined in the main module within our Flask application.

  return app