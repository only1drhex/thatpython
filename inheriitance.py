class Students:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def sayName(self):
        pass
        # print(f" hey {self.name} your id is {self.id}")
class Person(Students):

    def __init__(self, name, id):
        super().__init__(name, id)

    def checkInheritance(self):
       print(f" hey there  {self.name} your id is {self.id}")



obj = Person("ola", 23)
print(obj.checkInheritance())