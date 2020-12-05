from bytefood.ext.auth import models  # noqa
from bytefood.ext.auth.commands import add_user, list_users


def init_app(app):
    """TODO: inicializar Flask Simple Login + JWT"""
    app.cli.command()(list_users)
    app.cli.command()(add_user)
