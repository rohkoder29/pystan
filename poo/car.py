#!/usr/bin/env python3

"""

"""

# import

__author__ = "rohkoder"
__version__ = "0.1.0"
__license__ = "MIT"


class Car:
    # class attribute i.e same for all the instances
    brand = "Toyota"

    # initializer or constructor
    # (model, color and speed are instance attributes)
    def __init__(self, model, color, speed) -> None:
        self.model = model
        self.color = color
        self.speed = speed
        self.state = "IDLE"

    # instance method
    def speed_up(self) -> int:
        self.speed += 20
        return self.speed

    def turn_on(self) -> bool:
        self.state = "running"
        return self.state


if __name__ == "__main__":
    """ """
