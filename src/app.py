from flask import Flask

from src.controllers.auth_controller import auth_controller
from src.controllers.user_controller import user_controller

from src.views.admin import admin
from src.views.home import home
from src.views.profile import profile
from src.views.settings import settings

app = Flask(__name__)

# api
app.register_blueprint(auth_controller)
app.register_blueprint(user_controller)

# views
app.register_blueprint(admin)
app.register_blueprint(home)
app.register_blueprint(profile)
app.register_blueprint(settings)
