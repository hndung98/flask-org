import asyncio
from flask import Blueprint, request

from src.services.user_service import *

user_controller = Blueprint('user_controller', __name__,
                            url_prefix='/api')


@user_controller.get('/users')
async def get():
    # Do something
    res = await get_all_users()
    if not res["is_success"]:
        return {
            "is_success": False,
            "message": res["message"]
        }
    return {
        "is_success": True,
        "data": res["data"]
    }


@user_controller.post('/user')
async def post():
    # Do something
    name = request.form['name']
    email = request.form['email']
    data = {
        'name': name,
        'email': email
    }
    # asyncio.run(save_new_user(data))
    res = await save_new_user(data)
    if not res["is_success"]:
        return {
            "is_success": False,
            "message": res["message"]

        }
    return {
        "is_success": True,
        "message": "completed"
    }
