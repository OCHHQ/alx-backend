#!/usr/bin/env python3
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _

app = Flask(__name__)

class Config:
    """Configuration for Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
babel = Babel(app)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """Get the user from the mock database."""
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None

@app.before_request
def before_request():
    """Set the user in the global context before each request."""
    g.user = get_user()

@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages."""
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """Render the homepage with a welcome message."""
    return render_template('5-index.html')

if __name__ == '__main__':
    app.run(debug=True)