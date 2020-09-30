def fun1(x):
    if x > 0:
        print(x)
        fun1(x - 1)
    print('completed the setup now returning')


fun1(3)

"""
In Above First printing was done the recursive call was made
Printing was done at calling time that before the function was called 
"""