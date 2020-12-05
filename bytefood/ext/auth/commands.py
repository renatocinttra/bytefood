import click
from bytefood.ext.db import db
from bytefood.ext.auth.models import User


def list_users():
    users = User.query.all()
    click.echo(f"lista de usuarios {users}")


@click.option("--email", "-e")
@click.option("--passwd", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
def add_user(email, passwd, admin):
    """adiciona novo usuario"""
    user = User(
        email=email,
        passwd=passwd,
        admin=admin
    )
    db.session.add(user)
    db.session.commit()

    click.echo(f"User {email} create with sucessfull!")
