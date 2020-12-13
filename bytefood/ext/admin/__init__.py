from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from bytefood.ext.db import db
from bytefood.ext.db.models import Category

admin = Admin()


def init_app(app):
    admin.name = app.config.get("ADMIN_NAME", "Bytefood")
    admin.template_mode = app.config.get("ADMIN_TEMPLATE_MODE", "bootstrap2")
    admin.init_app(app)

    # TODO: Proteger com senha
    # TODO: Traduzir para PTBR

    admin.add_view(ModelView(Category, db.session))
