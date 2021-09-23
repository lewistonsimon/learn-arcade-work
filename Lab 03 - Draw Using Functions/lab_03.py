import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def draw_water():
    arcade.draw_lrtb_rectangle_filled(0, 600, 250, 0, arcade.color.BLUE)


def draw_sailboat():
    # Sail
    arcade.draw_triangle_filled(340, 550, 340, 350, 100, 350, arcade.color.WHITE)
    arcade.draw_rectangle_filled(225, 350, 245, 5, arcade.color.BROWN)
    arcade.draw_rectangle_filled(350, 380, 20, 350, arcade.color.BROWN)

    # Base
    arcade.draw_arc_filled(300, 280, 300, 200, arcade.color.BROWN, 180, 360)
    arcade.draw_rectangle_filled(330, 300, 180, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(370, 295, 10, arcade.color.LIGHT_BLUE, num_segments=32)
    arcade.draw_circle_filled(340, 295, 10, arcade.color.LIGHT_BLUE, num_segments=32)
    arcade.draw_circle_filled(310, 295, 10, arcade.color.LIGHT_BLUE, num_segments=32)
    arcade.draw_circle_filled(280, 295, 10, arcade.color.LIGHT_BLUE, num_segments=32)
    arcade.draw_text("Seas the Day",
                     355, 310,
                     arcade.color.REDWOOD, 7)


def draw_fish(x, y):
    arcade.draw_triangle_filled(34 + x - 43, 50 + y - 45, 20 + x - 43, 20 + y - 45, 10 + x - 43, 55 + y - 45, arcade.color.ORANGE)
    arcade.draw_ellipse_filled(40 + x - 40, 50 + y - 50, 35, 25, arcade.color.ORANGE)
    arcade.draw_circle_filled(45 + x - 40, 55 + y - 52, 3, arcade.color.BLACK, num_segments=32)


def draw_cloud(x, y):
    arcade.draw_circle_filled(30 + x - 30, 55 + y - 55, 20, arcade.color.WHITE)
    arcade.draw_circle_filled(15 + x - 30, 40 + y - 55, 20, arcade.color.WHITE)
    arcade.draw_circle_filled(45 + x - 30, 40 + y - 55, 20, arcade.color.WHITE)
    arcade.draw_ellipse_filled(30 + x - 30, 40 + y - 55, 55, 50, arcade.color.WHITE)


def draw_birds(x, y):
    arcade.draw_circle_filled(100 + x - 100, 300 + y - 300, 5, arcade.color.BLACK, num_segments=32)
    arcade.draw_arc_outline(85 + x - 100, 300 + y - 300, 20, 15, arcade.color.BLACK, 0, 180, 5, 1)
    arcade.draw_arc_outline(115 + x - 100, 300 + y - 300, 20, 15, arcade.color.BLACK, 0, 180, 5, 1)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 3 Boat")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.start_render()

    draw_water()
    draw_sailboat()
    draw_fish(100, 50)
    draw_fish(200, 60)
    draw_fish(200, 115)
    draw_fish(50, 30)
    draw_fish(120, 80)
    draw_fish(270, 100)
    draw_fish(175, 140)
    draw_cloud(500, 520)
    draw_cloud(150, 520)
    draw_cloud(90, 550)
    draw_cloud(70, 490)
    draw_birds(400, 370)
    draw_birds(450, 360)
    draw_birds(500, 375)
    draw_birds(450, 415)

    # Finish drawing.
    arcade.finish_render()

    # Keep the window up until someone closes it.
    arcade.run()


# Call the main function to get the program started.
main()
