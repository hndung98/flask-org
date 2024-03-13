import asyncio
from flask import Blueprint, request
from flask_restx import Api, Namespace, Resource, fields

from src.services.user_service import *

user_namespace = Namespace('user_namespace', 'user service related endpoints')

get_user_model = user_namespace.model('User', {
    'is_success': fields.String(
        description='name message'
    ),
    'message': fields.String(
        description='email message'
    )
})
post_user_model = user_namespace.model('User', {
    'is_success': fields.String(
        description='name message'
    ),
    'message': fields.String(
        description='email message'
    )
})

get_user_example = {'message': 'user service!'}

@user_namespace.route('/user')
class User(Resource):
    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    @user_namespace.response(500, 'Internal Server error')
    def get(self):
        '''get user message endpoint'''
        return self.loop.run_until_complete(self.async_get())
    
    async def async_get(self):
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
    
    @user_namespace.response(500, 'Internal Server error')
    def post(self):
        '''post user message endpoint'''
        return self.loop.run_until_complete(self.async_post())
    
    async def async_post(self):
        # Do something
        name = request.form['name']
        email = request.form['email']
        data = {
            'name': name,
            'email': email
        }
        
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

user_controller = Blueprint('user_controller', __name__,
                            url_prefix='/api')

# api_extension = Api(
#     user_controller,
#     title='Flask RESTplus Demo',
#     version='1.0',
#     description='Application tutorial to demonstrate Flask RESTplus extension\
#         for better project structure and auto generated documentation',
#     doc='/doc'
# )

# api_extension.add_namespace(user_namespace)

# @user_controller.get('/users')
# async def get():
#     # Do something
#     res = await get_all_users()
#     if not res["is_success"]:
#         return {
#             "is_success": False,
#             "message": res["message"]
#         }
#     return {
#         "is_success": True,
#         "data": res["data"]
#     }


# @user_controller.post('/user')
# async def post():
#     # Do something
#     name = request.form['name']
#     email = request.form['email']
#     data = {
#         'name': name,
#         'email': email
#     }
#     # asyncio.run(save_new_user(data))
#     res = await save_new_user(data)
#     if not res["is_success"]:
#         return {
#             "is_success": False,
#             "message": res["message"]

#         }
#     return {
#         "is_success": True,
#         "message": "completed"
#     }
