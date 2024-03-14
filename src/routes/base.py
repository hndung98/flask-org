import asyncio
from flask import request
from flask_restx import Namespace, Resource, fields

from src.services.base import *

login_namespace = Namespace('login_namespace', 'login service related endpoints', path="/api/v1/login")

login_parser = login_namespace.parser()
login_parser.add_argument('name', required=True, type=str, help='name of user', location='form')
login_parser.add_argument('email', required=True, type=str, help='email of user', location='form')

@login_namespace.route('/')
class User(Resource):
    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
    
    @login_namespace.expect(login_parser)
    @login_namespace.response(500, 'Internal Server error')
    def post(self):
        '''login message endpoint'''
        name = request.form['name']
        email = request.form['email']
        data = {
            'name': name,
            'email': email
        }
        return self.loop.run_until_complete(async_sign_in(data))
