#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _

app = Flask(__name__)

class Config:
    """Configuration for Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages."""
    # Check if a 'locale' parameter was passed in the URL
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    # If not, try to guess the best match based on the accept headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """Render the homepage with translated messages."""
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run(debug=True)
