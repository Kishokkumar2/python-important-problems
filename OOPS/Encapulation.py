# hiding the object which is to be hidden 

# types:
# *public
# *private
# *protected

# private only accesable inside that class
# protected only accesable inside that class and also accessable to the child class
class School:
    def __init__(self):
        self.Name="ABC"
        self.Place="CHENNAI"
        self.__Revenue=50000000 #private
        self._Fees=100000#private

    def schoolrevenue(self):
        print(self.__Revenue)
    def s(self):
        print(self._Fees)


class Facaluty(School):
    def rev(self):
        print(self._Fees)
        
   

s=School()
print(s.Name)

s.schoolrevenue()
s.s()
s1=Facaluty()
s1.rev()
print(s1.Place)