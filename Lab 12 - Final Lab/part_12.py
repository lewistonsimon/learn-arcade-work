class Room:
    """
    This is a class that represents the rooms.
    """
    def __init__(self, description, north, east, south, west, up, down, northeast, northwest, southeast, southwest):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.northeast = northeast
        self.northwest = northwest
        self.southeast = southeast
        self.southwest = southwest


class Item:
    """
    This is a class that represents the items.
    """
    def __init__(self, room_number):
        self.stapler = room_number
        self.compass = 0
        self.knife = 0
        self.food = 0
        self.fork = 0
        self.bucket = 0
        self.twine = 0
        self.corn = 0


def main():

    # Rooms
    room_list = []
    room = Room("You are standing outside on a farm. The corn is tall and green.\n"
                "Clouds fill the sky and the noise of distant tractors fill your ears.\n"
                "The wind ruffles the leaves in the trees and you see squirrels running.\n"
                "There is an old red barn to the east. The door is slide open.\n"
                "Paint is beginning to chip off of it causing it to look rundown.\n"
                "To the west there is a white ranch style house.\n"
                "North of you is a corn field.",
                13, 10, None, 1, None, None, None, None, None, None)
    room_list.append(room)

    room = Room("You're standing in an entry way. The light is dim and pictures of landscapes line the wall.\n"
                "The tile floor is covered in dirt spots most likely leftover from work boots.\n"
                "You are met with three different hallways to the north, south, and west.\n"
                "The door to the east leads you back outside.",
                2, 0, 5, 8, None, None, None, None, None, None)
    room_list.append(room)

    room = Room("You entered a long hallway. There is no overhead lighting.\n"
                "You can make out the outlines of clay statues that line the wall.\n"
                "There is a door on the west side of the hall.\n"
                "An arch way on the east wall leads into the living room.\n"
                "Stairs along the left side of the hall lead to the basement.",
                None, 3, 1, 9, None, 12, None, None, None, None)
    room_list.append(room)

    room = Room("You are standing in the living room.\n"
                "There is a large window that has a view of the corn field outside.\n"
                "There is a TV, a couch, and multiple chairs.\n"
                "The remote is sitting by the couch.\n"
                "There are no other exits out of the living room besides the way you came.",
                None, None, None, 2, None, None, None, None, None, None)
    room_list.append(room)

    room = Room("You are standing in the kitchen. Pots and pans line the counter of last night's dinner.\n"
                "The fruit bowl is sitting on the table. Flies have begun to gather around the rotting fruit.\n"
                "Spoons have been spilled and now cover the floor.\n"
                "You can enter back into the hallway by heading west.",
                None, None, None, 5, None, None, None, None, None, None)
    room_list.append(room)

    room = Room("You are in a hallway. Light is shining through the small window on the south wall.\n"
                "The hard tile floor is clean and looks recently redone.\n"
                "You can smell something like rotten eggs behind the east door.\n"
                "There is a door on the west wall.\n"
                "The north archway leads back to the entry way.",
                1, 4, None, 6, None, None, None, None, None, None)
    room_list.append(room)

    room = Room("You are in the guest bedroom.\n"
                "There is a small twin bed and a dresser that is missing the bottom drawer.\n"
                "A brown suitcase is sitting in the corner. Above the suitcase there is a cracked window.\n"
                "You can head east into the hallway.",
                None, 5, None, None, None, None, None, None, None, None)
    room_list.append(room)

    room = Room("You are standing in the master bedroom. The king size bed is a mess.\n"
                "Cloths are scattered throughout the room.\n"
                "You can head north back into the hallway",
                8, None, None, None, None, None, None, None, None, None)
    room_list.append(room)

    room = Room("You are standing in a hallway. 18th century paintings lines the walls. \n"
                "There are doors to your north and south.\n"
                "You can also head east down a hallway.",
                9, 1, 7, None, None, None, None, None, None, None)
    room_list.append(room)

    room = Room("You are in the office. There is desk that is neatly organized.\n"
                "There is a stapler and a copier on the desk.\n"
                "Book shelves full of large text books line the walls.\n"
                "There are two exists on the south and east wall.",
                None, 2, 8, None, None, None, None, None, None, None)
    room_list.append(room)

    room = Room("You are standing in the barn. The air is still.\n"
                "Dim lights in the rafter show dust sitting in the air.\n"
                "Hay is lining the floor and the smell of animals fill the air.\n"
                "There is an empty horse stable and you see mice running in and out of holes in the walls.\n"
                "There is a ladder on the back wall that leads up to the loft. ",
                None, None, None, 0, 11, None, None, None, None, None)
    room_list.append(room)

    room = Room("You are in the old hay loft. The floor is filled with cracked boards.\n"
                "There is some loose twine hanging from the rafters above you.\n"
                "",
                None, None, None, None, None, 10, None, None, None, None)
    room_list.append(room)

    room = Room("You are standing in the basement. It is cold and damp.\n"
                "Cobwebs line the ceiling.",
                None, None, None, None, 2, None, None, None, None, None)
    room_list.append(room)

    room = Room("You have entered the corn field. It can be tricky to navigate through.\n"
                "The yard is to your south. You can go deeper into the field by going north, northeast, or northwest.",
                15, None, 0, None, None, None, 16, 14, None, None) # 13
    room_list.append(room)

    room = Room("You have entered deeper into the corn field.\n"
                "You can go deeper into the field by going north, northeast, or northwest.",
                17, None, None, None, None, None, None, None, 13, 24) # 14
    room_list.append(room)

    room = Room("15 You have entered deeper into the corn field.\n"
                "You can go deeper into the field by going north, northeast, or northwest.",
                19, None, 13, None, None, None, None, 25, None, None)  # 15
    room_list.append(room)

    room = Room("16 You have entered deeper into the corn field.\n"
                "You can go deeper into the field by going north, northeast, or northwest.",
                20, None, 23, None, None, None, 21, None, 22, 13)  # 16
    room_list.append(room)

    room = Room("17 You have entered deeper into the corn field.\n"
                "You can go deeper into the field by going north, northeast, or northwest.",
                25, None, 14, None, None, None, None, 18, None, None)  # 17
    room_list.append(room)

    room = Room("18 You have entered deeper into the corn field.\n"
                "You can go deeper into the field by going north, northeast, or northwest.",
                None, 25, 24, None, None, None, None, None, 17, None)  # 18
    room_list.append(room)

    room = Room("19 You have entered deeper into the corn field.\n"
                "You can go deeper into the field by going north, northeast, or northwest.",
                None, None, 15, 25, None, None, None, None, 20, None)  # 19
    room_list.append(room)

    room = Room("20 You have entered deeper into the corn field.\n"
                "You can go deeper into the field by going north, northeast, or northwest.",
                None, 21, 16, None, None, None, None, 20, None, None)  # 20
    room_list.append(room)

    room = Room("21 You have entered deeper into the corn field.\n"
                "You can go deeper into the field by going north, northeast, or northwest.",
                None, None, 22, 20, None, None, None, None, None, 16)  # 21
    room_list.append(room)

    room = Room("22 You have entered deeper into the corn field.\n"
                "You can go deeper into the field by going north, northeast, or northwest.",
                21, None, None, None, None, None, None, 16, None, 23)  # 22
    room_list.append(room)

    room = Room("23 You have entered deeper into the corn field.\n"
                "You can go deeper into the field by going north, northeast, or northwest.",
                16, None, None, None, None, None, 22, None, None, None)  # 23
    room_list.append(room)

    room = Room("24 You have entered deeper into the corn field.\n"
                "You can go deeper into the field by going north, northeast, or northwest.",
                18, None, None, None, None, None, 14, None, None, None)  # 24
    room_list.append(room)

    room = Room("25 You have entered deeper into the corn field.\n"
                "You can go deeper into the field by going north, northeast, or northwest.",
                None, 19, 17, 18, None, None, None, None, 15, None)  # 25
    room_list.append(room)

    # Items
    item_list = []
    item = Item("A blue stapler is sitting on the desk")
    item_list.append(item)

    current_room = 0
    done = False

    while not done:
        print()
        print(room_list[current_room].description)
        user_input = input("What do you want to do? ")

        # When the user wants to go north.
        if user_input.lower() == "n" or user_input.lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # When the user wants to go east.
        elif user_input.lower() == "e" or user_input.lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # When the user wants to go south.
        elif user_input.lower() == "s" or user_input.lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # When the user wants to head west.
        elif user_input.lower() == "w" or user_input.lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # When the user wants to go up
        elif user_input.lower() == "u" or user_input.lower() == "up":
            next_room = room_list[current_room].up
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # When the user wants to go down.
        elif user_input.lower() == "d" or user_input.lower() == "down":
            next_room = room_list[current_room].down
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # When the user wants to head northeast.
        elif user_input.lower() == "ne" or user_input.lower() == "northeast":
            next_room = room_list[current_room].northeast
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # When the user wants to head northwest.
        elif user_input.lower() == "nw" or user_input.lower() == "northwest":
            next_room = room_list[current_room].northwest
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # When the user wants to head southeast.
        elif user_input.lower() == "se" or user_input.lower() == "southeast":
            next_room = room_list[current_room].southeast
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # When the user wants to head southwest.
        elif user_input.lower() == "sw" or user_input.lower() == "southwest":
            next_room = room_list[current_room].southwest
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # When the user wants to quit the game.
        elif user_input.lower() == "q" or user_input.lower() == "quit":
            done = True
            print("See you some other time.")

        # The user selects an option that does not exist.
        else:
            print("error: please pick again.")


main()
