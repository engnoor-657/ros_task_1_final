from zope.interface import Interface
from abc import ABC

class Iultra(Interface, ABC):
    @abstractmethod
    def get_reading() -> int:
        """Get the reading from the ultrasonic sensor."""