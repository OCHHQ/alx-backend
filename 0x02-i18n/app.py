#!/usr/bin/env python3
"""
Flask application module for internationalization support.
This module implements a Flask web application with Babel integration
for handling multiple languages and timezones.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from datetime import datetime
import pytz
from babel.dates import format_datetime
from typing import Dict, Union

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration class for Flask application.
    Defines language and timezone settings for the application.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    Retrieve user dictionary based on URL parameters.
    Returns:
        Dict: User dictionary if ID exists in users
        None: If user ID doesn't exist or no login_as parameter
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """
    Execute before all requests.
    Sets user as global on flask.g.user.
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for supported languages.
    Returns:
        str: Best matching locale based on priority order:
             1. URL parameters
             2. User settings
             3. Request header
             4. Default locale
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Determine the appropriate timezone for the user.
    Returns:
        str: Timezone string based on priority order:
             1. URL parameters
             2. User settings
             3. Default timezone
    """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user and g.user['timezone']:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.context_processor
def utility_processor() -> Dict:
    """
    Make utility functions available to templates.
    Returns:
        Dict: Dictionary containing utility functions
    """
    return {
        'get_locale': get_locale,
        'get_timezone': get_timezone
    }


@app.route('/')
def index() -> str:
    """
    Render the homepage of the application.
    Returns:
        str: Rendered HTML template with formatted current time
    """
    timezone = pytz.timezone(get_timezone())
    current_time = datetime.now(timezone)
    formatted_time = format_datetime(current_time, locale=get_locale())
    return render_template('index.html', current_time=formatted_time)


if __name__ == "__main__":
    app.run(debug=True)
