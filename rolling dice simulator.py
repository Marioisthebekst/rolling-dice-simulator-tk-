from random import randrange

main = input("Welcome to the rolling dice simulator! \nCreated by itay \nWould you like to start?\n y for yes and n for no: ")

if main != "y":
    quit(":( Hope we will see you next time!")

if main == "y":
    role = input("Great!\nfor rolling 1 cube type role 1 for rolling 2 cubes type role 2: ")
    if role == "role 1":
        print(randrange(1, 6))
    if role == "role 2":
        print(randrange(1,6))
        print( randrange(1,6))


def rolling():
    for i in range(100000):
        again =input("would you like to do another one? \nif yes type role 1 or role 2: ")
        if again == "role 1":
            print(randrange(1, 6))
        if again == "role 2":
            print(randrange(1, 6))
            print(randrange(1,6))


        if again != "role 1" and again != "role 2":
            sure =input("are you sure you want to quit?\nif no type yes: ")
            if sure == "yes":
                continue
            if sure != "yes":
                quit("Okay see you next time!")



# perfect rolling dice simulator!
print(rolling())