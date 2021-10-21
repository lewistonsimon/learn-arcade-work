import arcade

arcade.open_window(600, 600, "Sound Demo")
laser_sound = arcade.load_sound(":resources:sounds/fall2.wav")
arcade.play_sound(laser_sound)
arcade.run()

#
# Sprites and Collisions
""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

    def on_draw(self):
        arcade.start_render()


def main():
    """ Main method """
    window = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
