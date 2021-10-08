class Room:
    """
    This is a class that represents the room
    """
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    room_list = []
    room = Room("You are standing outside. The corn is green and the trees are full of leaves."
                "There is a barn to the east and a house to the west.",
                None, 10, None, 1)
    room_list.append(room)
    room = Room("You are standing in a hallway. The light is dim and pictures on the wall of landscapes"
                "You can walk north into a long hallway that leads to office and living room."
                "You can walk south into a hallway that will take you to a bedroom and the kitchen."
                "You can continue straight and walk to the master bedroom or office.",
                2, 0, 5, 8)
    room_list.append(room)
    room = Room("You are standing in hallway. There are clay statues lining wall."
                " You can head west and go into the office."
                "You can east into the living room.",
                None, 3, 1, 9)
    room_list.append(room)
    room = Room("You are standing in the living room. "
                "There is a large window that has a view of the corn field outside."
                "There is a TV, a couch, and multiple chairs."
                "The remote is sitting by the couch."
                "There are no other exits out of the living room besides the way you came.",
                None, None, None, 2)
    room_list.append(room)
    room = Room("You are standing in the kitchen. Pots and pans line the counter of last nights dinner"
                "The fruit bowl is sitting on the table. Spoons have been spilled on the floor."
                "You can enter back into the hallway by heading west.",
                None, None, None, 5)
    room_list.append(room)
    room = Room("You are in a hallway. Light is shining through the small window, the hard tile is clean."
                "You can head west into the guest bedroom."
                "You can head east into the kitchen."
                "You can head north into the original hallway.",
                1, 4, None, 6)
    room_list.append(room)
    room = Room("You are in the guest bedroom."
                "You can head east into the hallway.",
                None, 5, None, None)
    room_list.append(room)
    room = Room("You are standing in the master bedroom. The king size bed is a mess."
                "Cloths are scattered throughout the room. "
                "You can head north back into the hallway",
                8, None, None, None)
    room_list.append(room)
    room = Room("You are standing in a hallway. 18th centerys line the walls. "
                "You can head south into the master bedroom."
                "You can head north into the office or can head east back down the hallway.",
                9, 1, 7, None)
    room_list.append(room)
    room = Room("You are in the office. There is desk that is neatly organized."
                "There is a stapler and a copier on the desk. "
                "You can head south in to the hallway or east into a different hallway.",
                None, 2, 8, None)
    room_list.append(room)
    room = Room("You are standing in the barn. Hay is lining the floor and smells good."
                "There is an empty horse stable and mice running. You can head west back outside",
                None, None, None, 0)
    room_list.append(room)

    current_room = 0
    done = False

    while not done:
        print()
        print(room_list[current_room].description)
        user_input = input("What do you want to do?")
        if user_input.lower == "n" or user_input.lower == "north":
            next_room = room_list[current_room].north














main()


