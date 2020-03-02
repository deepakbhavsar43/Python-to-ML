class Dog:
    def __init__(sel):
        sel.name = str(input("Enter name of dog : "))
        sel.age = int(input("Enter age of dog : "))
        sel.species = str(input("Enter species of dog : "))


taison  = Dog()
sheru = Dog()

print(taison == sheru)
print(taison)
print("{} is {} years old {} dog.".format(taison.name, taison.age, taison.species))
print(sheru)
print("{} is {} years old {} dog.".format(sheru.name, sheru.age, sheru.species))
