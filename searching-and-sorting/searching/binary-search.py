def binary_search(arr, size, key):
    if key > arr[-1]:
        return -1

    start = 0
    end = size - 1

    while start <= end:
        mid = (start + end) // 2  # taking floor value
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1


sorted_array = [2, 3, 4, 5, 6, 7]
print(binary_search(sorted_array, len(sorted_array), 7))
