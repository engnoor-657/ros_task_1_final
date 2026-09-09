import random
from Iultra import Iultra
from zope.interface import implementer

@implementer(Iultra)
class Ultrasonic:
    def __init__(self,max_range,min_range,reading)
        self.max_range = 200
        self.min_range = 10

    def get_reading(self) -> int:
        self.reading = random.randint(self.min_range, self.max_range)
        return self.reading

