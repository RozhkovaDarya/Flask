from flask_sqlalchemy import SQLAlchemy
from blog.models.user import User
from blog.models.author import Author

__all__ = [
    "User",
]

db = SQLAlchemy()

__all__ = [
    "db",
]
