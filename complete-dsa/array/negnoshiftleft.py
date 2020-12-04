def neg_no_shift_left(arr):
    # Time complexity: O(N)
    curr = 0
    for i in range(len(arr)):
        print(curr, i)
        if arr[i] < 0:
            temp = arr[i]
            arr[i] = arr[curr]
            arr[curr] = temp
            curr += 1
    print(arr)


neg_no_shift_left([-12, 11, -3, -2, 1, 6, -13])
