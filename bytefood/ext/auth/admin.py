from flask_admin.contrib.sqla import ModelView, filters
from flask_admin.actions import action
from bytefood.ext.auth.models import User
from bytefood.ext.db import db
from flask import flash


def format_user(self, request, user, *args):
    return user.email.split("@")[0]

# TODO: descrever todos os models


class UserAdmin(ModelView):
    """Interface"""
    column_formatters = {
        "email": format_user
        # "email: lambda s, r, u, a: u.email.split("@")[0]"
    }
    column_list = ["email", "admin"]
    column_searchable_list = ["email"]
    column_filters = [
        "email",
        "admin",
        filters.FilterLike(
            User.email,
            "Dominio",
            options=(("gmail", "Gmail"), ("uol", "Uol"))
        )
    ]

    can_edit = False
    can_create = True
    can_delete = True

    @action(
        'toggle_admin',
        'Toggle Admin Status',
        'Are you sure?'
    )
    def toggle_admin_status(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        for user in users:
            user.admin = not user.admin
        db.session.commit()
        flash(f"{len(users)} usuários alterados com sucesso!", "success")

    @action(
        'send_email',
        'Send email to all users',
        'Are you sure?'
    )
    def send_email(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        # Redirect para um form para escrever a mensagem de email
        # enviar o email
        flash(f"{len(users)} email enviados.", "success")
