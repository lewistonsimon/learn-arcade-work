import random


def main():
    print("Welcome to the desert!")
    print("You have taken a camel from a local tribe to make your way across the desert.")
    print("The natives are chasing you to get their camel back.")
    print("Survive your trip and do not get caught.")

    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    natives_traveled = -20
    drinks_in_canteen = 3


    done = False
    while not done:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed. ")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        choice = input("What is your choice? ")
        if choice.lower() == "q":
            done = True
            print("Have a nice day.")
        elif choice.lower() == "e":
            print("You have traveled", miles_traveled, "miles.")
            print("You have", drinks_in_canteen, "drinks left.")
            print("The natives are", (miles_traveled - natives_traveled), "miles behind you.")
        elif choice.lower() == "d":
            native_number_now = random.randrange(7, 15)
            camel_tiredness = 0
            natives_traveled += native_number_now
            print("You had a good night sleep.")
        elif choice.lower() == "a":
            print("You have quenched your thirst. ")
        elif choice.lower() == "b":
            camel_distance = random.randrange(5, 13)
            miles_traveled += camel_distance
            print("You traveled", camel_distance, "miles")
            print("You are making progress.")
        elif choice.lower() == "c":
            camel_distance = random.randrange(10, 21)
            miles_traveled += camel_distance
            print("You traveled", camel_distance, "miles")
            print("You are zooming.")


main()