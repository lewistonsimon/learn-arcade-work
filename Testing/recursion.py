# def f():
#     g()
#     print("f")
#
# def g():
#     print("g")
#
# f()

# def f():
#     print("Hello")
#     f()
#
# f()  # prints hello and calls the f() which prints and calls the f()... only works 1000 times

# def f(level):
#     # Print the level we are at
#     print("Recursion call, level",level)
#     # If we haven't reached level ten...
#     if level < 10:
#         # Call this function again
#         # and add one to the level
#         f(level+1)
#
# # Start the recursive calls at level 1
# f(1)

# This program calculates a factorial
# WITHOUT using recursion
# def factorial_nonrecursive(n):
#     answer = 1
#     for i in range(2, n + 1):
#         answer = answer * i
#     return answer

# This program calculates a factorial
# WITH recursion
# def factorial_recursive(n):
#     if n == 1:
#         return 1
#     elif n > 1:
#         return n * factorial_recursive(n - 1)

# Common in math
# def f(n):
#     if n == 1:
#         return 6
#     elif n > 1:
#         return (1 / 2) * f(n - 1) + 4

# """
# Recursive Rectangles
# """
# import arcade
#
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 500
#
#
# def draw_rectangle(x, y, width, height):
#     """ Recursively draw a rectangle, each one a percentage smaller """
#
#     # Draw it
#     arcade.draw_rectangle_outline(x, y, width, height, arcade.color.BLACK)
#
#     # As long as we have a width bigger than 1, recursively call this function with a smaller rectangle
#     if width > 1:
#         # Draw the rectangle 90% of our current size
#         draw_rectangle(x, y, width * .9, height * .9)
#
#
# class MyWindow(arcade.Window):
#     """ Main application class. """
#
#     def __init__(self, width, height):
#         super().__init__(width, height)
#
#         arcade.set_background_color(arcade.color.WHITE)
#
#     def on_draw(self):
#         """ Render the screen. """
#         arcade.start_render()
#
#         # Find the center of our screen
#         center_x = SCREEN_WIDTH / 2
#         center_y = SCREEN_HEIGHT / 2
#
#         # Start our recursive calls
#         draw_rectangle(center_x, center_y, SCREEN_WIDTH, SCREEN_HEIGHT)
#
#
# def main():
#
#     MyWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
#     arcade.run()
#
#
# if __name__ == "__main__":
#     main()


# """
# Recursive H's
# """
# import arcade
#
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 500
#
# RECURSION_DEPTH = 0
#
#
# def draw_h(x, y, width, height, count):
#     """ Recursively draw an H, each one a half as big """
#
#     # Draw the H
#     # Draw cross-bar
#     arcade.draw_line(x + width * .25, height / 2 + y,
#                      x + width * .75, height / 2 + y, arcade.color.BLACK)
#     # Draw left side
#     arcade.draw_line(x + width * .25, height * .5 / 2 + y,
#                      x + width * .25, height * 1.5 / 2 + y, arcade.color.BLACK)
#     # Draw right side
#     arcade.draw_line(x + width * .75, height * .5 / 2 + y,
#                      x + width * .75, height * 1.5 / 2 + y, arcade.color.BLACK)
#
#     # As long as we have a width bigger than 1, recursively call this function with a smaller rectangle
#     if count > 0:
#         count -= 1
#         # Draw the rectangle 90% of our current size
#         # Draw lower left
#         draw_h(x, y, width / 2, height / 2, count)
#         # Draw lower right
#         draw_h(x + width / 2, y, width / 2, height / 2, count)
#         # Draw upper left
#         draw_h(x, y + height / 2, width / 2, height / 2, count)
#         # Draw upper right
#         draw_h(x + width / 2, y + height / 2, width / 2, height / 2, count)
#
#
# class MyWindow(arcade.Window):
#     """ Main application class. """
#
#     def __init__(self, width, height):
#         super().__init__(width, height)
#
#         arcade.set_background_color(arcade.color.WHITE)
#
#     def on_draw(self):
#         """ Render the screen. """
#         arcade.start_render()
#
#         # Start our recursive calls
#         draw_h(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, RECURSION_DEPTH)
#
#
# def main():
#     MyWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
#     arcade.run()
#
#
# if __name__ == "__main__":
#     main()

