#!/usr/bin/env python3
"This is a line of text"
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    "This is a line of text"
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
Babel.default_locale = "en"
Babel.default_timezone = "UTC"


@babel.localeselector
def get_locale():
    "This is a line of text"
    locale = request.args.get("locale")
    if locale:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/", methods=["GET"])
def index():
    "This is a line of text"
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
