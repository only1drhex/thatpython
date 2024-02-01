import datetime


class Person:
    def __init__(self, name,country, dob):
        self.name = name
        self.country = country
        self.dob = dob
    def determineAge(self):
        year = int(self.dob.split("-")[2])
        presentYear = datetime.datetime.today().year
        age = presentYear - year
        return f"Hey! {self.name}, from {self.country} your age is {age}"


obj = Person("lanre","Nigeria","12-4-2002")

print(obj.determineAge())
