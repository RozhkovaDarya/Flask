from flask_sqlalchemy import SQLAlchemy
from blog.models.user import User
from blog.models.author import Author
from blog.models.article import Article

__all__ = [
    "User",
    "Author",
    "Article",
]

db = SQLAlchemy()

__all__ = [
    "db",
]
