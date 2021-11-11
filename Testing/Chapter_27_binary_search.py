# binary search

# a number between 1...128
# would take 7 guesses
# a number between 1...256
# would take 8 guesses
# 1...512
# would take 9 guesses


def main():
    my_file = open("super_villains.txt")

    name_list = []
    for line in my_file:
        line = line.strip()
        name_list.append(line)

    my_file.close()

    print(name_list)
    print("There were", len(name_list), "names in the file.")

    # Binary Search
    key = "Octavia the Siren"

    lower_bound = 0
    upper_bound = len(name_list) - 1
    found = False
    while lower_bound <= upper_bound and not found:
        middle_pos = (lower_bound + upper_bound) // 2

        if name_list[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif name_list[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True

    if found:
        print("Found at position: ", middle_pos)

    if not found:
        print("Not Found.")


main()

# worst case binary search
# 128 items take 7 guesses
# 2^7 = 128
# 2^16 = 65536

# 2^? = 1024
# use log2
# log2 1024 = 10

# worst case binary search, in terms of n
# log2(n)
