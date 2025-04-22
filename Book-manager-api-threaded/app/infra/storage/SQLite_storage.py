#from domain.book import Book
from app.uuu import db
from app.uuu import Book
class SQLite_storage:
    def __init__(self):
        self.books = [] # теперь сохраняю не в список а через сессию к базеданных

    def add(self, book):
        db.session.add(book)
        db.session.commit()
        #self.books.append(book)
        return book.id

    def delete(self, id):
        book = db.session.query(Book).get(id)
        if book:
            db.session.delete(book)
            db.session.commit()
    
    def get(self):
        return db.session.query(Book).all()
