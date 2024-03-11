from flask import Blueprint

from src.services.auth_service import *

auth_controller = Blueprint('auth_controller', __name__,
                            url_prefix='/api')


@auth_controller.post('/sign-in')
def post():
    res = sign_in()
    return res
