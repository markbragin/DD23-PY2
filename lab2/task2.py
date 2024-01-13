BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    },
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError("id_ must be an integer")
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(pages, int):
            raise TypeError("pages must be an integer")

        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    def __init__(self, books: list[Book] = []):
        self.books = books

    def get_next_book_id(self):
        return max(self.books, key=lambda b: b.id).id + 1 if self.books else 1

    def get_index_by_book_id(self, book_id: int):
        if not isinstance(book_id, int):
            raise TypeError("book id must be an integer")

        for i, book in enumerate(self.books):
            if book.id == book_id:
                return i
        raise ValueError("No book with this id in the Library")


if __name__ == "__main__":
    empty_library = Library()
    print(empty_library.get_next_book_id())

    list_books = [
        Book(
            id_=book_dict["id"],
            name=book_dict["name"],
            pages=book_dict["pages"],
        )
        for book_dict in BOOKS_DATABASE
    ]

    library_with_books = Library(list_books)
    print(library_with_books.get_next_book_id())
    print(library_with_books.get_index_by_book_id(1))
