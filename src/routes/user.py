import asyncio
from flask import request
from flask_restx import Namespace, Resource, fields

from src.services.user import *

user_namespace = Namespace('user_namespace', 'user service related endpoints', path="/api/user")

wild = fields.Wildcard(fields.String)
get_user_model = user_namespace.model('get_user_model', {
    'is_success': fields.String(
        description='name message'
    ),
    'data': wild
    ,
    'message': fields.String(
        description='email message'
    )
})
post_user_model = user_namespace.model('post_user_model', {
    'is_success': fields.String(
        description='name message'
    ),
    'message': fields.String(
        description='email message'
    )
})

get_user_example = {'message': 'user service!'}

post_parser = user_namespace.parser()
post_parser.add_argument('name', required=True, type=str, help='name of user', location='form')
post_parser.add_argument('email', required=True, type=str, help='email of user', location='form')

@user_namespace.route('/')
class User(Resource):
    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    @user_namespace.response(500, 'Internal Server error')
    def get(self):
        '''get user message endpoint'''
        return self.loop.run_until_complete(get_all_users())
    
    @user_namespace.expect(post_parser)
    @user_namespace.response(500, 'Internal Server error')
    def post(self):
        '''post user message endpoint'''
        name = request.form['name']
        email = request.form['email']
        data = {
            'name': name,
            'email': email
        }
        return self.loop.run_until_complete(save_new_user(data))
