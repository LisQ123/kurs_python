# dog = {
#     name : "Pimpek",
#     breed : "Sznaucer",
#     age : 4,
#     color : "white"
# }
import random


class Dog:
    tail = True

    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        self.pseudo = name + "-" + color

    # def pseudo(self):
    #     adj = ["destroyer", "powerful", "funny", "sweet"]
    #     return self.name + "-" + random.choice(adj)
    def bark(self):
        return "Hau" * self.age

obj_pimpek = Dog("Pimpek", "Colie", 5, "white")
obj_dyzio = Dog("Dyzio", "Cotton de tulear", 7, "blond")

# print(Dog.pseudo(obj_dyzio))
print(obj_dyzio.bark())