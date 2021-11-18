import arcade
import random

WIDTH = 60
HEIGHT = 60
MARGIN = 5
COLUMN_COUNT = 10
ROW_COUNT = 10
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.NAVY_BLUE)

        # Create grid of numbers
        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

        self.grid[2][1] = 1
        # row column format
        print(self.grid)

        # another way to create a grid of numbers
        # self.grid = [[0 for x in range(10)] for y in range(10)]

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                x = MARGIN + WIDTH / 2 + column * (WIDTH + MARGIN)
                y = MARGIN + HEIGHT / 2 + row * (HEIGHT + MARGIN)
                if self.grid[row][column] == 0:
                    color = arcade.color.ORANGE
                else:
                    color = (random.randrange(256),
                             random.randrange(256),
                             random.randrange(256))
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        row = y // (HEIGHT + MARGIN)
        column = x // (WIDTH + MARGIN)
        print("Click", row, column)
        if self.grid[row][column] == 0:
            self.grid[row][column] = 1
        else:
            self.grid[row][column] = 0


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()

# Part 1
# lab has nothing to do the draw. do not change the on draw method.
# change the click method. On mouse_press is where this will take place
# only do it if where you click in a certain range, four if statmetenst are needed.
