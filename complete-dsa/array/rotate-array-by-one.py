def rotate_array_by_one(arr):
    new_arr = [arr[-1]]
    for i in range(len(arr) - 1):
        new_arr.append(arr[i])

    print(new_arr)


def rotate(arr, n):
    if len(arr) < n:
        print('Value of n should ne less than or equal to array size')
        return
    right_shift = arr[:n]
    left_shift = arr[n:]

    right_shift_start = len(arr) - n
    for i in range(right_shift_start):
        arr[i] = left_shift[i]

    count = 0
    for j in range(right_shift_start, len(arr)):
        arr[j] = right_shift[count]
        count += 1

    print(arr)


rotate([1, 2, 3, 4, 5], 4)
