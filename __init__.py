from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
# Initializing application
app = Flask(__name__)


from app import views,

# Initializing application
app = Flask(__name__,instance_relative_config = True)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile("config.py")

# Initializing Flask Extensions
bootstrap = Bootstrap(app)
db = SQLAlchemy()