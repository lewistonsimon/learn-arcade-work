# answer = 42
# print(f"The answer is {answer}.")

# def average(x, y, z):
#     my_average = (x + y + z) / 3
#     return my_average
#
#
# n1 = 8
# n2 = 29
# n3 = 78
# new_average = average(n1, n2, n3)
# print(new_average)

# done = False
# while not done:
#     quit = input("Do you want to quit?")
#     if quit == "yes":
#         done == True
#
#     attack = input("Do you attack the dragon? ")
#     if attack == "yes":
#         print("Bad choice, you died.")
#         done = True

# def average(x, y, z, w):
#     my_average = (x + y + z + w) / 4
#     return my_average
#
#
# n1 = 2
# n2 = 5
# n3 = 9
# n4 = 8
# new_average = average(n1, n2, n3, n4)
# print(new_average)

# total = 0
# done = False
# while not done:
#     quit = int(input())
#     if quit == 0:
#         done = True

# import random
#
# x = random.random() * 10 + 10
# print(x)

# for i in range(1, 13):
#     for x in range(0,60):
#         print(i, x)
# total = 0
# for i in range(10):
#     total = total + 1
#     print(total)


# def print_triangle(rows):
#     for i in range(rows):
#         for j in range(rows - i - 1):
#             print(".", end=" ")
#         for j in range(i + 1):
#             print(j, end=" ")
#         for j in range(i - 1, -1, -1):
#             print(j, end=" ")
#         for j in range((rows - i), 1, -1):
#             print(".", end=" ")
#         print()
# print_triangle(5)


# def print_rectangle(width, height):
#     for i in range(height):
#         for j in range(width):
#             print("&", end=" ")
#         print()
#
#
# print_rectangle(3, 8)


# def print_tri(rows):
#     for i in range(rows):
#         for j in range(rows - i):
#             print("*", end=" ")
#         print()
#
#
# print_tri(4)
#
# def print_triangle(rows):
#     for i in range(rows):
#         for j in range(rows - 1 - i):
#             print(".", end=" ")
#         for j in range(i + 1):
#             print(j, end=" ")
#         for j in range(i - 1, -1, -1):
#             print(j, end=" ")
#         print()
#
# print_triangle(5)

# x = 1
# while x < 64:
#     print(x)
#     x = x * 2

# my_list = [3, 4, 1, 0]
#
# print(my_list[0])

# different_list = [12, 14, 200, 150, 0, 190]
# print(different_list[2])

# lotto_numbers = [45, 54, 33, 45, 76, 98]
# lotto_numbers[0] = 100
# print(lotto_numbers)

# my_list = [3, 4, 2, 54, 11, 9]
#
# for i in range(len(my_list)):
#     my_list[i] = 0
# print(my_list)

# hourly_temperature = [56, 58, 59, 62]
#
# hourly_temperature.append(65)
# print(hourly_temperature)

# daily_cars_sold_list = [5, 3, 0, 2, 4, 3]
# total_cars_sold = 0
# for daily_cars_sold in daily_cars_sold_list:
#     total_cars_sold += daily_cars_sold
#
# print(total_cars_sold)

# my_list = [3, 5, 2, 1]
# for i in range(len(my_list)):
#     print(my_list[0], end=" ")

# my_list = [[3, 2], [1, 4]]
# print(my_list[1][1])

# my_list = [[0, 0], [1, 2], [5, 6]]
# print(len(my_list))

# my_list = [3] * 4
# print(my_list)

# my_text = "Simpson"
# print(my_text[3:])

my_list = [3, 4, 2, 54, 11, 9]
for i in range(len(my_list)):
    my_list[i] = 0
print(my_list)
