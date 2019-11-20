class Animals:
    def __init__(self):
        print('Im an Animal!')


class Mammals(Animals):
    kingdom = 'Mammals'

    def Milk(self):
        print('Mammals are vertebrate animals which produce milk for feeding (nursing) their young')


class Dog(Mammals):
    pass
    # def __init__(self):
    #     print('Dog says: Woof')


class Cat(Mammals):
    def Says(self):
        print('Cat says: Meow')


class Human(Mammals):
    def __init__(self):
        print('Human says: Hello World')
        Mammals.__init__(self)
        Animals.__init__(self)

d = Dog()
c = Cat()
h = Human()
# print(d)
# print(c)
# print(h)