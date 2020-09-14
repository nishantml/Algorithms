def fun1(x):
    if x > 0:
        fun1(x - 1)
        print(x)
    print('completed the setup now returning')


fun1(3)

"""
In above function recusrive call was done the print out 
In this printing was done at returning time i.e when function was returning to the previous call
"""
