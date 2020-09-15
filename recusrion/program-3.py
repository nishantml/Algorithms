def mult(n):
    if n == 1:
        return n
    else:
        return n * mult(n - 1)


print(mult(7))
