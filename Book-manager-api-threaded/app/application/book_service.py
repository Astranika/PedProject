class BookService:
    def __init__(self, repository):
        self.repository = repository

    def add(self, book):
        return self.repository.add(book)

    def delete(self, id):
        self.repository.delete(id)

    def get(self):
        return self.repository.get()
