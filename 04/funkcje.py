def mood():
    print("how are you?")
mood()
print("________________________________________")

def my_mood(answear):
    print("My mood today:")
    print(answear)

resp = input("how are y?")
my_mood(resp)

print("_________________________________________")

def my_mood(answear):
    return answear * 2
resp = input("How are you?")
twiced = my_mood(resp)
print("My mood is like", twiced)
