from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "ef322fmewfimsfeoefofdswf3o4jfemds"

app.config.from_object(__name__)
from app import views
