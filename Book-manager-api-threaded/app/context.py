
from app.repository import Repository
from app.application.book_service import BookService
from app.infra.storage.SQLite_storage import SQLite_storage
class Context:
    def __init__(self):
        book_storage = SQLite_storage()
        self.book_repository = Repository(book_storage)
        self.book_service = BookService(self.book_repository)


def get_context(app):
    return app.config["CONTEXT"]
