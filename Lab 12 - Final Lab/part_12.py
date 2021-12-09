import random

from create_rooms import create_rooms
from create_items import create_items
from create_enemy import create_enemy


def main():
    # Introduction
    print("Welcome to the Colson Family Farm.")
    print("The locals have not heard much from them recently.")
    print("You have been sent to their property to find out information.")

    room_list = create_rooms()
    item_list = create_items()
    enemy_list = create_enemy()

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

        # If the user runs into an enemy.
        for enemy in enemy_list:
            if enemy.room_number == current_room:
                if player_health >= 1:
                    player_health -= 1
                    print(f"You were injured by {enemy.name}.")
                else:
                    print(f"You were killed by the {enemy.name}.")
                    done = True


main()
