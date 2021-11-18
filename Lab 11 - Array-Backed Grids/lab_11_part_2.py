import arcade

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
                    color = arcade.color.WHITE
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        row = int(y // (HEIGHT + MARGIN))
        column = int(x // (WIDTH + MARGIN))
        print("Click", row, column)
        if self.grid[row][column] == 0:
            self.grid[row][column] = 1
        else:
            self.grid[row][column] = 0

        # Listing 1
        total = 0
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    total += 1
        print("Total of ", total, "cells are selected.")

        # Listing 2
        for row in range(ROW_COUNT):
            cell_count = 0
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    cell_count += 1
            print("Row ", row, "has ", cell_count, "cells selected.")

        # Listing 3
        for column in range(COLUMN_COUNT):
            cell_count = 0
            for row in range(ROW_COUNT):
                if self.grid[row][column] == 1:
                    cell_count += 1
            print("Column ", column, "has ", cell_count, "cells selected")



def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
