import os
from flask import Flask
from app.context import Context
from app.views.book import bp as book_bp
from app.uuu import db
from app.uuu import Book,Genre

def create_app():
    app = Flask(__name__)
    app.register_blueprint(book_bp, url_prefix="/books")
    app.config["CONTEXT"] = Context()
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
    db.init_app(app)
    return app

app = create_app()


with app.app_context():
    #db.drop_all()
    db.create_all()

    genre_name = "наука"
    genre = Genre.query.filter_by(name=genre_name).first()

    # Если жанра нет, создаем новый
    if not genre:
        genre = Genre(name=genre_name)
        db.session.add(genre)
    genre_name = "фантастика"
    genre2 = Genre.query.filter_by(name=genre_name).first()

    # Если жанра нет, создаем новый
    if not genre2:
        genre2 = Genre(name=genre_name)
        db.session.add(genre2)


    for i in range(4):
        if i%2==0:
            db.session.add(Book(name=f"трактат {i}", genre=genre))
        else:
            db.session.add(Book(name=f"сказка {i}", genre=genre2))
    db.session.commit()
if __name__ == "__main__":
    app.run(debug=True)