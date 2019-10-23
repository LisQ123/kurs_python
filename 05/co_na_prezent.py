gift_list = ["slodycze", "zabawka", "ksiazka", "bizuteria"]
friends_list = ["Oli", "Kasii", "Marty", "Patryka"]
import random


def pick_gift(gift):
    return random.choice(gift)

def pick_friend(friend):
    return random.choice(friend)


print(pick_gift(gift_list), "to prezent dla ", pick_friend(friends_list))
