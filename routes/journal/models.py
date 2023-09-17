from dataclasses import dataclass

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime

from extensions import db

@dataclass
class User(db.Model):
    uid: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

@dataclass
class Journal(db.Model):
    uid: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime.datetime] = mapped_column(db.Date, primary_key=True)
    prompt: Mapped[str] = mapped_column(String())
    message: Mapped[str] = mapped_column(String())

@dataclass
class Mood(db.Model):
    uid: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime.datetime] = mapped_column(db.Date, primary_key=True)
    score: Mapped[int] = mapped_column()
    is_day: Mapped[bool] = mapped_column(primary_key=True)
