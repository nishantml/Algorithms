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


sorted_array = [2, 3, 4, 5, 6, 7]
print(binary_search(sorted_array, 7, 0, len(sorted_array) - 1))
