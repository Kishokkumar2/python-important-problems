# polymism allows the methoh to behave differently based on the object action

class person:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sleep(self,sleeptime):
        print("sleeping timing is",sleeptime)
    def sleep(self,s,e):
        print("Sleeping time",s-e)



p=person("kishok",20)
p.sleep(20,12)