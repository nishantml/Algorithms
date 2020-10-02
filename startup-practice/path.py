from itertools import permutations


def paths(arr):
    return len(list(permutations(arr)))


print(paths([1, 2, 3, 4, 5]))
