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
my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]


def insertion_sort(my_list):
    for key_pos in range(1, len(my_list)): # 100
        key_value = my_list[key_pos]
        scan_pos = key_pos - 1
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value): # worse - average 50, not worse case - average 50
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos -= 1

        my_list[scan_pos + 1] = key_value


insertion_sort(my_list)
print(my_list)

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