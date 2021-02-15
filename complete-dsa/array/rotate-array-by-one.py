def rotate_array_by_one(arr):
    new_arr = [arr[-1]]
    for i in range(len(arr) - 1):
        new_arr.append(arr[i])

    print(new_arr)


def rotate(arr, n):
    if len(arr) < n:
        print('Value of n should ne less than or equal to array size')
        return
    right_shift = arr[:len(arr) - n]
    left_shift = arr[len(arr) - n:]
    # print(right_shift)
    # print(left_shift)

    for i in range(n):
        # print(i)
        arr[i] = left_shift[i]

    count = 0
    for j in range(n, len(arr)):
        arr[j] = right_shift[count]
        count += 1

    print(arr)


rotate([1, 2, 3, 4, 5, 6], 2)
