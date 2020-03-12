from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = "ef322fmewfimsfeoefofdswf3o4jfemds"
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:1234@localhost/profiles"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

app.config.from_object(__name__)

from app import views
