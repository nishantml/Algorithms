def sort012(arr):
    """using bubble sort"""
    size = len(arr)
    for i in range(size):
        for j in range(0, size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def sort012_1(arr):
    Hash = dict({0: 0, 1: 0, 2: 0})

    for i in arr:
        if i not in Hash:
            Hash[i] = 1
        else:
            Hash[i] = Hash[i] + 1

    num = 0
    iteration = 0
    while num <= 2:
        for i in range(Hash[num]):
            arr[iteration] = num
            iteration += 1
        num += 1

    print(arr)


# print(sort012([0, 2, 1, 2, 0]))
sort012_1([0, 2, 1, 2, 0])
