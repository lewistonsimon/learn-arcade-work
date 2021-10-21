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
    room = Room("You are standing outside a farm house. The corn is tall and green.\n"
                "Clouds fill the sky and the noise of distant tractors fill your ears.\n"
                "The wind ruffles the leaves in the trees and you see squirrels running.\n"
                "There is an old red barn to the east. Paint is beginning to chip off of it.\n"
                "To the west there is a white ranch style house. The door is cracked open a little.",
                None, 10, None, 1)
    room_list.append(room)
    room = Room("You're standing in an entry way. The light is dim and pictures of landscapes line the wall.\n"
                "The tile floor is covered in dirt spots most likely leftover from work boots.\n"
                "You are met with three different hallways to the north, south, and west.\n"
                "The door to the east leads you back outside.",
                2, 0, 5, 8)
    room_list.append(room)
    room = Room("You entered a long hallway. There is no overhead lighting.\n"
                "You can make out the outlines of clay statues that line the wall.\n"
                "There is a door on the west side of the hall.\n"
                "An arch way on the east wall leads into the living room.",
                None, 3, 1, 9)
    room_list.append(room)
    room = Room("You are standing in the living room.\n"
                "There is a large window that has a view of the corn field outside.\n"
                "There is a TV, a couch, and multiple chairs.\n"
                "The remote is sitting by the couch.\n"
                "There are no other exits out of the living room besides the way you came.",
                None, None, None, 2)
    room_list.append(room)
    room = Room("You are standing in the kitchen. Pots and pans line the counter of last nights dinner.\n"
                "The fruit bowl is sitting on the table. Flies have begun to gather around the rotting fruit.\n"
                "Spoons have been spilled and now cover the floor.\n"
                "You can enter back into the hallway by heading west.",
                None, None, None, 5)
    room_list.append(room)
    room = Room("You are in a hallway. Light is shining through the small window on the south wall.\n"
                "The hard tile floor is clean and looks recently redone.\n"
                "You can smell something like rotten eggs behind the east door.\n"
                "To the west is a guest bedroom.\n"
                "The north archway leads back to the entry way.",
                1, 4, None, 6)
    room_list.append(room)
    room = Room("You are in the guest bedroom.\n"
                "There is a small twin bed and a dresser that is missing the bottom drawer.\n"
                "A brown suitcase is sitting in the corner. Above the suitcase there is a cracked window.\n"
                "You can head east into the hallway.",
                None, 5, None, None)
    room_list.append(room)
    room = Room("You are standing in the master bedroom. The king size bed is a mess.\n"
                "Cloths are scattered throughout the room.\n"
                "You can head north back into the hallway",
                8, None, None, None)
    room_list.append(room)
    room = Room("You are standing in a hallway. 18th century paintings lines the walls. \n"
                "You can head south into the master bedroom.\n"
                "You can head north into the office or can head east down a hallway.",
                9, 1, 7, None)
    room_list.append(room)
    room = Room("You are in the office. There is desk that is neatly organized.\n"
                "There is a stapler and a copier on the desk.\n"
                "Book shelves full of large text books line the walls.\n"
                "There are two exists on the south and east wall.",
                None, 2, 8, None)
    room_list.append(room)
    room = Room("You are standing in the barn. The air is still.\n"
                "Dim lights in the rafter show dust sitting in the air.\n"
                "Hay is lining the floor and the smell of animals fill the air.\n"
                "There is an empty horse stable and you see mice running in and out of holes in the walls.\n"
                "There is not much to do. You can go west and end up back outside.",
                None, None, None, 0)
    room_list.append(room)

    current_room = 0
    done = False

    while not done:
        print()
        print(room_list[current_room].description)
        user_input = input("What do you want to do? ")
        if user_input.lower() == "n" or user_input.lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room
                print(current_room)

        elif user_input.lower() == "e" or user_input.lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "s" or user_input.lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "w" or user_input.lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "q" or user_input.lower() == "quit":
            done = True
            print("See you some other time.")

        else:
            print("error: please pick again.")


main()
