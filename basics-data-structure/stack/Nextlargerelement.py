

def Nextlargerelement(arr):
    newLst = []
    for i in range(len(arr) - 1):
        maxVal = arr[i]
        valFound = 0
        for j in range(i + 1, len(arr)):
            if maxVal < arr[j]:
                maxVal = arr[j]
                valFound = 1
                break;
        if (valFound == 1):
            newLst.append(maxVal)
        else:
            newLst.append(-1)
        # print(maxVal)
    newLst.append(-1)
    return newLst



print(Nextlargerelement([1 ,3 ,2 ,4]))
print(Nextlargerelement([4 ,3 ,2 ,1]))