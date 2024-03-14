from flask import Flask
from flask_restx import Api, Resource

from src.routes.base import login_namespace
from src.routes.user import user_namespace

from src.views.admin import admin
from src.views.home import home
from src.views.profile import profile
from src.views.settings import settings

app = Flask(__name__)
app.config['RESTX_MASK_SWAGGER'] = False

api = Api(app,
          version='1.0',
          title="Flask API with JWT-Based Authentication",
          description="Welcome to the Swagger UI documentation site!",
          doc="/ui",
          )

# add routes
api.add_namespace(login_namespace)
api.add_namespace(user_namespace)

# api
# app.register_blueprint(auth_controller)
# app.register_blueprint(user_controller)

# views
app.register_blueprint(admin)
app.register_blueprint(home)
app.register_blueprint(profile)
app.register_blueprint(settings)
