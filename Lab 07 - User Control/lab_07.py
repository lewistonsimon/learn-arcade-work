""" Lab 7 - User Control """

import arcade

laser_sound = arcade.load_sound(":resources:sounds/fall2.wav")
arcade.play_sound(laser_sound)

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


def draw_water():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, arcade.color.BLUE)


def birds(x, y):
    arcade.draw_circle_filled(100 + x - 100, 300 + y - 300, 5, arcade.color.BLACK, num_segments=32)
    arcade.draw_arc_outline(85 + x - 100, 300 + y - 300, 20, 15, arcade.color.BLACK, 0, 180, 5, 1)
    arcade.draw_arc_outline(115 + x - 100, 300 + y - 300, 20, 15, arcade.color.BLACK, 0, 180, 5, 1)


def fish(x, y):
    arcade.draw_triangle_filled(34 + x - 43, 50 + y - 45, 20 + x - 43, 20 + y - 45, 10 + x - 43, 55 + y - 45, arcade.color.ORANGE)
    arcade.draw_ellipse_filled(40 + x - 40, 50 + y - 50, 35, 25, arcade.color.ORANGE)
    arcade.draw_circle_filled(45 + x - 40, 55 + y - 52, 3, arcade.color.BLACK, num_segments=32)


class Fish:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_triangle_filled(34 + self.position_x - 43, 50 + self.position_y - 45, 20 + self.position_x - 43, 20 + self.position_y - 45, 10 + self.position_x - 43, 55 + self.position_y - 45,
                                    arcade.color.ORANGE)
        arcade.draw_ellipse_filled(40 + self.position_x - 40, 50 + self.position_y - 50, 35, 25, arcade.color.ORANGE)
        arcade.draw_circle_filled(45 + self.position_x - 40, 55 + self.position_y - 52, 3, arcade.color.BLACK, num_segments = 32)


class Bird:
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
        arcade.draw_circle_filled(100 + self.position_x - 100, 300 + self.position_y - 300, 5, arcade.color.BLACK, num_segments=32)
        arcade.draw_arc_outline(85 + self.position_x - 100, 300 + self.position_y - 300, 20, 15, arcade.color.BLACK, 0, 180, 5, 1)
        arcade.draw_arc_outline(115 + self.position_x - 100, 300 + self.position_y - 300, 20, 15, arcade.color.BLACK, 0, 180, 5, 1)

    def update(self):
        # Move the bird
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        # Create our fish
        self.fish = Fish(50, 50, 15, arcade.color.AUBURN)
        self.set_mouse_visible(False)

        # Create our bird
        self.bird = Bird(50, 50, 0, 0, 15, arcade.color.AUBURN)

    def on_draw(self):
        arcade.start_render()
        draw_water()
        fish(50, 30)
        birds(450, 360)
        self.fish.draw()
        self.bird.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.fish.position_x = x
        self.fish.position_y = y

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):

        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left button hit at, ", x, y)
        if button == arcade.MOUSE_BUTTON_RIGHT:
            print("Right button hit at, ", x, y)

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.bird.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.bird.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.bird.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.bird.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.bird.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.bird.change_y = 0

    def on_update(self, delta_time: float):
        self.bird.update()


def main():
    window = MyGame()
    arcade.run()


main()
