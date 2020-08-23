def binary_search(arr, key, start, end):
    while start <= end:
        mid = (start + end) // 2  # taking floor value
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            end = mid - 1
            return binary_search(arr, key, start, end)
        else:
            start = mid + 1
            return binary_search(arr, key, start, end)

    return -1


def exponentialSearch(A, item, size):
    if A[0] == item:
        return 0

    i = 1

    while i < size and A[i] <= item:
        i = i * 2

    return binary_search(A, item, i // 2, min(i, size))


arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
size = len(arr)
print(exponentialSearch(arr, 610, size))
