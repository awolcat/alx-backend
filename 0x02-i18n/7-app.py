#!/usr/bin/env python3
"""A simple flask app
"""


import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel
from datetime import datetime


class Config(object):
    """Flask App Config
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# configure the flask app
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Mock getting uer session
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """Runs before request
    """
    user = get_user()
    g.user = user


def get_locale():
    """Get user locale
    """
    locale = request.args.get('locale')
    if locale is None:
        locale = g.user.get('locale')

    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone():
    """Get user timezone
    """
    if request.args.get('timezone'):
        tz = request.args.get('timezone')
    elif g.user and g.user.get('timezone'):
        tz = g.user.get('timezone')
    else:
        tz = None
    try:
        pytz.timezone(tz)
        return tz
    except Exception:
        return None

babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route('/')
def hello():
    """Simple route
    """
    time = datetime.utcnow()
    return render_template('7-index.html', time=time)


if __name__ == '__main__':
    app.run(debug=True)
