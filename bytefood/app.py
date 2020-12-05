from flask import Flask
from bytefood.ext import site
from bytefood.ext import config
from bytefood.ext import toolbar
from bytefood.ext import db
from bytefood.ext import migrate
from bytefood.ext import cli
from bytefood.ext import hooks
from bytefood.ext import auth


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    auth.init_app(app)
    migrate.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    hooks.init_app(app)
    return app
