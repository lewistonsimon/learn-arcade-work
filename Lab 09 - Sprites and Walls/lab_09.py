import random
import arcade

SPRITE_SCALING = 0.5
TACO_SCALING = .1

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"
SPRITE_SCALING_BOX = .5
SPRITE_SCALING_PLAYER = .5
TACO_COUNT = 45

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 15


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.taco_list = None

        # Set up the player
        self.player_sprite = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        self.score = 0

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.taco_list = arcade.SpriteList()

        # Set up the player
        # image found at kenny.nl
        self.player_sprite = arcade.Sprite("malePerson_idle.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 200
        self.player_list.append(self.player_sprite)

        # Control Wall
        wall = arcade.Sprite("grassCenter_round.png", SPRITE_SCALING_BOX)
        wall.center_x = 100
        wall.center_y = 200
        self.wall_list.append(wall)

        wall = arcade.Sprite("spikes.png", SPRITE_SCALING_BOX, flipped_vertically=True)
        wall.center_x = 868
        wall.center_y = 712
        self.wall_list.append(wall)

        wall = arcade.Sprite("spikes.png", SPRITE_SCALING_BOX)
        wall.center_x = 1060
        wall.center_y = 648
        self.wall_list.append(wall)

        # Walls around the Edge.
        # Bottom
        for x in range(228, 1764, 64):
            wall = arcade.Sprite("grassCenter_round.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 136
            self.wall_list.append(wall)

        # Top
        for x in range(228, 1764, 64):
            wall = arcade.Sprite("grassCenter_round.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1096
            self.wall_list.append(wall)

        # Left
        for y in range(136, 1160, 64):
            wall = arcade.Sprite("grassCenter_round.png", SPRITE_SCALING_BOX)
            wall.center_x = 228
            wall.center_y = y
            self.wall_list.append(wall)

        # Right
        for y in range(136, 1160, 64):
            wall = arcade.Sprite("grassCenter_round.png", SPRITE_SCALING_BOX)
            wall.center_x = 1764
            wall.center_y = y
            self.wall_list.append(wall)

        # Walls Dirt blocks
        coordinate_list = [[484, 200],
                           [484, 264],
                           [484, 328],
                           [484, 392],
                           [484, 456],
                           [484, 520],
                           [484, 584],
                           [484, 648],
                           [484, 712],
                           [484, 776],
                           [484, 840],
                           [676, 200],
                           [676, 264],
                           [676, 328],
                           [740, 328],
                           [612, 776],
                           [740, 520],
                           [740, 264],
                           [740, 200],
                           [804, 264],
                           [804, 200],
                           [804, 456],
                           [868, 200],
                           [868, 392],
                           [932, 328],
                           [996, 264],
                           [676, 776],
                           [676, 712],
                           [676, 648],
                           [1384, 648],
                           [1384, 712],
                           [1384, 776],
                           [676, 584],
                           [740, 584]]

        for coordinate in coordinate_list:
            wall = arcade.Sprite("stoneMid.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # Top most row
        for x in range(484, 1572, 64):
            wall = arcade.Sprite("stoneMid.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 904
            self.wall_list.append(wall)

        for x in range(740, 1316, 64):
            wall = arcade.Sprite("stoneMid.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 776
            self.wall_list.append(wall)

        # Eight rows from the bottom
        for x in range(868, 1572, 64):
            wall = arcade.Sprite("stoneMid.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 584
            self.wall_list.append(wall)

        # Two walls up from bottom
        for x in range(996, 1572, 64):
            wall = arcade.Sprite("stoneMid.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 264
            self.wall_list.append(wall)

        # Placing down the tacos
        for i in range(TACO_COUNT):
            taco = arcade.Sprite("taco-155812__340.png", TACO_SCALING)

            taco_placed_successfully = False

            while not taco_placed_successfully:
                taco.center_x = random.randrange(228, 1764)
                taco.center_y = random.randrange(136, 1096)

                wall_hit_list = arcade.check_for_collision_with_list(taco, self.wall_list)

                taco_hit_list = arcade.check_for_collision_with_list(taco, self.taco_list)

                if len(wall_hit_list) == 0 and len(taco_hit_list) == 0:
                    taco_placed_successfully = True

            self.taco_list.append(taco)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.DARK_BLUE)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.taco_list.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
               f"{self.camera_sprites.position[1]:5.1f})"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

        output = "Score: " + str(self.score)
        arcade.draw_text(output, 10, 40, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        self.player_list.update()
        self.taco_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.taco_list)
        for taco in hit_list:
            self.score += 1
            taco.remove_from_sprite_lists()

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Scroll the screen to the player
        self.scroll_to_player()

    def scroll_to_player(self):
        """
        Scroll the window to the player.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        position = self.player_sprite.center_x - self.width / 2, \
            self.player_sprite.center_y - self.height / 2
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
