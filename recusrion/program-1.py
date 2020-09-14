def fun1(x):
    if x > 0:
        print(x)
        fun1(x - 1)
    print('completed the setup now returning')


fun1(3)
