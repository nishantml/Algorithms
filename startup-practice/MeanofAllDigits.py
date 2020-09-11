def Mean_of_All_Digits(num):
    arr = []
    n = num
    while n > 0:
        r = n % 10
        n = n // 10
        arr.append(r)
    return sum(arr)//len(arr)


print(Mean_of_All_Digits(42))
print(Mean_of_All_Digits(12345))
print(Mean_of_All_Digits(666))