from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from website_project.config import Config
from website_project.models import User, Product, Order
from website_project.utils.database import db_session

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

from website_project import routes