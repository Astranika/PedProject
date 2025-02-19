
import time
from flask import Blueprint, current_app, request,render_template,redirect, url_for,jsonify
from app.uuu import db
from app.context import get_context
from app.uuu import Book,Genre
import threading

bp = Blueprint("book", __name__)
book_deletion_semaphore = threading.Semaphore(value=2)

@bp.route("/")
def all_books():
    print("ЗАПУСТИЛОСЬ")
    ctx = get_context(current_app)
    #books = Book.query.order_by(Book.added.desc()).limit(15).all()
    bok=db.session.query(Book).order_by(Book.added.desc()).limit(15).all()
    print("8888888888888888 ",bok)
    #return json.dumps([b.to_dict() for b in ctx.book_service.get()],ensure_ascii=False)
    return render_template("all_books.html", books=bok)


@bp.route("/update_book/", methods=["POST"])
def update_book():
    book_id = request.form.get("book_id")
    if book_id:
        book = Book.query.get(book_id)
        if book:
            checkbox_value = request.form.get(f"book_{book.id}_is_read")
            if checkbox_value == "on":  # Если галочка была поставлена
                book.is_read = True
            else:
                book.is_read = False
            db.session.commit()
            return jsonify({
                "success": True,
                "book_id": book.id,
                "is_read": book.is_read
            })

    #return redirect(url_for('book.all_books'))


@bp.route("/genre/<int:genre_id>")
def books_by_genre(genre_id):
    genre=Genre.query.get_or_404(genre_id)
    #genre.books
    t=genre.books
    print("99999999  ",t)
    for book in t:
        print(book.id)
    return render_template("books_by_genre.html",department_name=genre.name,books=t)

@bp.route("/", methods=["POST"])
def add_book():
    print("pfgecr ADD")
    new_book_name = request.form.get("Q")
    new_book_genre = request.form.get("G")

    genre_name = new_book_genre
    genre = Genre.query.filter_by(name=genre_name).first()

    if not genre:
        genre = Genre(name=genre_name)

    if request.form.get("W") == "W":
        db.session.add(Book(name=f" {new_book_name}", genre=genre))
        db.session.commit()
    return redirect(url_for('book.all_books'))

@bp.route("/delete_book/<int:id>", methods=["POST"])
def delete_book(id):
    print("ЗАПУСТИЛСЯ ДЕЛ")
    book_deletion_semaphore.acquire()
    try:
        book = Book.query.get_or_404(id)
        time.sleep(5)
        db.session.delete(book)
        db.session.commit()
        return jsonify({"success": True})
    finally:
        book_deletion_semaphore.release()
@bp.route("/book/<int:id>")
def book_detail(id):
    book = Book.query.get_or_404(id)
    return render_template("book_detail.html", book=book)
