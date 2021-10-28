"""
Show how to have enemies shoot bullets aimed at the player.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_bullets_enemy_aims
"""

import arcade
import math
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites and Bullets Enemy Aims Example"
BULLET_SPEED = 4


class MyGame(arcade.Window):
    """ Main application class """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.color.BLACK)

        self.frame_count = 0

        self.enemy_list = None
        self.bullet_list = None
        self.player_list = None
        self.player = None

    def setup(self):
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        # Add player ship
        self.player = arcade.Sprite(":resources:images/space_shooter/playerShip1_orange.png", 0.5)
        self.player_list.append(self.player)

        # Add top-left enemy ship
        enemy = arcade.Sprite(":resources:images/space_shooter/playerShip1_green.png", 0.5)
        enemy.center_x = 120
        enemy.center_y = SCREEN_HEIGHT - enemy.height
        enemy.angle = 180
        self.enemy_list.append(enemy)

        # Add top-right enemy ship
        enemy = arcade.Sprite(":resources:images/space_shooter/playerShip1_green.png", 0.5)
        enemy.center_x = SCREEN_WIDTH - 120
        enemy.center_y = SCREEN_HEIGHT - enemy.height
        enemy.angle = 180
        self.enemy_list.append(enemy)

    def on_draw(self):
        """Render the screen. """

        arcade.start_render()

        self.enemy_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()

    def on_update(self, delta_time):
        """All the logic to move, and the game logic goes here. """

        self.frame_count += 1

        # Loop through each enemy that we have
        for enemy in self.enemy_list:

            # First, calculate the angle to the player. We could do this
            # only when the bullet fires, but in this case we will rotate
            # the enemy to face the player each frame, so we'll do this
            # each frame.

            # Position the start at the enemy's current location
            start_x = enemy.center_x
            start_y = enemy.center_y

            # Get the destination location for the bullet
            dest_x = self.player.center_x
            dest_y = self.player.center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Set the enemy to face the player.
            enemy.angle = math.degrees(angle)-90

            # Shoot every 60 frames change of shooting each frame
            if self.frame_count % 60 == 0:
                bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png")
                bullet.center_x = start_x
                bullet.center_y = start_y

                # Angle the bullet sprite
                bullet.angle = math.degrees(angle)

                # Taking into account the angle, calculate our change_x
                # and change_y. Velocity is how fast the bullet travels.
                bullet.change_x = math.cos(angle) * BULLET_SPEED
                bullet.change_y = math.sin(angle) * BULLET_SPEED

                self.bullet_list.append(bullet)

        # Get rid of the bullet when it flies off-screen
        for bullet in self.bullet_list:
            if bullet.top < 0:
                bullet.remove_from_sprite_lists()

        self.bullet_list.update()

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """Called whenever the mouse moves. """
        self.player.center_x = x
        self.player.center_y = y


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()


