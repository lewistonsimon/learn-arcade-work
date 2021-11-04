def main():
    my_file = open("super_villains.txt")

    name_list = []
    for line in my_file:
        line = line.strip()
        name_list.append(line)

    my_file.close()

    print(name_list)
    print("There were", len(name_list), "names in the file.")

    # Linear Search
    key = "Octavia the Siren"

    current_list_position = 0
    while current_list_position < len(name_list) and name_list[current_list_position] != key: # position matters
        current_list_position += 1

    if current_list_position < len(name_list):
        print("Found at:", current_list_position)
    else:
        print("Not Found.")


    # If you want to print if you don't find it
    key = "Octavia the Siren"

    current_list_position = 0
    while current_list_position < len(name_list) and name_list[current_list_position] != key:  # position matters
        current_list_position += 1

    if current_list_position == len(name_list):
        print("Not Found.")






main()
