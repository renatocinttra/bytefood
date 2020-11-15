from flask import Flask
from bytefood.ext import site
from bytefood.ext import config
from bytefood.ext import toolbar
from bytefood.ext import db
from bytefood.ext import cli


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app
