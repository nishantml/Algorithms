def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            print('Data found at index ', i)
            return
    print('Data not found ')
    return


linear_search([3, 2, 3, 5, 6, 7, 1], 7)
