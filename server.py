from flask import Flask
from flask_login import LoginManager, current_user, login_user, login_required
app = Flask(__name__)
app.config["SECRET_KEY"] = "Highly secret key"
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
