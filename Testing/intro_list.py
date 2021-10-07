# # x = 3
# # print(x)
# # x = 4
# # print(x)
# # could do the following
# x = (2, 3, 4, 5) # tuple
# print(x)
# x = [2, 3, 4, 5] # list
# print(x)
# x = 2, 3, 4, 5 # considered a tuple
# print(x)

# List
# x = [10, 20]
# # print(x)
# # # wrong ways to print list
# # print(x(1))
#
# # right ways to print list
# print(x[0]) # make sure you consider the 0


# x = [3, 8, 7, 0, 5, 5, 2, 1]
# print(x[1])
# # index is the position we are talking about, starts at zero
# # values are what is in the index
# x = [3, 8, 7, 0, 5, 5, 2, 1]
# print(x[-3]) # counts backwards and is useful to find last element of the list


# x = [3, 8, 7, 0, 5, 5, 2, 1]
# print(x)
#
# x[2] = 22
# print(x)
#
# x = 18 # will toss out the list and print 18
# print(x)

# you can start with a list with nothing in it.
# x = []
# print(x)

# x = [3, 7, 3]
# size = len(x)
# print(x)

# # my_list = [3, 7, 3]
# #
# for item_variable in my_list:
#     print(item_variable)

# my_list = ["Knife", "Spoon", "Fork"]
#
# for item_variable in my_list:
#     print(item_variable)

# my_list = [[2, 3], [6, 5], [8, 10]] # can put list inside of list
# print(my_list[2][0])

# my_list = [2, 3, 6, 5, 8, 10]
#
# for i in range(6):
#     print(my_list[i])

# my_list = [2, 3, 6, 5, 8, 10]
#
# for item in my_list:
#     print(item)
#
# for i in range(len(my_list)):
#     print(my_list[i])

# all do the same thing
# my_list = [2, 3, 6, 5, 8, 10]
#
# for item in my_list:
#     print(item)
#
# for i in range(len(my_list)):
#     print("Item", i, "is", my_list[i])
#
# for index, value in enumerate(my_list):
#     print("Item", index, "is", value)

# my_list = [2, 3, 6, 5, 8, 10]
#
# print(my_list)
#
# my_list.append(100)
# print(my_list)

# how to add to list
# my_list = []
#
# for i in range(5):
#     user_input = int(input("Enter number: "))
#     my_list.append(user_input) # you want the word append not add
#
# print(my_list)

# my_list = ["surprise"] * 100
# print(my_list)

# my_list = [1, 4, 7, 9, 10]
#
# list_total = 0
#
# for item in my_list:
#     list_total += item
#
#
# print(list_total)

#Notes
# You can not change a tuple which is a list in (). It is faster and that is why you might use one.
#
# my_list = (3, 4, 4)
# print(my_list)
#
# my_list = (2, 5, 7) # can just toss the whole thing cant change an indivdual element.


# my_list = []
# for i in range(5):
#     user_input = int(input("enter a number: "))
#     my_list.append(user_input)
#
# print(my_list)

# my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]
#
# for item in my_list:
#     item = item * 2 # stores it in item and is a copy.
#
# print(my_list)

# my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]
#
# for i in range(len(my_list)):
#     my_list[i] *= 2
#
# print(my_list)
#
# x = "This is a sample string"
#
# print("x=", x)
# print("x=", x[0]) # prints out the number of character
# print("x[0", x[6])

# x = "0123456789"
# print("x[:5]=", x[:5])
# print("x[5:]=", x[5:])
# print("x[5:8]=", x[5:8])

# a = "Hi"
# b = "There"
# c = "!"
#
# print(a + b)
# print(a + b + c)
# print(3 * a)
# print(2 * a) + (2 * b)

# for charactr in "This is a test.":
#     print(charactr)

# months = "JanFebMarAprMayJunJulAugSepOctNovDec"
# n = int(input("Enter a month number: "))
# month = months[(n - 1) * 3:(n - 1) * 3 + 3]
# print(month)

# plain_text = "This is a test. ABC abc"
#
# for c in plain_text:
#     print(c, end=" ")

# plain_text = "This is a test. ABC abc"
#
# for c in plain_text:
#     x = ord(c)
#     x += 1
#     c2 = chr(x)
#     print(c2, end="")
# print()
# encrypted_text = "Uijt!jt!b!uftu/!BCD!bcd"
#
# for c in encrypted_text:
#     x = ord(c)
#     x -= 1
#     c2 = chr(x)
#     print(c2, end="")

# my_list = [ 4, 2, 56, 2, 0]
#
# biggest_number = 0 # does not work if negative numbers are in you list
# for item in my_list:
#     if item > biggest_number:
#         biggest_number = item
#
# print(biggest_number)


# my_list = [ -4, -2, -56, -2, -30]
#
# biggest_number = my_list[0]
# for item in my_list:
#     if item > biggest_number:
#         biggest_number = item
#
# print(biggest_number)

# my_list = [-4, -2, -56, 2, 30]
#
# positive_outlook_list = []
# for item in my_list:
#     if item in my_list > 0:
#         positive_outlook_list.append(item)
#
#
# print(positive_outlook_list)
