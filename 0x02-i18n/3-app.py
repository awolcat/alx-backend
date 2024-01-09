#!/usr/bin/env python3
"""Simple Flask Application
"""
from flask import Flask, render_template, request
from flask_babel import Babel
Config = __import__('config').Config

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
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel = Babel(app, locale_selector=get_locale)

@app.route('/')
def hello():
    """Simple route
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
