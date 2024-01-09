#!/usr/bin/env python3
"""Simple Flask Application
"""
import flask
import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel
from datetime import datetime


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Flask app config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    """Get user locale
    """
    if ('locale' in request.args
    and request.args['locale'] in app.config['LANGUAGES']):
        return request.args['locale']
    elif (g.user and g.user.get('locale')
    and g.user.get('locale') in app.config['LANGUAGES']):
        return g.user.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_timezone():
    """Get user timezone
    """
    if 'timezone' in request.args:
        tz = request.args['timezone']
        # print(tz)
    elif g.user and g.user.get('timezone'):
        tz = g.user.get('timezone')
        # print(tz)
    else:
        tz = None
    try:
        pytz.timezone(tz)
        return tz
    except Exception:
        return None

    
babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


def get_user():
    """Get current user
    """
    user_id = request.args.get('login_as', None)
    if user_id:
        return users.get(int(user_id), None)
    return None


@app.before_request
def before_request():
    """Get user before any other request processing
    """
    flask.g.user = get_user()


@app.route('/')
def hello():
    """Simple route
    """
    time = datetime.utcnow()
    return render_template('7-index.html', time=time)


if __name__ == '__main__':
    app.run(debug=True)
