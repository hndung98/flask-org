from flask import Blueprint, render_template

admin = Blueprint('admin', __name__,
                  url_prefix='/app/admin',
                  template_folder='../templates/admin')

@admin.route('/')
def default():
    # Do something
    return render_template('welcome.html')
