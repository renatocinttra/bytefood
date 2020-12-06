from bytefood.ext.admin import admin as base_admin
from bytefood.ext.auth import models  # noqa
from bytefood.ext.auth.admin import UserAdmin
from bytefood.ext.auth.commands import add_user, list_users
from bytefood.ext.auth.models import User
from bytefood.ext.db import db


def init_app(app):
    """TODO: inicializar Flask Simple Login + JWT"""
    app.cli.command()(list_users)
    app.cli.command()(add_user)

    base_admin.add_view(UserAdmin(User, db.session))
