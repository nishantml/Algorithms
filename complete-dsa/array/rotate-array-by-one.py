def rotate_array_by_one(arr):
    new_arr = [arr[-1]]
    for i in range(len(arr) - 1):
        new_arr.append(arr[i])

    print(new_arr)


def rotate(arr, n):
    right_shift = arr[:len(arr) - n]
    left_shift = arr[len(arr) - n:]
    arr[:] = left_shift + right_shift
    print(arr)


rotate([1, 2, 3, 4, 5, 6], 8)
