"""
This program is for my Lab 2 project.
"""

# Import the "Arcade Library"
import arcade

# Open up a window.
arcade.open_window(600, 600, "Lab 2 Boat")

# Set the background color.
arcade.set_background_color(arcade.color.SKY_BLUE)

# Get ready to draw.
arcade.start_render()

# Drawing the water.
arcade.draw_lrtb_rectangle_filled(0, 600, 250, 0, arcade.color.BLUE)

# Drawing the base of the boat.
arcade.draw_arc_filled(300, 280, 300, 200, arcade.color.BROWN, 180, 360)

# Drawing the Mast of the boat.
arcade.draw_rectangle_filled(350, 380, 20, 350, arcade.color.BROWN)

# Drawing the house on the boat.
arcade.draw_rectangle_filled(330, 300, 180, 40, arcade.color.WHITE)

# Drawing the sail of the boat.
arcade.draw_triangle_filled(340, 550, 340, 350, 100, 350, arcade.color.WHITE)

# Drawing the broom of the boat.
arcade.draw_rectangle_filled(225, 350, 245, 5, arcade.color.BROWN)

# Drawing the windows on the boat.
arcade.draw_circle_filled(370, 295, 10, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(340, 295, 10, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(310, 295, 10, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(280, 295, 10, arcade.color.LIGHT_BLUE)

# Drawing the fish
arcade.draw_triangle_filled(34,50, 34, 20, 10, 50, arcade.color.ORANGE)
arcade.draw_ellipse_filled(40, 50, 35, 25, arcade.color.ORANGE)
arcade.draw_circle_filled(45, 55, 3, arcade.color.BLACK)
# Name of the boat.
arcade.draw_text("Seas the Day",
                 355, 310,
                 arcade.color.REDWOOD, 7)

# Finish drawing.
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()