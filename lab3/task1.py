class Book:
    """Base class for Book
    
    Usage:
    >>> b1 = Book("Onegin", "Pushkin")

    >>> b2 = Book(1984, "Orwell")
    Traceback (most recent call last):
    ...
    TypeError: Name must be a string

    >>> b3 = Book("Orwell", 1984)
    Traceback (most recent call last):
    ...
    TypeError: Author must be a string

    >>> b1.name = "aboba"
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute 'name'
    """

    def __init__(self, name: str, author: str):
        self._name = None
        self._author = None
        self.init_name(name)
        self.init_author(author)

    def init_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self._name = name

    def init_author(self, author: str):
        if not isinstance(author, str):
            raise TypeError("Author must be a string")
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}," \
               f"author={self.author!r})"


class PaperBook(Book):
    """Class for a paper book

    Usage:
    >>> b1 = PaperBook("Onegin", "Pushkin", 200)

    >>> b2 = PaperBook("Onegin", "Pushkin", -100)
    Traceback (most recent call last):
    ...
    ValueError: Pages must be a positive integer

    >>> b3 = PaperBook("1984", "Orwell", 200.5)
    Traceback (most recent call last):
    ...
    TypeError: Pages must be an integer
    """

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Pages must be an integer")
        if pages <= 0:
            raise ValueError("Pages must be a positive integer")
        self._pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}," \
               f"author={self._author!r}, pages={self._pages})"


class AudioBook(Book):
    """Class for an audiobook

    Usage:
    >>> b1 = AudioBook("Onegin", "Pushkin", 12.5)

    >>> b2 = AudioBook("Onegin", "Pushkin", 0.)
    Traceback (most recent call last):
    ...
    ValueError: Duration must be a positive float
    """

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float):
        if not isinstance(duration, float):
            raise TypeError("Duration must be a float")
        if duration <= 0:
            raise ValueError("Duration must be a positive float")
        self._duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}," \
               f"author={self._author!r}, duration={self._duration})"


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
