from enemy import Enemy


def create_enemy():
    # Enemies
    enemy_list = []

    enemy = Enemy("A scarecrow is staring at you.\n"
                  "It seems to be following you with its eyes. It notices you.\n"
                  "It says, \"You have entered my corn field. You need an offering to continue.\"\n"
                  "If you do not have an offering you will die.",
                  "scarecrow", 16, 9)
    enemy_list.append(enemy)

    enemy = Enemy("A coyote is attacking you!", "coyote", 18, 15)
    enemy_list.append(enemy)

    enemy = Enemy("A rat is staring at you.",
                  "rat", 12, 2)
    enemy_list.append(enemy)

    return enemy_list
