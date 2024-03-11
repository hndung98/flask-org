from flask import Blueprint, render_template

settings = Blueprint('settings', __name__,
                     url_prefix='/settings',
                     template_folder='../templates/settings')

@settings.route('/')
def default():
    # Do something
    return render_template('security.html')
