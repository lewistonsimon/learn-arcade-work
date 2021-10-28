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
# #
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
#
# my_text = "Simpson"
# print(my_text[3:])
#
# my_list = [3, 4, 2, 54, 11, 9]
# # for i in range(len(my_list)):
# #     my_list[i] = 0
# # print(my_list)
# evens_list = []
# # def get_evens(my_list):
# #     for item in my_list:
# #         if item % 2 == 0:
# #             evens_list.append(item)
# #         return evens_list
#
#
# my_list = [2, 3, 4]

# for i in range(len(my_list)):
#     my_list[i] = 0
#
# print(my_list)


# class Address:
#     def __init__(self):
#         self.name = ""
#         self.line1 = ""
#         self.line2 = ""
#         self.city = ""
#         self.state = ""
#         self.zip = ""
#
# def main():
#     # Create an address
#     my_address = Address()
#
#     # This does work:
#     my_address.name = "Dr. Smith"
#     my_address.line1 = "4"
#     print(my_address.name)
#     print(my_address.line1)
#
#
# main()
# import arcade
#
# class Coin(arcade.Sprite):
#
#     def update(self):
#         self.center_x += 1
#         self.center_y -= 1

import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 3


class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)

    def update(self):
        # Move the ball
        self.position_y -= 1
        self.position_x += 1


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()

    def update(self, delta_time):
        self.ball.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0


def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()