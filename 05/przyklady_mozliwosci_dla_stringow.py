def list_my_numbers():
    txt_list = ""
    for i in range(20):
        txt_list += str(i) + ", "
    return txt_list


name = "Daria"
fav_color = "niebieski"
print("Im", name, "my fav color is", fav_color)
print("Im {} my fav color is {}".format(name, fav_color))
print(f"Im {name * 2} my fav color is {fav_color}")  # w nawiasie mozna wpisac kod
print(f"Im {name * 2} my fav numbers are: {list_my_numbers()}")
