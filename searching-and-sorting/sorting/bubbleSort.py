def bubbleSort(arr):
    size = len(arr)
    for i in range(size):
        for j in range(0, size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [3, 2, 1, 4, 5, 3, 65, 2, 45, 23, 21, 44, 100]
print(bubbleSort(arr))
