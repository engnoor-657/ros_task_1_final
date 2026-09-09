import random
from Iinfrared import Iinfrared
from zope.interface import implementer
@implementer(Iinfrared)
class Infrared:
    def __init__(self):
        self.max_range = 200
        self.min_range = 10

    def get_reading(self) -> int:
        self.reading = random.randint(self.min_range, self.max_range)
        return self.reading