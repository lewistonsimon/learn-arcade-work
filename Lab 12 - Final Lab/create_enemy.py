from enemy import Enemy


def create_enemy():
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

    return enemy_list