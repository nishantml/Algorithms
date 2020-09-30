def array1(arr):
    print('head -> ', arr[0])
    middle = len(arr) // 2
    if len(arr) % 2 == 0:
        print('middle -> ', arr[middle - 1:middle + 1])
    else:
        print('middle -> ', arr[middle])
    print('tail ->  ', arr[-1])


array1(["eyes", "nose", "lips", "ears"])
array1(["eyes", "nose", "lips", "ears", "legs"])
