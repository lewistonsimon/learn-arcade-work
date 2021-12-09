from item import Item


def create_items():
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

    return item_list
