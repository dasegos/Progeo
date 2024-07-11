from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self, *args, **kwargs):
        pass

    @abstractmethod
    def perimeter(self, *args, **kwargs):
        pass 