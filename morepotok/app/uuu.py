
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import func
db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    genre_id=db.Column(db.Integer,db.ForeignKey("genre.id",ondelete="SET NULL"))
    genre=relationship("Genre",back_populates="books")
    is_read = db.Column(db.Boolean, default=False)

    added = db.Column(db.DateTime, nullable=False, default=func.now())
    def __repr__(self):
        return f'<Book {self.name}>'
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    books=relationship("Book",back_populates="genre")

    def __repr__(self):
        return f'<Genre {self.name}>'