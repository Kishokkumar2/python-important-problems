# taking data from parent class to child


class Parent:
    def sing(self):
        print("parent is singer")
class Child(Parent):
    def dance(self):
        print("child is dancer")

class Yourchild(Child):
    def music(self):
        print("your child is musician")
parent1=Parent()
parent1.sing()
child1=Child()
child1.sing()
child1.dance( )
your=Yourchild()
your.sing()