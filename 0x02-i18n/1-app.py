#!/usr/bin/env python3
"""Basic Flask application with Babel support."""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Configuration class.

    Attributes:
        LANGUAGES (list): List of available languages.
        BABEL_DEFAULT_LOCALE (str): Default locale.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


babel = Babel()


def create_app():
    """
    Creates a Flask application instance.

    Returns:
        Flask: Application instance.
    """
    app = Flask(__name__)
    app.config.from_object(Config)
    babel.init_app(app)

    @app.route('/')
    def index():
        """
        Index route.

        Returns:
            str: Rendered HTML template.
        """
        return render_template('1-index.html')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
