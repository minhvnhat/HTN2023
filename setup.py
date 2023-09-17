from extensions import db
from flask import current_app
import click

from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
    pass

def init_db():
    db.create_all()


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')