import random

# These constants are used to determine what should be stored in the grid if we have an empty
# space or a filled space.
EMPTY = "   "
WALL = "XXX"

# Maze must have an ODD number of rows and columns.
# Walls go on EVEN rows/columns.
# Openings go on ODD rows/columns
MAZE_HEIGHT = 51
MAZE_WIDTH = 51


def create_grid(width, height):
    """ Create an empty grid. """
    grid = []
    for row in range(height):
        grid.append([])
        for column in range(width):
            grid[row].append(EMPTY)
    return grid


def print_maze(maze):
    """ Print the maze. """

    # Loop each row, but do it in reverse so 0 is at the bottom like we expect
    for row in range(len(maze) - 1, -1, -1):
        # Print the row/y number
        print(f"{row:3} - ", end="")

        # Loop the row and print the content
        for column in range(len(maze[row])):
            print(f"{maze[row][column]}", end="")

        # Go down a line
        print()

    # Print the column/x at the bottom
    print("     ", end="")
    for column in range(len(maze[0])):
        print(f"{column:3}", end="")
    print()


def create_outside_walls(maze):
    """ Create outside border walls."""

    # Create left and right walls
    for row in range(len(maze)):
        maze[row][0] = WALL
        maze[row][len(maze[row])-1] = WALL

    # Create top and bottom walls
    for column in range(1, len(maze[0]) - 1):
        maze[0][column] = WALL
        maze[len(maze[0]) - 1][column] = WALL


def create_maze(maze, top, bottom, left, right):
    """
    Recursive function to divide up the maze in four sections
    and create three gaps.
    Walls can only go on even numbered rows/columns.
    Gaps can only go on odd numbered rows/columns.
    Maze must have an ODD number of rows and columns.
    """

    # Figure out where to divide horizontally
    start_range = bottom + 2
    end_range = top - 1
    y = random.randrange(start_range, end_range, 2)

    # Do the division
    for column in range(left + 1, right):
        maze[y][column] = WALL

    # Figure out where to divide vertically
    start_range = left + 2
    end_range = right - 1
    x = random.randrange(start_range, end_range, 2)

    # Do the division
    for row in range(bottom + 1, top):
        maze[row][x] = WALL

    # Now we'll make a gap on 3 of the 4 walls.
    # Figure out which wall does NOT get a gap.
    wall = random.randrange(4)
    if wall != 0:
        gap = random.randrange(left + 1, x, 2)
        maze[y][gap] = EMPTY

    if wall != 1:
        gap = random.randrange(x + 1, right, 2)
        maze[y][gap] = EMPTY

    if wall != 2:
        gap = random.randrange(bottom + 1, y, 2)
        maze[gap][x] = EMPTY

    if wall != 3:
        gap = random.randrange(y + 1, top, 2)
        maze[gap][x] = EMPTY

    # Print what's going on
    print(f"Top/Bottom: {top}, {bottom} Left/Right: {left}, {right} Divide: {x}, {y}")
    print_maze(maze)
    print()

    # If there's enough space, to a recursive call.
    if top > y + 3 and x > left + 3:
        create_maze(maze, top, y, left, x)

    if top > y + 3 and x + 3 < right:
        create_maze(maze, top, y, x, right)

    if bottom + 3 < y and x + 3 < right:
        create_maze(maze, y, bottom, x, right)

    if bottom + 3 < y and x > left + 3:
        create_maze(maze, y, bottom, left, x)


def main():

    # Create the blank grid
    maze = create_grid(MAZE_WIDTH, MAZE_HEIGHT)

    # Fill in the outside walls
    create_outside_walls(maze)

    # Start the recursive process
    create_maze(maze, MAZE_HEIGHT - 1, 0, 0, MAZE_WIDTH - 1)


if __name__ == "__main__":
    main()