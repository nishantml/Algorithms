def array_union(arr1, arr2):
    union_array = []
    for i in range(max(len(arr1), len(arr2))):
        if i < len(arr1):
            if arr1[i] not in union_array:
                union_array.append(arr1[i])

        if i < len(arr2):
            if arr2[i] not in union_array:
                union_array.append(arr2[i])
    print(union_array)


def array_intersection(arr1, arr2):
    intersection_array = []
    for i in range(len(arr1)):
        if arr1[i] in arr2:
            intersection_array.append(arr1[i])
    print(intersection_array)


# array_union([1, 2, 3], [3, 4, 5])
array_union([1, 3, 4, 5, 7], [2, 3, 5, 6])
array_intersection([1, 3, 4, 5, 7], [2, 3, 5, 6])
