import math as Math


def mergeSort(array):
    """call itself to divide the array till the size becomes one"""
    if len(array) == 1:
        return array
    #    Split Array in into right and left from the middle
    length = len(array)
    middle = Math.floor(length / 2)
    left = array[0:middle]
    right = array[middle:]
    # print('left:', left);
    # print('right:', right);

    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    """this is used for merging two halves """
    # print('inside Merge ')
    result = [];
    leftIndex = 0;
    rightIndex = 0;
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1
        # print('merge', left, right)
        # print('result', result)
        # print('left elements ->', left[leftIndex:] + right[rightIndex:])
    # Checking if any element was left
    return result + left[leftIndex:] + right[rightIndex:]


print(mergeSort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]))
