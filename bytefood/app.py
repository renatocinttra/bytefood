from flask import Flask
from bytefood.ext import site
from bytefood.ext import config
from bytefood.ext import toolbar


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app
