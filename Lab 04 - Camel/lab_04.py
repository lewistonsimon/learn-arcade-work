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
            if drinks_in_canteen >= 1:
                drinks_in_canteen -= 1
                thirst = 0
                print("You have quenched your thirst. ")
            else:
                print("You do not have any water left.")
        elif choice.lower() == "b":
            camel_distance = random.randrange(5, 13)
            miles_traveled += camel_distance
            thirst += 1
            camel_tiredness += 1
            native_number_now = random.randrange(7, 15)
            natives_traveled += native_number_now
            print("You traveled", camel_distance, "miles")
            print("You are making progress.")
            if random.randrange(20) == 0:
                drinks_in_canteen = 3
                thirst = 0
                camel_tiredness = 0
                print("You found an oasis!")
        elif choice.lower() == "c":
            camel_distance = random.randrange(10, 21)
            miles_traveled += camel_distance
            moving_tiredness = random.randrange(1, 4)
            camel_tiredness += moving_tiredness
            thirst += 1
            native_number_now = random.randrange(7, 15)
            natives_traveled += native_number_now
            print("You traveled", camel_distance, "miles")
            print("You are zooming.")
            if random.randrange(20) == 0:
                drinks_in_canteen = 3
                thirst = 0
                camel_tiredness = 0
                print("You found an oasis!")
        else:
            print("error please pick again.")

        if not done:
            if miles_traveled >= 200:
                print("You Win!")
                done = True

        if not done:
            if thirst > 4 and thirst <= 6:
                print("You are thirsty.")
            elif thirst > 6:
                print("You died of thirst.")
                done = True

        if not done:
            if camel_tiredness > 5 and camel_tiredness <= 8:
                print("Your camel is getting tired.")
            elif camel_tiredness > 8:
                print("Your camel is dead.")
                caught = (miles_traveled - natives_traveled)
                natives_traveled += caught

        if not done:
            if natives_traveled >= miles_traveled:
                print("You have been caught by the natives.")
                print("You have lost.")
                done = True
            elif (miles_traveled - natives_traveled) < 15:
                print("The natives are getting close!")


main()
