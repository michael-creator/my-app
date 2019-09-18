from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

def create_app():
    # Initializing applicationem
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'MYKEYISKEY'
    app.config['SQLAlchemy_DATABASE_uri'] = 'sqlite:///db.sqlite'
    # Initializing application
    app = Flask(__name__,instance_relative_config = True)

    # Setting up configuration
    app.config.from_object(DevConfig)
    app.config.from_pyfile("config.py")

    # Initializing Flask Extensions
    bootstrap = Bootstrap(app)
    db = SQLAlchemy()
    db.init_app(app) 


    from .auth import auth

    app.register_blueprint(auth_blueprint)
    from .main import main
    app.register_blueprint(main_blueprint)
