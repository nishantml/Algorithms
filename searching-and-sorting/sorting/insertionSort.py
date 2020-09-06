def insertionSort(nums):
    for i in range(len(nums)):
        value = nums[i]
        hole = i - 1
        while hole >= 0 and nums[hole] > value:
            nums[hole + 1] = nums[hole]
            hole -= 1

        nums[hole + 1] = value
    return nums


arr = [3, 2, 1, 4, 5, 3, 65, 2, 45, 23, 21, 44, 100]
print(insertionSort(arr))
