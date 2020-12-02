def find_kth_smallest_element(arr, k):
    arr.sort()
    return arr[k - 1]


def find_kth_max_element(arr, k):
    arr.sort()
    print(arr)
    return arr[k - 1]


# print(find_kth_smallest_element([21, 22, 1, 5, 4, 65, 7], 2))
print(find_kth_max_element([21, 22, 1, 5, 4, 65, 7], 2))
