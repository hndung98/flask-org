from flask import Blueprint, render_template

profile = Blueprint('profile', __name__,
                    url_prefix='/<user_url_slug>',
                    template_folder='../templates/profile')

@profile.route('/')
def default(user_url_slug):
    # Do something
    lst_username = ["hnd", "hd", "dung"]
    if user_url_slug in lst_username:
        return render_template('about.html', username=user_url_slug)
    return render_template('not_found.html')

@profile.route('/timeline')
def timeline(user_url_slug):
    # Do something
    print(user_url_slug)
    return render_template('timeline.html')

@profile.route('/photos')
def photos(user_url_slug):
    # Do something
    return render_template('photos.html')
