# Sorting Items

my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
# print(my_list)
#
# # Swap the 15 and 14
# temp = my_list[0]
# my_list[0] = my_list[2]
# my_list[2] = temp
#
# print(my_list)

# can also do, only in python
# my_list[0], my_list[2] = my_list[2], my_list[0]
# print(my_list)

# 15 57 14 33 72 79 26 56 42 40
# have a varible hold a small number
# see if the number next to it is larger than the previous one
# if it is smaller swap where it needs to be

# start
# 15 57 14 33 72 79 26 56 42 40

# 14 is the smallest swap to pos 0
# 14 57 15 33 72 79 26 56 42 40

# 15 is the next smallest swap to pos 1
# 14 15 57 33 72 79 26 56 42 40
# ect...

# This is the SELECTION sort. I am SELECTING the smallest and swapping

# code for selection sort


def selection_sort(my_list):
    for cur_pos in range(len(my_list)):
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(my_list)):
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos
        # Swap
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp


selection_sort(my_list)
print(my_list)

# n = 10, outside loop run 100, inside runs average of 50, 100 * 50 = 5000
# n * (n / 2) same as n^2 / 2



