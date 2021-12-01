# insertion sort
# 15 57 14 33 72 79 26 56 42 40
# 15 57 14 33 72 79 26 56 42 40
# 14 15 57 33 72 79 26 56 42 40
# 14 15 33 57 72 79 26 56 42 40
# 14 15 33 57 72 79 26 56 42 40
# 14 15 33 57 72 79 26 56 42 40
# 14 15 26 33 57 72 79 56 42 40
# 14 15 26 33 56 57 72 79 42 40
# 14 15 26 33 42 56 57 72 79 40
# 14 15 26 33 40 42 56 57 72 79

# does not scan it finds the next number and moves it to where it belongs
# my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
#
#
#
# def insertion_sort(my_list):
#     for key_pos in range(1, len(my_list)): # 100
#         key_value = my_list[key_pos]
#         scan_pos = key_pos - 1
#         while (scan_pos >= 0) and (my_list[scan_pos] > key_value): # worse - average 50, not worse case - average 50
#             my_list[scan_pos + 1] = my_list[scan_pos]
#             scan_pos -= 1
#
#         my_list[scan_pos + 1] = key_value
#
#
# insertion_sort(my_list)
# print(my_list)

# insertion sort, worse case
# n = 10, 10 * 5 = 50
# n = 100, 100 * 50 = 50
# n * (n/2) = n^2 / 2


# insertion sort, average case
# n = 10, 10 * 2.5 = 25
# n = 100, 100 * 14 = 2,500
# n * (n/4) = n^2 / 4

# insertion sort, best case
# n = 10, 10 * 1 = 10
# n = 100, 100 * 1 = 100


import random


def selection_sort(my_list):
    """ Sort a list using the selection sort """

    outside_loop = 0
    inside_loop = 0

    # Loop through the entire array
    for cur_pos in range(len(my_list)):
        outside_loop += 1
        # Find the position that has the smallest number
        # Start with the current position
        min_pos = cur_pos

        # Scan left to right (end of the list)
        for scan_pos in range(cur_pos + 1, len(my_list)):
            inside_loop += 1

            # Is this position smallest?
            if my_list[scan_pos] < my_list[min_pos]:
                # It is, mark this position as the smallest
                min_pos = scan_pos

        # Swap the two values
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp
    print(outside_loop)
    print(inside_loop)


def insertion_sort(my_list):
    """ Sort a list using the insertion sort """

    inside_loop = 0
    outside_loop = 0

    # Start at the second element (pos 1).
    # Use this element to insert into the
    # list.
    for key_pos in range(1, len(my_list)):
        outside_loop += 1

        # Get the value of the element to insert
        key_value = my_list[key_pos]

        # Scan from right to the left (start of list)
        scan_pos = key_pos - 1

        # Loop each element, moving them up until
        # we reach the position the
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):
            inside_loop += 1
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos = scan_pos - 1

        # Everything's been moved out of the way, insert
        # the key into the correct location
        my_list[scan_pos + 1] = key_value
    print(outside_loop)
    print(inside_loop)


# This will point out a list
# For more information on the print formatting {:3}
# see the chapter on print formatting.
def print_list(my_list):
    for item in my_list:
        print(f"{item:3}", end="")
    print()


def main():
    # Create two lists of the same random numbers
    list_for_selection_sort = []
    list_for_insertion_sort = []
    list_size = 100
    for i in range(list_size):
        new_number = random.randrange(100)
        list_for_selection_sort.append(new_number)
        list_for_insertion_sort.append(new_number)

    # Print the original list
    print("Original List")
    print_list(list_for_selection_sort)

    # Use the selection sort and print the result
    print("Selection Sort")
    selection_sort(list_for_selection_sort)
    print_list(list_for_selection_sort)

    # Use the insertion sort and print the result
    print("Insertion Sort")
    insertion_sort(list_for_insertion_sort)
    print_list(list_for_insertion_sort)


main()
