from flask import Blueprint

from src.services.user_service import *

user_controller = Blueprint('user_controller', __name__,
                            url_prefix='/api')


@user_controller.get('/users')
def get():
    # Do something
    res = get_all_users()
    return res


@user_controller.post('/user')
def post(data):
    # Do something
    res = save_new_user(data)
    return res
