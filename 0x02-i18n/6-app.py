from flask import Flask, request, g, render_template
from babel.support import Locale, gettext
from babel.core import UnknownLocaleError
import os

app = Flask(__name__)

# List of supported locales
SUPPORTED_LOCALES = ['en', 'fr', 'es']
DEFAULT_LOCALE = 'en'

LOCALE_MAPPING = {
    '1': 'en',
    '2': 'fr',
    # Add more mappings as needed
}

def get_locale():
    """
    Determine the user's preferred locale based on the following priority:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale

    Returns:
        str: The user's preferred locale
    """
    # 1. Get locale from URL parameters
    login_as = request.args.get('login_as')
    locale = LOCALE_MAPPING.get(login_as)

    # 2. Get locale from user settings
    if hasattr(g, 'user') and g.user and 'locale' in g.user:
        locale = g.user['locale']

    # 3. Get locale from request header
    if not locale:
        header_locale = request.headers.get('Accept-Language')
        if header_locale:
            # Parse the header and find the best match
            header_locales = header_locale.split(',')
            for header_locale in header_locales:
                try:
                    locale = Locale.parse(header_locale).language
                    if locale in SUPPORTED_LOCALES:
                        break
                except (ValueError, UnknownLocaleError):
                    pass

    # 4. Use default locale
    return locale or DEFAULT_LOCALE

@app.route('/')
def index():
    g.user = {'name': 'John Doe', 'locale': 'en'}  # Example user data
    locale = get_locale()

    # Set the gettext function to use the detected locale
    _ = lambda s: gettext(s, locale=locale)

    return render_template('6-index.html', locale=locale, name=g.user['name'], _=_)


if __name__ == "__main__":
    app.run(debug=True)
