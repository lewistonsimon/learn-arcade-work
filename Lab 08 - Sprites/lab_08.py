import random
import arcade
import math

SPRITE_SCALING = 0.5
GOOD_SCALE = 0.1
BAD_SCALE = .3
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 2.5
GOOD_SPEED = 4
GOOD_COUNT = 50
BAD_COUNT = 50


class Player(arcade.Sprite):

    def update(self):
        """ Move the player """
        # Move player.
        # Remove these lines if physics engine is moving player.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class Bad(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        """ Constructor. """
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

        # Current angle in radians
        self.circle_angle = 0

        # How far away from the center to orbit, in pixels
        self.circle_radius = 0

        # How fast to orbit, in radians per frame
        self.circle_speed = .01

        # Set the center of the point we will orbit around
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):

        """ Update the ball's position. """
        # Calculate a new x, y
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
            + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
            + self.circle_center_y

        # Increase the angle in prep for the next round.
        self.circle_angle += self.circle_speed


class Good(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Moving the taco.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Bounce off the walls.
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):

        super().__init__(width, height)

        # Sprite lists
        self.player_list = None
        self.bad_list = None
        self.good_list = None
        self.good_sprite_list = None

        # Set up the player
        self.score = 0
        self.player_sprite = None

    def start_new_game(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.bad_list = arcade.SpriteList()
        self.good_list = arcade.SpriteList()
        self.good_sprite_list = arcade.SpriteList()

        self.score = 0
        # malePerson image from kenney.nl
        self.player_sprite = Player("malePerson_walk5.png", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        for i in range(50):

            # Create the bad instance
            # Bad image from kenney.nl
            bad = Bad("bee.png", BAD_SCALE)

            # Position the center of the circle the bad will orbit
            bad.circle_center_x = random.randrange(SCREEN_WIDTH)
            bad.circle_center_y = random.randrange(SCREEN_HEIGHT)

            # Random radius from 10 to 200
            bad.circle_radius = random.randrange(10, 200)

            # Random start angle from 0 to 2pi
            bad.circle_angle = random.random() * 2 * math.pi

            self.bad_list.append(bad)

        for i in range(1):
            # I found the taco image at
            good = Good("taco-155812__340.png", GOOD_SCALE)

            good.center_x = random.randrange(SCREEN_WIDTH)
            good.center_y = random.randrange(SCREEN_HEIGHT)
            good.change_x = random.randrange(GOOD_SPEED)
            good.change_y = random.randrange(GOOD_SPEED)

            self.good_sprite_list.append(good)

        # Set the background color
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.

        self.player_list.draw()
        self.good_sprite_list.draw()
        self.bad_list.draw()

        # Put the text on the screen.
        output = "Score: " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_update(self, delta_time):

        self.good_sprite_list.update()

        if len(self.good_sprite_list) > 0:
            self.player_list.update()
            self.bad_list.update()
        elif len(self.good_sprite_list) == 0:
            arcade.draw_text("Game Over", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.WHITE, 18)

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_sprite_list)
        for good in hit_list:
            # play sound
            self.score += 1
            good.remove_from_sprite_lists()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_list)
        for bad in hit_list:
            # play sound
            self.score -= 1
            bad.remove_from_sprite_lists()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        # If the player presses a key, update the speed
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.start_new_game()
    arcade.run()


if __name__ == "__main__":
    main()
