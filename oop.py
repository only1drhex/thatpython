class Myclass:
    # x = 2
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = Myclass(
    "dsvid",
    15
    
    )


# print(obj.x)
# print(obj.name)


class Students:
    def __init__(self, id, name):
        
        self.name = name
        self.id = id

    def sayName(self):
        # return f"Welcome {self.id}, {self.name}"
        return "Welcome {}, {} ".format(self.id, self.name)

    

studentObj = Students("id44", "Lanre").sayName()

print(studentObj)


        




