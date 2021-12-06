import random
import arcade

# for i in range(10):
#     x = random.randrange(100000)
#     print(f"My number: {x:6,}")  # you can use a f string anywhere not just a print
#
# x = 5
# y = 4
# z = 777
# print(f"{x=} {y=} {z=}")

# my_fruit = ["Apples", "Oranges", "Grapes", "Pears"]
# my_calories = [4, 300, 70, 30]
#
# for i in range(4):
#     print(my_fruit[i], "are", my_calories[i], "calories.")  # regular
#     print(f"{my_fruit[i]:7} are {my_calories[i]:3} calories.")  # f string
#     # python will right justify numbers and will left justify words
#     print(f"{my_fruit[i]:>7} are {my_calories[i]:<3} calories.")  # f string, flips justify

# clock
# for hours in range(1,13):
#     for minutes in range(0,60):
#         print(f"Time {hours}:{minutes:02}")

# floating point numbers
# x = 0.1
# y = 123.456789
#
# print(f"{x:.1}  {y:.1}")
# print(f"{x:.2}  {y:.2}")
# print(f"{x:.3}  {y:.3}")
# print(f"{x:.4}  {y:.4}")
# print(f"{x:.5}  {y:.5}")
# print(f"{x:.6}  {y:.6}")
#
# print()
# print(f"{x:.1f}  {y:.1f}")
# print(f"{x:.2f}  {y:.2f}")
# print(f"{x:.3f}  {y:.3f}")
# print(f"{x:.4f}  {y:.4f}")
# print(f"{x:.5f}  {y:.5f}")
# print(f"{x:.6f}  {y:.6f}")

# x = 0.1
# y = 123.456789
#
# print(f"My number: '{x:10.1}' and '{y:10.1}'")
# print(f"My number: '{x:10.2}' and '{y:10.2}'")
# print(f"My number: '{x:10.3}' and '{y:10.3}'")
# print(f"My number: '{x:10.4}' and '{y:10.4}'")
# print(f"My number: '{x:10.5}' and '{y:10.5}'")
# print(f"My number: '{x:10.6}' and '{y:10.6}'")
#
# print()
# print(f"My number: '{x:10.1f}' and '{y:10.1f}'")
# print(f"My number: '{x:10.2f}' and '{y:10.2f}'")
# print(f"My number: '{x:10.3f}' and '{y:10.3f}'")
# print(f"My number: '{x:10.4f}' and '{y:10.4f}'")
# print(f"My number: '{x:10.5f}' and '{y:10.5f}'")
# print(f"My number: '{x:10.6f}' and '{y:10.6f}'")

# mistake made
# cost1 = 3.07
# tax1 = cost1 * 0.06
# total1 = cost1 + tax1
#
# print(f"Cost:  ${cost1:5.2f}")
# print(f"Tax:    {tax1:5.2f}")
# print(f"-------------")
# print(f"Total: ${total1:5.2f}")


# cost1 = 3.07
# tax1 = cost1 * 0.06
# total1 = cost1 + tax1
#
# print(f"Cost:  ${cost1:5.3f}")
# print(f"Tax:    {tax1:5.3f}")
# print(f"-------------")
# print(f"Total: ${total1:5.3f}")
#
# cost2 = 5.07
# tax2 = cost2 * 0.06
# total2 = cost2 + tax2
#
# print()
# print(f"Cost:  ${cost2:5.3f}")
# print(f"Tax:    {tax2:5.3f}")
# print(f"-------------")
# print(f"Total: ${total2:5.3f}")
#
# print()
# grand_total = total1 + total2
# print(f"Grand total: ${grand_total:5.3f}")

# with round function
# cost1 = 3.07
# tax1 = round(cost1 * 0.06, 2)
# total1 = cost1 + tax1
#
# print(f"Cost:  ${cost1:5.2f}")
# print(f"Tax:    {tax1:5.2f}")
# print(f"-------------")
# print(f"Total: ${total1:5.2f}")
#
# cost2 = 5.07
# tax2 = round(cost2 * 0.06, 2)
# total2 = cost2 + tax2
#
# print()
# print(f"Cost:  ${cost2:5.2f}")
# print(f"Tax:    {tax2:5.2f}")
# print(f"-------------")
# print(f"Total: ${total2:5.2f}")
#
# print()
# grand_total = total1 + total2
# print(f"Grand total: ${grand_total:5.2f}")

# add a timer

def on_draw(self):
    """ Use this function to draw everything to the screen. """

    # Start the render. This must happen before any drawing
    # commands. We do NOT need an stop render command.
    arcade.start_render()

    # Calculate minutes
    minutes = int(self.total_time) // 60

    # Calculate seconds by using a modulus (remainder)
    seconds = int(self.total_time) % 60

    # Figure out our output
    output = f"Time: {minutes:02d}:{seconds:02d}"

    # Output the timer text.
    arcade.draw_text(output, 300, 300, arcade.color.BLACK, 30)

def update(self, delta_time):
    """
    All the logic to move, and the game logic goes here.
    """
    self.total_time += delta_time