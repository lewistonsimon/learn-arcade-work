import random
import arcade

SPRITE_SCALING = 0.5
TACO_SCALING = .1

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SPRITE_SCALING_BOX = .5
SPRITE_SCALING_PLAYER = .5
TACO_COUNT = 13
PLAYER_MOVEMENT_SPEED = 5
VIEWPORT_MARGIN = 220
CAMERA_SPEED = 0.1

collect_sound = arcade.load_sound(":resources:sounds/coin2.wav")


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        """
        Initializer
        """
        super().__init__(width, height, resizable=True)

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
            wall = arcade.Sprite("stoneMid.png", SPRITE_SCALING_BOX)
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
                           [740, 584],
                           [1572, 392],
                           [1508, 392],
                           [1444, 392],
                           [1380, 392],
                           [1316, 392],
                           [1188, 392],
                           [1188, 328],
                           [1188, 456],
                           [1572, 520],
                           [1508, 520],
                           [1444, 520],
                           [1380, 520],
                           [1316, 520],
                           [1636, 392],
                           [1636, 328],
                           [1636, 264],
                           [1636, 200],
                           [1060, 520],
                           [1060, 456],
                           [1060, 392],
                           [996, 456],
                           [996, 520],
                           [932, 520],
                           [676, 392],
                           [292, 328],
                           [292, 392],
                           [356, 392],
                           [356, 520],
                           [420, 520],
                           [420, 584],
                           [420, 648],
                           [420, 712],
                           [292, 648],
                           [292, 712],
                           [356, 840],
                           [356, 904],
                           [356, 968],
                           [548, 264],
                           [548, 328],
                           [548, 392],
                           [612, 520],
                           [676, 520],
                           [548, 648],
                           [1700, 968],
                           [1636, 968],
                           [1636, 904],
                           [1700, 904],
                           [1636, 840],
                           [1700, 840],
                           [1636, 776],
                           [1700, 776],
                           [1636, 712],
                           [1700, 712],
                           [1636, 712],
                           [1700, 648],
                           [1636, 648],
                           [1700, 584],
                           [1508, 712],
                           [1508, 776]]

        # Rows in order from top to bottom
        for coordinate in coordinate_list:
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        for x in range(484, 1572, 64):
            wall = arcade.Sprite("spikes.png", SPRITE_SCALING_BOX, flipped_vertically=True)
            wall.center_x = x
            wall.center_y = 1032
            self.wall_list.append(wall)

        for x in range(484, 1572, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 904
            self.wall_list.append(wall)

        for x in range(740, 1316, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 776
            self.wall_list.append(wall)

        for x in range(868, 1572, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 584
            self.wall_list.append(wall)

        for x in range(996, 1572, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 264
            self.wall_list.append(wall)

        # Placing down the tacos at random
        # I found the taco image from OpenClipart-Vectors, pixabay.com
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

        item_list = [[420, 840],
                     [292, 1032],
                     [1700, 200],
                     [1700, 1032],
                     [1508, 328],
                     [1316, 200],
                     [548, 200],
                     [548, 520],
                     [676, 456],
                     [1060, 328],
                     [740, 648],
                     [932, 648],
                     [1124, 712],
                     [1444, 648],
                     [612, 968],
                     [1380, 968],
                     [996, 840]]

        # I found the taco image from OpenClipart-Vectors, pixabay.com
        # Fixed Taco locations
        for item in item_list:
            taco = arcade.Sprite("taco-155812__340.png", TACO_SCALING)
            taco.center_x = item[0]
            taco.center_y = item[1]

            self.taco_list.append(taco)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color

        arcade.set_background_color(arcade.color.DARK_BLUE)

        arcade.set_background_color(arcade.color.MIDNIGHT_BLUE)

        self.set_mouse_visible(False)

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

        # Camera for our GUI
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

        if len(self.taco_list) == 0:
            arcade.draw_text("Game Over", DEFAULT_SCREEN_WIDTH / 2, DEFAULT_SCREEN_HEIGHT / 2,
                             arcade.color.RED, 50, anchor_x="center")

    def on_update(self, delta_time):
        """ Movement and game logic """

        self.taco_list.update()

        if len(self.taco_list) > 0:
            self.player_list.update()
            self.scroll_to_player()
            self.physics_engine.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.taco_list)
        for taco in hit_list:
            self.score += 1
            arcade.play_sound(collect_sound)
            taco.remove_from_sprite_lists()

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
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
