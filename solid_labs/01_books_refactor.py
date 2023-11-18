from typing import List, Optional


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f"{self.title} by {self.author} with {self.page}"


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find_book(self, title: str) -> Optional[Book]:
        try:
            book = [b for b in self.books if b.title.lower() == title.lower()][0]
            return book
        except IndexError:
            return None

book = Book("Title1", "Test")
book2 = Book("Title2", "Tes2")

library = Library()
print(library.books)
library.add_book(book)
print(library.books)
