import math


def jumpSearch(arr, item, n):
    # Finding block size to be jumped
    step = int(math.sqrt(n))

    # Finding the block where element is
    # present (if it is present)
    prev = 0
    while arr[min(step, n) - 1] < item:
        print('min', min(step, n) - 1)
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Doing a linear search for item in
    # block beginning with prev.
    while arr[prev] < item:
        prev += 1

        # If we reached neitemt block or end
        # of array, element is not present.
        if prev == min(step, n):
            return -1

    # If element is found
    if arr[int(prev)] == item:
        return prev

    return -1


arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
size = len(arr)
print(jumpSearch(arr, 610, size))

# Credit GFG
