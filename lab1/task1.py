from typing import Any


class DeadHumanAction(BaseException):
    pass


class Queue:
    """Simple implementation of a Queue.

    Usage:
    >>> queue = Queue()
    >>> queue.push(1)
    >>> queue.push(2)
    >>> queue.front()
    1
    >>> queue.pop()
    1
    >>> queue.pop()
    2
    >>> queue = Queue()
    >>> queue.pop()
    Traceback (most recent call last):
    ...
    IndexError: Performing pop with an empty queue

    >>> queue.is_empty()
    True
    """

    def __init__(self):
        """Initialization of the object"""
        self._data = []

    @property
    def size(self):
        """Size of the queue"""
        return len(self._data)

    def push(self, value: Any):
        """Pushes the value to the back of the queue.

        Args:
            value: a value to push
        """
        self._data.append(value)

    def pop(self) -> Any:
        """Removes a value from the back of the queue and returns it.

        Returns:
            A value from the back of the queue.

        Raises:
            IndexError: An error while performing pop with an empty queue
        """
        if self.size == 0:
            raise IndexError("Performing pop with an empty queue")
        res = self._data[0]
        self._data = self._data[1:]
        return res

    def front(self) -> Any:
        """Returns a value which is currently at front of the queue.
        Unlike pop this method doesn't remove the value from a queue.

        Returns:
            A value from the top of the queue.

        Raises:
            IndexError: An error while performing pop with an empty queue
        """
        if self.size == 0:
            raise IndexError("Performing pop with an empty queue")
        return self._data[0]

    def is_empty(self) -> bool:
        """Returns true if the queue if empty."""
        return True if self.size == 0 else False


class Human:
    """Simple implementation of a basic human being.

    Usage:
    >>> mark = Human("Mark", 22)
    >>> mark.greet()
    Hi, I am Mark.
    >>> mark.age
    22
    >>> mark.grow_older()
    >>> mark.age
    23
    """

    def __init__(self, name: str, age: int):
        """Initialization.

        Args:
            name: a name of the human
            age: age of the human
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(age, int):
            raise TypeError("Age must be an integer")

        self._name = name
        self._age = age
        self._alive = True

    @property
    def name(self) -> str:
        """Name of the human"""
        return self._name

    @property
    def age(self) -> int:
        """Age of the human"""
        return self._age

    @property
    def alive(self) -> bool:
        """Returns if the human is alive."""
        return self._alive

    def greet(self):
        """Prints greetings to the console.
        >>> man = Human("2Pac", 25)
        >>> man.die()
        >>> man.greet()
        Traceback (most recent call last):
        ...
        DeadHumanAction: Dead human can't speak.
        """
        if not self._alive:
            raise DeadHumanAction("Dead human can't speak.")
        print(f"Hi, I am {self._name}.")

    def grow_older(self):
        """Increases age of the human by 1 year.
        >>> x = Human("Jahseh", 20)
        >>> x.alive
        True
        >>> x.die()
        >>> x.alive
        False
        >>> x.grow_older()
        Traceback (most recent call last):
        ...
        DeadHumanAction: Dead human can't grow older.
        """
        if not self._alive:
            raise DeadHumanAction("Dead human can't grow older.")
        self._age += 1

    def die(self):
        """Kills the human :( ."""
        self._alive = False


class Printer:
    """Full-featured :D implementation of a printer.

    Usage:
    >>> pages = ["line1", "line2", "line3", "line4", "line5"]
    >>> printer = Printer(3)
    >>> printer.print(pages)
    line1
    line2
    line3
    >>> printer.has_ink()
    False
    >>> printer.refill(3)
    >>> new_pages = ["page1", "page2"]
    >>> printer.print(new_pages)
    line4
    line5
    page1
    >>> not_printed = printer.clear()
    >>> not_printed
    ['page2']
    """

    def __init__(self, ink: int):
        """Initialization."""
        if not isinstance(ink, int):
            raise TypeError("Ink must be an integer")
        self._ink = ink
        self._queue = Queue()

    def has_ink(self) -> bool:
        """Returns if there is ink in the printer.

        Returns:
            True if there is ink in the printer otherwise False
        """
        return self._ink > 0

    def print(self, pages: list[str]):
        """Prints pages to the console separated by newline.

        Args:
            pages: pages to print.
        """
        self._push_to_queue(pages)
        for _ in range(self._queue.size):
            if not self.has_ink():
                break
            print(self._queue.pop())
            self._ink -= 1

    def _push_to_queue(self, pages: list[str]):
        """Pushes pages to print to the queue.

        Args:
            pages: pages to push.
        """
        for page in pages:
            self._queue.push(page)

    def clear(self) -> list[str]:
        """Getting rid of the pages in the pinter queue.

        Returns:
            All the pages stacked in the printer queue.
        """
        return [self._queue.pop() for _ in range(self._queue.size)]

    def refill(self, ink: int):
        """Refills printer."""
        if not isinstance(ink, int):
            raise TypeError("Ink must be an integer")
        self._ink += ink


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
