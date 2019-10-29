import random
places_list = ["forrest", "mountain", "lake", "mine", "desert"]
adjective_places_list = ["old", "ugly", "horrible", "disgusting", "lonely", "sad", "happy", "mysterious"]
adjective_ppl_list = ["old", "ugly", "nice", "fat", "crazy", "angry", "mysterious"]
lucky_list = [1, 2, 3]
killer_list = ["cat", "spider", "wolf", "lady", "gnome", "monster"]
job_list = ["hunt", "sleep", "eat", "rescue"]
food_list = ["banana", "meat", "dinner", "apple", "candies"]


def init_game():  # zaczynamy
    name = input("Hello, i'm The Game master. What is your name Adventurer?  ").capitalize()
    print(name, ", welcome in my world, its a pleasure to meet you,", fraction(), ".")


def fraction():
    races = ["elf", "human", "gnome", "dwarf"]
    race = random.choice(races)
    return race


def try_again():
    again = input("Do you want to play again? Pick \'yes\' or \'no\'.")
    if again == "yes":
        init_game()
    else:
        print("Goodbye Adventurer...")
        exit()


def death():
    print("You are just died. Game over")
    try_again()


def let_start():  # poczatek
    x = input("Would you like to start your adventure? Pick \'yes\' or \'no\'.")
    if x == "no":
        print("You don't want to play?!?")
        return death()
    elif x == "yes":
        print("Great! We'll see what fate brings you.")
    else:
        print("I see you don't know how to read or write, soo...")
        return death()


def check_lucky():  # latwo umrzec w tym swiecie
    lucky = random.choice(lucky_list)
    kill = random.choice(killer_list).capitalize()
    what_killer = random.choice(adjective_ppl_list)
    if lucky == 1:
        print("Ohh...", what_killer, kill, "suddenly appeared on your way and kill you...")
        return death()
    else:
        return "You are lucky, you just avoided random, unexpected death from {} {}\'s hands.".format(what_killer, kill)


def lucky_adv():  # czy uda sie wykonac misje
    lucky = random.choice(lucky_list)
    if lucky == 1:
        return "You are loser!", death()
    elif lucky == 2:
        return "You did'it! You can start your next adventure!", let_start()
    else:
        return"You didn't complete your mission, but you are still alive so lets start another adventure", let_start()


def jobs():  # zadanie na misji
    job = random.choice(job_list)
    if job == "eat":
        what_eat = random.choice(food_list)
        print("You will", job, what_eat, "now, it isn't a job but ok..everything can happens in my world.", lucky_adv())
    elif job == "sleep":
        print("You will", job, "now. You are really lazy adventurer..everything can happens in my world.", lucky_adv())

    else:
        whom = random.choice(killer_list).capitalize()
        what_whom = random.choice(adjective_ppl_list)
        if job == "rescue":
            return "You will", job, what_whom, whom, "now. Good luck!", lucky_adv()
        elif job == "hunt":
            return "You will", job, "on", what_whom, whom, "Good luck!", lucky_adv()


def first_ad():  # misja
    first_place = random.choice(places_list).capitalize()
    what_place = random.choice(adjective_places_list).capitalize()
    print("Are you ready? Your adventure just started, you are going to the \'", what_place, first_place, "\'")
    print("But we have to check your lucky on a road...", check_lucky())  # cos zle, pokazuje None
    print("You are still alive, great. You are in the\'", what_place, first_place, "\'so let's find some job here.")
    do_sth = input("Do you want to find a job? Pick \'yes\' or \'no\'.")
    if do_sth == "yes":
        return jobs()
    elif do_sth == "no":
        print("If you don't want to work you won't play!", death())


init_game()
long = int(input("Just tell me, how many advantures do you want to achiev?"))
how_long = 0
let_start()
while long > int(how_long):
    first_ad()
    how_long = how_long + 1
else:
    print("Your travel should be over as you wished at the beginning!")
    try_again()
