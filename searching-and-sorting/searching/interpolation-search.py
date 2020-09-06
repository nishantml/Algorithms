def interpolationSearch(A, item, size):
    lo = 0
    hi = size - 1

    while lo < hi and A[lo] <= item <= A[hi]:

        if lo == hi:
            if arr[lo] == item:
                return lo
            return -1

        pos = lo + int(((float(hi - lo) /
                         (arr[hi] - arr[lo])) * (item - arr[lo])))

        if A[pos] == item:
            return pos

        if A[pos] < item:
            lo = pos + 1

        else:
            hi = pos - 1

    return -1


arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
size = len(arr)
print(interpolationSearch(arr, 1, size))
