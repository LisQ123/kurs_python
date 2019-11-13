class Fifo:

    def __init__(self, elements):
        self.elements = elements

    def __str__(self):
        return " - ".join(self.elements)

    def show(self):
        print(self.elements)

    def get(self):
        if len(self.elements) == 0:
            return "no elements"
        else:
            return self.elements.pop(0)

    def put(self, value):
        self.elements.append(value)


list_elem = ["a", "b", "c", "d"]
fifo1 = Fifo(list_elem)

print(fifo1)
fifo1.show()
print(fifo1.get())
v = input("Gimme something: ")
fifo1.put(v)
print(fifo1)
