
"""Python serial number generator."""

class SerialGenerator:
    """
    Machine to create unique incrementing serial numbers.
    This class will take a start number and it will return the next sequential
    number.

    Attributes
    -------------------
    start: int
        the starting point unpon the class will start to add numbers

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

     >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.start = start
        self.counter = 0
    
    def generate(self):
        """Will add +1 each time it's called """
        self.output = self.start + self.counter
        self.counter += 1
        return self.output

    def reset(self):
        """Will reset the value to the starting point defined at the beginning and will restart the counter to zero"""
        self.counter = 0
    



