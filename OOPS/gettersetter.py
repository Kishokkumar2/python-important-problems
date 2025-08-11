class person:
    def __init__(self):
        self.__name=None

    def setname(self,name):
        if len(name) < 20:
          self.__name=name
        else:
            print("errror")

    def getname(self):
        print(self.__name)
p=person()
p.setname("jai")
p.getname()