from room import Room


def create_rooms():
    # Rooms
    room_list = []

    # Room 0
    room = Room("You are standing outside on a farm. The corn is tall and green.\n"
                "Clouds fill the sky and the noise of distant tractors fill your ears.\n"
                "The wind ruffles the leaves in the trees and you see squirrels running around the yard.\n"
                "There is an old red barn to the east. The door is slide open.\n"
                "Paint is beginning to chip off of it causing it to look rundown.\n"
                "To the west there is a white ranch style house.\n"
                "North of you is a corn field.",
                13, 10, None, 1, None, None, None, None, None, None)
    room_list.append(room)

    # Room 1
    room = Room("You're standing in an entry way. The light is dim and pictures of landscapes line the wall.\n"
                "The tile floor is covered in dirt spots most likely leftover from work boots.\n"
                "You are met with three different hallways to the north, south, and west.\n"
                "The door to the east leads you back outside.",
                2, 0, 5, 8, None, None, None, None, None, None)
    room_list.append(room)

    # Room 2
    room = Room("You entered a long hallway. There is no overhead lighting.\n"
                "You can make out the outlines of clay statues that line the wall.\n"
                "There is a door on the west side of the hall.\n"
                "An arch way on the east wall leads into the living room.\n"
                "Stairs along the left side of the hall lead to the basement.",
                None, 3, 1, 9, None, 12, None, None, None, None)
    room_list.append(room)

    # Room 3
    room = Room("You are standing in the living room.\n"
                "There is a large window that has a view of the corn field outside.\n"
                "There is a TV, a couch, and multiple chairs.\n"
                "The remote is sitting by the couch.\n"
                "There are no other exits out of the living room besides the way you came.",
                None, None, None, 2, None, None, None, None, None, None)
    room_list.append(room)

    # Room 4
    room = Room("You are standing in the kitchen. Pots and pans line the counter from a previous dinner.\n"
                "The fruit bowl is sitting on the table. Flies have begun to gather around the rotting fruit.\n"
                "Silverware has been spilled and now cover the floor.\n"
                "A sink is on the far wall of the kitchen.\n"
                "You can enter back into the hallway by heading west.",
                None, None, None, 5, None, None, None, None, None, None)
    room_list.append(room)

    # Room 5
    room = Room("You are in a hallway. Light is shining through the small window on the south wall.\n"
                "The hard tile floor is clean and looks recently redone.\n"
                "You can smell something like rotten eggs behind the east door.\n"
                "There is a door on the west wall.\n"
                "The north archway leads back to the entry way.",
                1, 4, None, 6, None, None, None, None, None, None)
    room_list.append(room)

    # Room 6
    room = Room("You are in the guest bedroom.\n"
                "There is a small twin bed and a dresser that is missing the bottom drawer.\n"
                "A brown suitcase is sitting in the corner. Above the suitcase there is a cracked window.\n"
                "You can head east into the hallway.",
                None, 5, None, None, None, None, None, None, None, None)
    room_list.append(room)

    # Room 7
    room = Room("You are standing in the master bedroom. The king size bed is a mess.\n"
                "Cloths are scattered throughout the room.\n"
                "You can head north back into the hallway",
                8, None, None, None, None, None, None, None, None, None)
    room_list.append(room)

    # Room 8
    room = Room("You are standing in a hallway. 18th century paintings lines the walls. \n"
                "There are doors to your north and south.\n"
                "You can also head east down a hallway.",
                9, 1, 7, None, None, None, None, None, None, None)
    room_list.append(room)

    # Room 9
    room = Room("You are in the office. There is desk that is neatly organized.\n"
                "There is a lamp on the desk.\n"
                "Book shelves full of large text books line the walls.\n"
                "There are two exists on the south wall and east wall.",
                None, 2, 8, None, None, None, None, None, None, None)
    room_list.append(room)

    # Room 10
    room = Room("You are standing in the barn. The air is still.\n"
                "Dim lights in the rafter show dust sitting in the air.\n"
                "Hay is lining the floor and the smell of animals fill the air.\n"
                "There is an empty horse stable and you see mice running in and out of holes in the walls.\n"
                "There is a ladder on the back wall that leads up to the loft. ",
                None, None, None, 0, 11, None, None, None, None, None)
    room_list.append(room)

    # Room 11
    room = Room("You are in the old hay loft. The floor is filled with cracked boards.\n"
                "There is some loose twine hanging from the rafters above you.",
                None, None, None, None, None, 10, None, None, None, None)
    room_list.append(room)

    # Room 12
    room = Room("You are standing in the basement. It is cold and damp.\n"
                "Cobwebs line the ceiling.",
                None, None, None, None, 2, None, None, None, None, None)
    room_list.append(room)

    # Room 13
    room = Room("You are standing right inside the corn field. You can see the blue sky above you.\n"
                "The yard is to your south. You can go deeper into the field by going north, northeast, or northwest.\n"
                "You can also walk the front fence line to the east or west.",
                15, 23, 0, 24, None, None, 16, 14, None, None)
    room_list.append(room)

    # Room 14
    room = Room("The corn is getting thick and everything looks the same.\n"
                "You can continue by going north, southeast, or southwest.",
                17, None, None, None, None, None, None, None, 13, 24)
    room_list.append(room)

    # Room 15
    room = Room("The corn is getting thick and everything looks the same.\n"
                "You can continue by going north, south, northeast, or northwest.",
                19, None, 13, None, None, None, 20, 25, None, None)
    room_list.append(room)

    # Room 16
    room = Room("The corn is getting thick and everything looks the same.\n"
                "You can continue by going north, south, northeast, southeast, or southwest.",
                20, None, 23, None, None, None, 21, None, 22, 13)
    room_list.append(room)

    # Room 17
    room = Room("The corn is getting thick and everything looks the same.\n"
                "You can continue by going north, south, northeast, or northwest.",
                25, None, 14, None, None, None, 19, 18, None, None)
    room_list.append(room)

    # Room 18
    room = Room("You are standing in the far corner of the corn field.\n"
                "You can continue by going east, south, or southeast.",
                None, 25, 24, None, None, None, None, None, 17, None)
    room_list.append(room)

    # Room 19
    room = Room("You are standing along the fence line at the opposite end of the property.\n"
                "You can continue by going south, southeast, southwest, or west.",
                None, None, 15, 25, None, None, None, None, 20, 17)
    room_list.append(room)

    # Room 20
    room = Room("The corn is getting thick and everything looks the same.\n"
                "You can continue by going east, south, northwest, or southwest.",
                None, 21, 16, None, None, None, None, 19, None, 15)
    room_list.append(room)

    # Room 21
    room = Room("You are standing on the east side of the field.\n"
                "You can continue by going south, west, or southwest.",
                None, None, 22, 20, None, None, None, None, None, 16)
    room_list.append(room)

    # Room 22
    room = Room("You are standing on the east side of the field.\n"
                "You can continue by going north, northwest, or southwest.",
                21, None, None, None, None, None, None, 16, None, 23)
    room_list.append(room)

    # Room 23
    room = Room("You are standing along the front fence of the field that prevents you from going south.\n"
                "You can just make out the top of the house to the southwest.\n"
                "You can continue by going north, west, or northeast.",
                16, None, None, 13, None, None, 22, None, None, None)
    room_list.append(room)

    # Room 24
    room = Room("You are standing along the front fence of the field that prevents you from going south.\n"
                "You can barley see the top of the barn over the corn in the distant east.\n"
                "You can continue by going north, east, or northeast.",
                18, 13, None, None, None, None, 14, None, None, None)
    room_list.append(room)

    # Room 25
    room = Room("You are standing along the fence line at the opposite end of the property.\n"
                "You can continue by going east, south, west, or southeast.",
                None, 19, 17, 18, None, None, None, None, 15, None)
    room_list.append(room)

    return room_list
