#!/usr/bin/env python3
"This is a line of text"
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    "This is a line of text"
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
Babel.default_locale = "en"
Babel.default_timezone = "UTC"

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    "This is a line of text"
    locale = request.args.get("locale")
    if locale:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


def get_user():
    "This is a line of text"
    try:
        user = request.args.get("login_as")
        return users[int(user)]
    except Exception:
        return None


@app.before_request
def before_request():
    "This is a line of text"
    user = get_user()
    g.user = user


@app.route("/", methods=["GET"])
def index():
    "This is a line of text"
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