# """
# Show how to have enemies shoot bullets at regular intervals.
#
# If Python and Arcade are installed, this example can be run from the command line with:
# python -m arcade.examples.sprite_bullets_periodic
# """
# import arcade
#
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# SCREEN_TITLE = "Sprites and Periodic Bullets Example"
#
#
#
# class EnemySprite(arcade.Sprite):
#
#     """ Enemy ship class that tracks how long it has been since firing. """
#
#
#
#     def __init__(self, image_file, scale, bullet_list, time_between_firing):
#
#         """ Set up the enemy """
#
#         super().__init__(image_file, scale)
#
#
#
#         # How long has it been since we last fired?
#
#         self.time_since_last_firing = 0.0
#
#
#
#         # How often do we fire?
#
#         self.time_between_firing = time_between_firing
#
#
#
#         # When we fire, what list tracks the bullets?
#
#         self.bullet_list = bullet_list
#
#
#
#     def on_update(self, delta_time: float = 1/60):
#
#         """ Update this sprite. """
#
#
#
#         # Track time since we last fired
#
#         self.time_since_last_firing += delta_time
#
#
#
#         # If we are past the firing time, then fire
#
#         if self.time_since_last_firing >= self.time_between_firing:
#
#
#
#             # Reset timer
#
#             self.time_since_last_firing = 0
#
#
#
#             # Fire the bullet
#
#             bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png")
#
#             bullet.center_x = self.center_x
#
#             bullet.angle = -90
#
#             bullet.top = self.bottom
#
#             bullet.change_y = -2
#
#             self.bullet_list.append(bullet)
#
#
#
# class MyGame(arcade.Window):
#     """ Main application class """
#
#     def __init__(self):
#         super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
#
#         arcade.set_background_color(arcade.color.BLACK)
#
#         self.player = None
#         self.player_list = None
#         self.enemy_list = None
#         self.bullet_list = None
#
#     def setup(self):
#         """ Setup the variables for the game. """
#
#         self.player_list = arcade.SpriteList()
#         self.enemy_list = arcade.SpriteList()
#         self.bullet_list = arcade.SpriteList()
#
#         # Add player ship
#         self.player = arcade.Sprite(":resources:images/space_shooter/playerShip1_orange.png", 0.5)
#         self.player_list.append(self.player)
#
#         # Add top-left enemy ship
#
#         enemy = EnemySprite(":resources:images/space_shooter/playerShip1_green.png",
#
#                             scale=0.5,
#
#                             bullet_list=self.bullet_list,
#
#                             time_between_firing=2.0)
#
#         enemy.center_x = 120
#         enemy.center_y = SCREEN_HEIGHT - enemy.height
#         enemy.angle = 180
#         self.enemy_list.append(enemy)
#
#         # Add top-right enemy ship
#
#         enemy = EnemySprite(":resources:images/space_shooter/playerShip1_green.png",
#
#                             scale=0.5,
#
#                             bullet_list=self.bullet_list,
#
#                             time_between_firing=1.0)
#
#         enemy.center_x = SCREEN_WIDTH - 120
#         enemy.center_y = SCREEN_HEIGHT - enemy.height
#         enemy.angle = 180
#         self.enemy_list.append(enemy)
#
#     def on_draw(self):
#         """Render the screen. """
#
#         arcade.start_render()
#
#         self.enemy_list.draw()
#         self.bullet_list.draw()
#         self.player_list.draw()
#
#     def on_update(self, delta_time):
#         """ All the logic to move, and the game logic goes here. """
#
#
#         # Call on_update for each enemy in  the list
#
#         self.enemy_list.on_update(delta_time)
#
#
#         # Get rid of the bullet when it flies off-screen
#         for bullet in self.bullet_list:
#             if bullet.top < 0:
#                 bullet.remove_from_sprite_lists()
#
#         self.bullet_list.update()
#
#     def on_mouse_motion(self, x, y, delta_x, delta_y):
#         """
#         Called whenever the mouse moves.
#         """
#         self.player.center_x = x
#         self.player.center_y = 20
#
#
# def main():
#     """ Run the game """
#     window = MyGame()
#     window.setup()
#     arcade.run()
#
#
# if __name__ == "__main__":
#     main()

