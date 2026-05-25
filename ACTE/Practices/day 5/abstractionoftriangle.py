from abc import ABC, abstractmethod
class shape(ABC) :
    @abstractmethod
    def area(self) :
        pass

class triangle(shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def area(self):
        return 1/2 *self.l * self.b
a =triangle(5,4)
print("Area of Triangle is ", a.area())
