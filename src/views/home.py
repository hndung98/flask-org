from flask import Blueprint, render_template

home = Blueprint('home', __name__,
                 url_prefix='/app',
                 template_folder='../templates/home')

@home.route('/')
def default():
    # Do something
    return render_template('index.html')
