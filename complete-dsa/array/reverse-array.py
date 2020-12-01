def reverse_array_type_1(arr):
    rev_array = []
    for i in reversed(arr):
        rev_array.append(i)
    return rev_array


def reverse_array_type_2(arr):
    # optimal way to reverse array
    start = 0  # initial index value
    last = len(arr) - 1  # last index value

    while start < last:
        arr[start], arr[last] = arr[last], arr[start]
        start += 1
        last -= 1

    return arr


reverse_arr = reverse_array_type_2([1, 2, 3, 4, 5, 6])
print(reverse_arr)
