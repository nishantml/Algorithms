"""
Sorted Array
"""


def sorted_array(lst, val):
    if len(lst) == 0:
        return [val]

    if lst[-1] < val:
        lst.append(val)
        return lst

    for i in range(len(lst)):
        if lst[i] > val:
            break
    return lst[:i] + [val] + lst[i:]


arr = [4, 2, 3, 1, 5, 8]

sortedLst = []
for k in arr:
    sortedLst = sorted_array(sortedLst, k)
    # print(sortedLst)

print('Final List ', sortedLst)
