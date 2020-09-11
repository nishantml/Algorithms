def unique_num(arr):
    new = []
    for val in arr:
        if val not in new:
            new.append(val)
    return new


print(unique_num([2, 3, 3, 2, 1, 4, 5]))
