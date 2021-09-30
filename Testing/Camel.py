# # 'for Loop' - when you know how many times to loop
# # 'while loop' - Loop until a conditions
# for i in range(5):
#     print("I will not chew gum in class.")
# #
# #     print("But I can drink water.")
# New Thing
# repetitions = int(input("How many times"))
# def print_about_gum(repetitions)
#     for i in range(repetitions):
#     print("I will not chew gum in class.")
#
# print("But I can drink water.")
#
# repetitions = int(input("How many times"))
# print_about_gum(repetitions)
#
# print("But I can drink water.")

# for star_count in range(1, 11):
#     print(star_count)

# for star_count in range(10):
#     print(star_count + 1)

# for star_count in range(1, 12, 2):
#     print(star_count)

# # count backwards
# for star_count in range(10, -1, -1):
#     print(star_count)

# for item in [2, 6, 4, 2, 4, 6, 7, 4]:
#     print(item)

# # Nested loops
# for i in range(12):
#     print("a")
#     for j in range(12):
#         print("b")

# Real world example
for hour in range(1, 13):
    for minute in range(60):
        print(hour, minute)

# # Runnning total - make sure intial total is outside
#
# total = 0
# for i in range(5):
#     new_number = int(input("Enter a number: "))
#     total += new_number
#
# print("The total is", total)

# total = 0
# for i in range(1,101):
#     total += i
#
# print("The total is", total)

# for i in range(5):
#     print("Hello")
# print("there")

# a = 0
# for i in range(10):
#     a = a + 1
#     for j in range(10):
#         a = a + 1
# print(a)

# Intro to While loop

# for i in range(10):
#     print(i)

# i = 0 # Sentinel variable
# while i < 10:
#     print(i)
#     i += 1

# i = 10
# while i >= 0:
#     print(i)
#     i -= 1

# New Stuff
# for i in range(10):
#     print(i)

# i = 0
# while i < 10:
#     print(i)
#     i += 1

# i = 10
# while i >= 0:
#     print(i)
#     i -= 1

# New game
# quit = "n"
# while quit.lower() == "n" or quit.lower() == "no":
#     quit = input("Do you want quit?")

# Ways to stop
# done = False
# while not done:
#     quit = input("Do you want to quit? ")
#     if quit.lower() == "y":
#         done = True
#         print("Bye!")
#
#     if not done:
#         attack = input("Do you want to attack the dragon? ")
#         if attack.lower() == "y":
#             done = True
#             print("Bad choice,you died!")

# done = False
# while not done:
#     quit = input("Do you want to quit? ")
#     if quit.lower() == "y":
#         done = True
#         print("Bye!")
#         break
#
#     attack = input("Do you want to attack the dragon? ")
#     if attack.lower() == "y":
#         done = True
#         print("Bad choice,you died!")

# done = False
# while not done:
#     quit = input("Do you want to quit? ")
#     if quit.lower() == "y":
#         done = True
#         print("Bye!")
#         continue
#
#     attack = input("Do you want to attack the dragon? ")
#     if attack.lower() == "y":
#         done = True
#         print("Bad choice,you died!")

# Review
# def count_up(start, end):
#     for cur_number in range (start, end + 1):
#         print(cur_number)
#
# count_up(5, 10)

# Random number
import random

# my_number = random.randrange(50)
# print(my_number)

# for i in range(20):
#     my_number = random.randrange(1, 6)
#     print(my_number)


# my_number = random.randrange(5)
# if my_number == 0:
#     print("Dragon!")
# else:
#     print("No dragon.")

# my_number = random.random()
# print(my_number * 9 + 1)








