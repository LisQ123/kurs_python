class Vertebrate:
    backbone = True

    def __init__(self):
        print('Vertebrates represent the overwhelming majority of the phylum Chordata')


    def desc(self):
        return 'The word vertebrate derives from the Latin word vertebratus, meaning joint of the spine.'


class Cat(Vertebrate):
    def __init__(self, name):
        print('Kotek!')
        self.name = name

    def desc(self):
        print('Koty sa super')
        super().__init__()


    def sound(self):
        return 'miau'

ver = Vertebrate()
kitty = Cat('Kitty')
print(kitty.backbone)