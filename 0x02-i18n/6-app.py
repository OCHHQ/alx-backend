from flask import Flask, request, g, render_template
from flask_babel import Babel, gettext as _

app = Flask(__name__)

# List of supported locales
SUPPORTED_LOCALES = ['en', 'fr', 'es']
DEFAULT_LOCALE = 'en'

LOCALE_MAPPING = {
    '1': 'en',
    '2': 'fr',
    # Add more mappings as needed
}

app.config['BABEL_DEFAULT_LOCALE'] = DEFAULT_LOCALE
babel = Babel(app)


# Function to determine the best locale
@babel.localeselector
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
    locale = request.args.get('locale')
    if locale and locale in SUPPORTED_LOCALES:
        return locale

    # 2. Get locale from user settings
    login_as = request.args.get('login_as')
    if login_as:
        locale = LOCALE_MAPPING.get(login_as)

    # 3. Get locale from user settings (in case the user is logged in)
    if hasattr(g, 'user') and g.user and 'locale' in g.user:
        locale = g.user['locale']

    # 4. Get locale from request header
    if not locale:
        header_locale = request.headers.get('Accept-Language')
        if header_locale:
            locale = request.accept_languages.best_match(SUPPORTED_LOCALES)

    # 5. Use default locale if nothing matches
    return locale or DEFAULT_LOCALE


@app.route('/')
def index():
    # Example user data, typically set after login
    g.user = {'name': 'John Doe', 'locale': 'en'}

    # The _ function is already provided by Babel
    return render_template(
            '6-index.html', locale=g.user['locale'],
            name=g.user['name'])


if __name__ == "__main__":
    app.run(debug=True)
