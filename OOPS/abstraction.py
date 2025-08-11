# showing only necessary information in the class
from abc import ABC, abstractmethod
class vechicle(ABC):

    @abstractmethod
    def startengine(self):
        print("Dawdwa")
    def b(self):
        print("brake")
        
class car(vechicle):

    def startengine(self):
        print("car engine started")


c=car()
c.startengine()
c.b()

