import app.uuu

#from app.book_repository import InterficeRepository

from app.uuu import Book

class Repository():
    def __init__(self, storage):
        self.storage = storage

    def add(self, book: Book) -> int:
        return self.storage.add(book)

    def delete(self, id: int) -> None:
        self.storage.delete(id)

    def get(self) -> list:
        return self.storage.get()
