"""Kek module for cars.

Typical usage example:

    >>> c = PassengerCar('Lightning', 'Mcqueen', 500)
    >>> c.gas()
    First gear
    Second gear
    Third gear
    'Ka-chow!'
    >>> c.evaluate_cost()
    250000

    >>> cc = Truck('Tesla', 'CyberTruck', 10.)
    >>> cc.gas()
    First gear
    Second gear
    Third gear
    'Ka-chow!'
    >>> cc.evaluate_cost()
    12340
"""


class Car:
    """Base class for car.

    Attributes:
        brand: a string representing a car brand (such as Tesla, Chevrolet, ...)
        model: a string representing a model name (such as Model S, Camaro, ...)
    """

    def __init__(self, brand: str, model: str):
        """Init Car with brand and model."""
        self.brand = brand
        self.model = model

    @property
    def brand(self) -> str:
        """Brand of a car."""
        return self._brand

    @brand.setter
    def brand(self, brand: str):
        """A setter for a brand of a car.

        Raises:
            TypeError: An error occurred when passed argument is not a string.
        """
        if not isinstance(brand, str):
            raise TypeError("Brand must be a string")
        self._brand = brand

    @property
    def model(self) -> str:
        """Model of a car."""
        return self._model

    @model.setter
    def model(self, model: str):
        """A setter for a model of a car.

        Raises:
            TypeError: An error occurred when passed argument is not a string.
        """
        if not isinstance(model, str):
            raise TypeError("Model must be a string")
        self._model = model

    def evaluate_cost(self) -> int:
        """Evaluates cost of a car using hyper comprehensive super accurate
        algorithm.

        Base class (Car) is an abstraction hence it costs nothing.

        Method should be overwritten in every child class since every type of
        car needs different algo.

        Returns:
            An evaluated cost of a car in dollars.
        """
        return 0

    def gas(self) -> str:
        """Hit the gas and go.

        Returns: A sound of a running car.
        """
        self._speed_up()
        return "Ka-chow!"  # know the meme

    def _speed_up(self):
        """Speed up the car :D.

        Method is non-public since user doesn't have to know how the mechanism
        works under the hood and doesn't have to call the method either.
        """
        print("First gear")
        print("Second gear")
        print("Third gear")

    def __str__(self) -> str:
        return f"Car: {self._brand} {self._model}"

    def __repr__(self) -> str:
        return f"Car({self._brand!r}, {self._model!r})"


class PassengerCar(Car):
    """Class for passenger car.

    Attributes:
        brand: a string representing a car brand (such as Tesla, Chevrolet, ...)
        model: a string representing a model name (such as Model S, Camaro, ...)
        max_speed: an integer representing max speed of a car.
    """

    def __init__(self, brand: str, model: str, max_speed: int):
        """Init PassengerCar with brand, model and max speed."""
        super().__init__(brand, model)
        self.max_speed = max_speed

    @property
    def max_speed(self) -> int:
        """Max speed of a car in km/h."""
        return self._max_speed

    @max_speed.setter
    def max_speed(self, max_speed: int):
        """A setter for max speed.

        Raises:
            TypeError: An error occurred when passed argument is not an integer.
            ValueError: An error occurred when passed argument is non-positive.
        """
        if not isinstance(max_speed, int):
            raise TypeError("Max speed must be an integer")
        if not max_speed > 0:
            raise ValueError("Max speed must be a positive integer")
        self._max_speed = max_speed

    def evaluate_cost(self) -> int:
        """See base class."""
        return self._max_speed * 500

    def __repr__(self) -> str:
        return f"PassengerCar({self._brand!r}, {self._model!r}," \
               f"{self._max_speed})"


class Truck(Car):
    """Class for a truck.

    Attributes:
        brand: a string representing a car brand (such as Tesla, Chevrolet, ...)
        model: a string representing a model name (such as Model S, Camaro, ...)
        load: an integer representing max speed of a car.
    """

    def __init__(self, brand: str, model: str, load: float):
        """Init Truck with brand, model and vehicle load."""
        super().__init__(brand, model)
        self.load = load

    @property
    def load(self) -> float:
        """Vehicle load of a truck in tons."""
        return self._load

    @load.setter
    def load(self, load: float):
        """A setter for a vehicle load.

        Raises:
            TypeError: An error occurred when passed argument is not a float.
            ValueError: An error occurred when passed argument is non-positive.
        """
        if not isinstance(load, float):
            raise TypeError("Load must be a float")
        if not load > 0:
            raise ValueError("Load must be a positive float")
        self._load = load

    def evaluate_cost(self) -> int:
        """See base class."""
        return round(self._load * 1234)

    def __repr__(self) -> str:
        return f"Truck({self._brand!r}, {self._model!r}, {self._load})"


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
