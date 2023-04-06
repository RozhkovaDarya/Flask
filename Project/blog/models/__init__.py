from flask_sqlalchemy import SQLAlchemy
from blog.models.user import User

__all__ = [
    "User",
]

db = SQLAlchemy()

__all__ = [
    "db",
]
