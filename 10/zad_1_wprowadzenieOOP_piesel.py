class Dog:
    def __init__(self, name, color, breed):
        self.name = name
        self.color = color
        self.breed = breed

    def bark(self):
        return self.name + " says Hau"

    def wag(self):
        return self.name + "is wagging his tail"


obj_pimpek = Dog("Pimpek", "white", "jamnik")
obj_szarek = Dog("Szarek", "grey", "colie")
obj_burek = Dog("Burek", "white", "labrador")

print(obj_pimpek.bark())
print(obj_pimpek.wag())