def find_min_max_value_type_1(arr):
    min_val = arr[0]
    max_val = arr[0]

    for i in range(len(arr)):
        if arr[i] >= max_val:
            max_val = arr[i]
        if arr[i] <= min_val:
            min_val = arr[i]
    print(min_val)
    print(max_val)


# find_min_max_value_type_1([13, 2, 4, 5, 3, 0, 12])

# find_min_max_value_type_1([13])


def find_min_max_value(low, high, arr):
    # divide and conquer method
    min_value = arr[low]
    max_value = arr[low]

    if low == high:
        return min_value, max_value

    elif low + 1 == high:
        if arr[low] > arr[high]:
            min_value = arr[high]
            max_value = arr[low]
        else:
            min_value = arr[low]
            max_value = arr[high]

        return min_value, max_value
    else:
        mid = (low + high) // 2
        min_value_1, max_value_1 = find_min_max_value(low, mid, arr)
        min_value_2, max_value_2 = find_min_max_value(mid + 1, high, arr)

    return min(min_value_1, min_value_2), max(max_value_1, max_value_2)


data = [13]
low = 0
high = len(data) - 1
print(find_min_max_value(low, high, data))
