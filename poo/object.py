#!/usr/bin/env python3

"""

"""

# import

__author__ = "rohkoder"
__version__ = "0.1.0"
__license__ = "MIT"


def main() -> None:
    """ """

    class Computer:

        # this is a 'class attribute'
        # it is available class-wise i.e. for all instances
        chassis = "laptop"

        # this is a 'constructor'
        # it defines the 'attributes' of an instance and is called
        # automatically whenever a new instance is created
        def __init__(self, brand, cpu, ram, ssd) -> None:
            self.brand = brand
            self.cpu = cpu
            self.ram = ram
            self.ssd = ssd

        # this is an 'instance method'
        # it usually defines the behavior of an instance
        def config(self) -> str:
            if self.brand == "Apple":
                return f"This Mac has {self.ram}GB of uRAM and a 1TB SSD."
            return f"This {self.brand} {Computer.chassis} has {self.ram}GB of RAM."

    # this is an instance (object) of the class Computer
    cp1 = Computer("Dell", "i5", 8, 256)
    # print(cp1.config())

    cp2 = Computer("Apple", "M1 Max", 32, 1000)
    print(cp2.config())


if __name__ == "__main__":
    """ """
    main()
