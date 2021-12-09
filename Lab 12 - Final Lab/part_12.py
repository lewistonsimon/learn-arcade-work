import random

from item import Item
from room import Room
from enemy import Enemy


def main():
    # Introduction
    print("Welcome to the Colson Family Farm.")
    print("The locals have not heard much from them recently.")
    print("You have been sent to their property to find out information.")

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

    # Room 26

    # Items
    item_list = []

    item = Item("A blue stapler is here.", "stapler", 9)
    item_list.append(item)

    item = Item("There is a compass here.", "compass", 3)
    item_list.append(item)

    item = Item("There is a knife here.", "knife", 7)
    item_list.append(item)

    item = Item("Food is here.", "food", 4)
    item_list.append(item)

    item = Item("A bent fork is on the ground.", "fork", 4)
    item_list.append(item)

    item = Item("A bucket is sitting on the ground.", "bucket", 10)
    item_list.append(item)

    item = Item("Hay twine is here.", "twine", 11)
    item_list.append(item)

    item = Item("Corn is here.", "corn", 13)
    item_list.append(item)

    item = Item("An old key is here.", "key", 6)
    item_list.append(item)

    item = Item("A slingshot is here.", "slingshot", 0)
    item_list.append(item)

    # Enemies
    enemy_list = []

    enemy = Enemy("A scarecrow is staring at you.\n"
                  "It seems to be following you with its eyes.\n"
                  "It says, \"You have entered my corn field. You need an offering to continue.\""
                  "If you do not have an offering you will die.",
                  "scarecrow", 16, 5)
    enemy_list.append(enemy)

    enemy = Enemy("A coyote is running towards you!", "coyote", 0, 15)
    enemy_list.append(enemy)

    enemy = Enemy("A rat is staring at you.",
                  "rat", 12, 2)
    enemy_list.append(enemy)

    current_room = 0
    player_health = 5
    done = False
    food_exist = True
    corn_exist = True
    bucket_full = False
    stapler_count = 5
    rock_count = 3

    while not done:
        print()
        print(room_list[current_room].description)
        for item in item_list:
            if item.room_number == current_room:
                print(item.description)
        for enemy in enemy_list:
            if enemy.room_number == current_room:
                print(enemy.description)
        user_command = input("What do you want to do? ")
        command_words = user_command.split(" ")

        # When the user wants to go north.
        if command_words[0].lower() == "n" or command_words[0].lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # When the user wants to go east.
        elif command_words[0].lower() == "e" or command_words[0].lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # When the user wants to go south.
        elif command_words[0].lower() == "s" or command_words[0].lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # When the user wants to head west.
        elif command_words[0].lower() == "w" or command_words[0].lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # When the user wants to go up
        elif command_words[0].lower() == "u" or command_words[0].lower() == "up":
            next_room = room_list[current_room].up
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # When the user wants to go down.
        elif command_words[0].lower() == "d" or command_words[0].lower() == "down":
            next_room = room_list[current_room].down
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # When the user wants to head northeast.
        elif command_words[0].lower() == "ne" or command_words[0].lower() == "northeast":
            next_room = room_list[current_room].northeast
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # When the user wants to head northwest.
        elif command_words[0].lower() == "nw" or command_words[0].lower() == "northwest":
            next_room = room_list[current_room].northwest
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # When the user wants to head southeast.
        elif command_words[0].lower() == "se" or command_words[0].lower() == "southeast":
            next_room = room_list[current_room].southeast
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # When the user wants to head southwest.
        elif command_words[0].lower() == "sw" or command_words[0].lower() == "southwest":
            next_room = room_list[current_room].southwest
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # Get command
        elif command_words[0].lower() == "get" or command_words[0].lower() == "grab":
            if len(command_words) == 1:
                print("What do you want to get?")
                continue
            item_exist = False
            for item in item_list:
                if item.name == command_words[1]:
                    item_exist = True
                    if item.room_number == current_room:
                        item.room_number = -1
                        print(f"You picked up the {item.name}.")
                    else:
                        print(f"The {item.name} is not here.")
            if not item_exist:
                print(f"The {command_words[1]} is not here.")

        # Look at the player's inventory.
        elif command_words[0].lower() == "inventory":
            item_exist = False
            for item in item_list:
                if item.room_number == -1:
                    print(f"You have the {item.name} in your inventory.")

        # Drop an item from a player's inventory.
        elif command_words[0].lower() == "drop":
            if len(command_words) == 1:
                print("What do you want to drop?")
                continue
            item_exist = False
            for item in item_list:
                if item.name == command_words[1]:
                    item_exist = True
                    if item.room_number == -1:
                        item.room_number = current_room
                        print(f"You dropped the {item.name}.")
                    else:
                        print(f"You do not have possession of the {command_words[1]}.")
            if not item_exist:
                print(f"You do not have possession of the {command_words[1]}.")

        # If the user wants to fill the bucket.
        elif command_words[0].lower() == "fill" or command_words[0].lower() == "sink":
            if len(command_words) == 1:
                print("What do you want to fill?")
                continue
            if current_room == 4:
                for item in item_list:
                    if item.name == command_words[1]:
                        if command_words[1] == "bucket":
                            bucket_full = True
                            print(f"The {item.name} is now full of water.")
                        else:
                            print(f"You can not fill the {item.name} with water.")
            else:
                print("There is nowhere to fill anything.")

        # If the user wants to eat the food or the corn.
        elif command_words[0].lower() == "eat":
            if len(command_words) == 1:
                print("What do you want to eat?")
                continue
            item_exist = False
            for item in item_list:
                if item.name == command_words[1]:
                    item_exist = True
                    if item.name == "food":
                        if food_exist:
                            print(f"You ate the {command_words[1]}")
                            food_exist = False
                            item_list.remove(item)
                        else:
                            print("You already ate the food.")
                    if item.name == "corn":
                        if corn_exist:
                            print(f"You ate the {command_words[1]}.")
                            corn_exist = False
                            item_list.remove(item)
                        else:
                            print("You already ate the corn.")
                    else:
                        print(f"You can not eat the {command_words[1]}.")
            if not item_exist:
                print(f"You do not have possession of the {command_words[1]}.")

        # When the user wants to use an item.
        elif command_words[0].lower() == "use":
            if len(command_words) == 1:
                print("What do you want to use?")
                continue
            item_exist = False
            for item in item_list:
                if item.name == command_words[1]:
                    item_exist = True
                    if item.room_number == -1:
                        if command_words[1] == "bucket":
                            if bucket_full is True:
                                print(f"You used the {item.name}.")
                                print(f"The {item.name} is now empty.")
                            else:
                                print("The bucket is empty.")
                                print("You need to fill it before you can use it.")
                        if command_words[1] == "stapler":
                            if stapler_count >= 1:
                                stapler_count -= 1
                                print(f"You used the stapler. There are {stapler_count} staples left.")
                                for enemy in enemy_list:
                                    if current_room == enemy.room_number:
                                        if random.randrange(10) == 0:
                                            enemy.health -= 1
                                            print(f"You hit the {enemy.name}.")
                                            print(enemy.health)
                                            if enemy.health <= 0:
                                                print(f"You killed the {enemy.name}.")
                                        else:
                                            print(f"You missed the {enemy.name}.")
                            else:
                                print("There are no staples left.")
                        if command_words[1] == "slingshot":
                            if rock_count >= 1:
                                rock_count -= 1
                                print(f"You used the slingshot. There are {rock_count} rocks left.")
                                for enemy in enemy_list:
                                    if current_room == enemy.room_number:
                                        if random.randrange(2):
                                            enemy.health -= 3
                                            print(f"You hit the {enemy.name}.")
                                            print(enemy.health)
                                            if enemy.health <= 0:
                                                print(f"You killed the {enemy.name}.")
                                        else:
                                            print(f"You missed the {enemy.name}.")
                            else:
                                print("There are no rocks left.")
                        if command_words[1] == "fork":
                            print(f"You used the {item.name}.")
                        if command_words[1] == "compass":
                            print(f"You used the {item.name}.")
                            user_input = input("Where do you want to go?")
                            if user_input == "room.name":
                                current_room = user_input
                        if command_words[1] == "knife":
                            print(f"You used the {item.name}.")
                            for enemy in enemy_list:
                                if current_room == enemy.room_number:
                                    enemy.health -= 5
                                    print(f"You stabbed the {enemy.name}.")
                                    if enemy.health <= 0:
                                        print(f"You killed the {enemy.name}.")
                        if command_words[1] == "food":
                            print(f"You used the {item.name}.")
                        if command_words[1] == "twine":
                            print(f"You used the {item.name}.")
                        if command_words[1] == "Corn":
                            print(f"You used the {item.name}.")
                        if command_words[1] == "key":
                            if current_room == 12:
                                print(f"You unlocked the door.")
                            else:
                                print("There is nothing to unlock.")
                    else:
                        print(f"You do not have possession of the {command_words[1]}. ")
            if not item_exist:
                print(f"You do not have possession of the {command_words[1]}. ")

        # When the user wants to quit the game.
        elif command_words[0].lower() == "q" or command_words[0].lower() == "quit":
            done = True
            print("See you some other time.")

        # The user selects an option that does not exist.
        else:
            print("error: please pick again.")

        for enemy in enemy_list:
            if enemy.room_number == current_room:
                if player_health >= 1:
                    player_health -= 1
                    print(f"You were injured by {enemy.name}.")
                else:
                    print(f"You were killed by the {enemy.name}.")
                    done = True


main()
