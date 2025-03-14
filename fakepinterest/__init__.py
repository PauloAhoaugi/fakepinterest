from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://banco_fakepinterest_jbrq_user:XZXwfcLaj5h4wRDk117T8NwIL87GKhQA@dpg-cva33utumphs73adigfg-a.oregon-postgres.render.com/banco_fakepinterest_jbrq"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SECRET_KEY"] = "3c7a3c7127025d810a4a4145da0535b4"
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"


database = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

login_manager.login_view = "homepage"

from  fakepinterest import routes