# Shoot at an Angel
# """
# Sprite Bullets
#
# Simple program to show basic sprite usage.
#
# Artwork from https://kenney.nl
#
# If Python and Arcade are installed, this example can be run from the command line with:
# python -m arcade.examples.sprite_bullets_aimed
# """
#
# import random
# import arcade
# import math
# import os
#
# SPRITE_SCALING_PLAYER = 0.5
# SPRITE_SCALING_COIN = 0.2
# SPRITE_SCALING_LASER = 0.8
# COIN_COUNT = 50
#
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# SCREEN_TITLE = "Sprites and Bullets Aimed Example"
#
# BULLET_SPEED = 5
#
# window = None
#
#
# class MyGame(arcade.Window):
#     """ Main application class. """
#
#     def __init__(self):
#         """ Initializer """
#         # Call the parent class initializer
#         super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
#
#         # Set the working directory (where we expect to find files) to the same
#         # directory this .py file is in. You can leave this out of your own
#         # code, but it is needed to easily run the examples using "python -m"
#         # as mentioned at the top of this program.
#         file_path = os.path.dirname(os.path.abspath(__file__))
#         os.chdir(file_path)
#
#         # Variables that will hold sprite lists
#         self.player_list = None
#         self.coin_list = None
#         self.bullet_list = None
#
#         # Set up the player info
#         self.player_sprite = None
#         self.score = 0
#         self.score_text = None
#
#         # Load sounds. Sounds from kenney.nl
#         self.gun_sound = arcade.sound.load_sound(":resources:sounds/laser1.wav")
#         self.hit_sound = arcade.sound.load_sound(":resources:sounds/phaseJump1.wav")
#
#         arcade.set_background_color(arcade.color.AMAZON)
#
#     def setup(self):
#
#         """ Set up the game and initialize the variables. """
#
#         # Sprite lists
#         self.player_list = arcade.SpriteList()
#         self.coin_list = arcade.SpriteList()
#         self.bullet_list = arcade.SpriteList()
#
#         # Set up the player
#         self.score = 0
#
#         # Image from kenney.nl
#         self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING_PLAYER)
#         self.player_sprite.center_x = 50
#         self.player_sprite.center_y = 70
#         self.player_list.append(self.player_sprite)
#
#         # Create the coins
#         for i in range(COIN_COUNT):
#
#             # Create the coin instance
#             # Coin image from kenney.nl
#             coin = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)
#
#             # Position the coin
#             coin.center_x = random.randrange(SCREEN_WIDTH)
#             coin.center_y = random.randrange(120, SCREEN_HEIGHT)
#
#             # Add the coin to the lists
#             self.coin_list.append(coin)
#
#         # Set the background color
#         arcade.set_background_color(arcade.color.AMAZON)
#
#     def on_draw(self):
#         """ Render the screen. """
#
#         # This command has to happen before we start drawing
#         arcade.start_render()
#
#         # Draw all the sprites.
#         self.coin_list.draw()
#         self.bullet_list.draw()
#         self.player_list.draw()
#
#         # Put the text on the screen.
#         output = f"Score: {self.score}"
#         arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
#
#     def on_mouse_press(self, x, y, button, modifiers):
#         """ Called whenever the mouse button is clicked. """
#
#         # Create a bullet
#         bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_LASER)
#
#         # Position the bullet at the player's current location
#         start_x = self.player_sprite.center_x
#         start_y = self.player_sprite.center_y
#         bullet.center_x = start_x
#         bullet.center_y = start_y
#
#         # Get from the mouse the destination location for the bullet
#         # IMPORTANT! If you have a scrolling screen, you will also need
#         # to add in self.view_bottom and self.view_left.
#         dest_x = x
#         dest_y = y
#
#         # Do math to calculate how to get the bullet to the destination.
#         # Calculation the angle in radians between the start points
#         # and end points. This is the angle the bullet will travel.
#         x_diff = dest_x - start_x
#         y_diff = dest_y - start_y
#         angle = math.atan2(y_diff, x_diff)
#
#         # Angle the bullet sprite so it doesn't look like it is flying
#         # sideways.
#         bullet.angle = math.degrees(angle)
#         print(f"Bullet angle: {bullet.angle:.2f}")
#
#         # Taking into account the angle, calculate our change_x
#         # and change_y. Velocity is how fast the bullet travels.
#         bullet.change_x = math.cos(angle) * BULLET_SPEED
#         bullet.change_y = math.sin(angle) * BULLET_SPEED
#
#         # Add the bullet to the appropriate lists
#         self.bullet_list.append(bullet)
#
#     def on_update(self, delta_time):
#         """ Movement and game logic """
#
#         # Call update on all sprites
#         self.bullet_list.update()
#
#         # Loop through each bullet
#         for bullet in self.bullet_list:
#
#             # Check this bullet to see if it hit a coin
#             hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)
#
#             # If it did, get rid of the bullet
#             if len(hit_list) > 0:
#                 bullet.remove_from_sprite_lists()
#
#             # For every coin we hit, add to the score and remove the coin
#             for coin in hit_list:
#                 coin.remove_from_sprite_lists()
#                 self.score += 1
#
#             # If the bullet flies off-screen, remove it.
#             if bullet.bottom > self.width or bullet.top < 0 or bullet.right < 0 or bullet.left > self.width:
#                 bullet.remove_from_sprite_lists()
#
#
# def main():
#     game = MyGame()
#     game.setup()
#     arcade.run()
#
#
# if __name__ == "__main__":
#     main()