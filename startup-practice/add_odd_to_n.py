def add_odd_to_n(n):
    sum = 0
    for i in range(1, n + 1, 2):
        sum += i;

    return sum


print(add_odd_to_n(13))
