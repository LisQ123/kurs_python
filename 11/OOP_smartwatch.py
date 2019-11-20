class UsefulStuff:
    def __init__(self):
        print("I'm useful")


class Watch(UsefulStuff):
    def __init__(self):
        print("I can check: what time is it")


class Phone(UsefulStuff):
    def __init__(self):
        print("I can call")


class SmartWatch(Watch, Phone):
    def __init__(self):
        print("I'm smartwatch")
        super().__init__()
# u = UsefulStuff()
# w = Watch()
# p = Phone()
sw = SmartWatch()
