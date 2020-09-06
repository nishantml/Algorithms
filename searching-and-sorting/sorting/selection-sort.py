def selection_sort(arr):
    for i in range(len(arr) - 1):
        imin = i  # setting the current index as minimum 
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[imin]:
                imin = j;  # update the current index if current index islower than  previous

        temp = arr[i];  # swapping smallerst number at the current starting index one by one 
        arr[i] = arr[imin];
        arr[imin] = temp;
    return arr


arr = [3, 2, 1, 4, 5, 3, 65, 2, 45, 23, 21, 44, 100]
print(selection_sort(arr))
