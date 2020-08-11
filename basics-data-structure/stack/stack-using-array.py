"""
Stack is a linear data structure which follows a particular order in which the operations are performed. 
The order may be LIFO(Last In First Out) or FILO(First In Last Out).
"""


class Stack:
    def __init__(self):
        self.array = []
        self.length = 0

    def push(self, data):
        self.array.append(data)
        self.length += 1
        return

    def pop(self):
        poped = self.array[-1]
        self.array.pop(self.length - 1)
        self.length -= 1
        return poped

    def lookup(self):
        for val in reversed(self.array):
            print('-', val)

    def peek(self):
        return self.array[-1]

    def getMin(self):
        print(min(self.array))

    def reverse(self):
        left = 0
        right = self.length-1;
        '''Inplace replacement '''
        while left < right:
            self.array[left],self.array[right] = self.array[right],self.array[left]
            left += 1
            right -= 1

        self.lookup()


myStack = Stack()
print('Length of node is ->', myStack.length)
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(5)
myStack.lookup()
print('Length of node is ->', myStack.length)
# print('Top node is ->', myStack.peek())
# print('Poped node is ->', myStack.pop())
myStack.lookup()
print('Length of node is ->', myStack.length)
print('\nStacked reversed ')
myStack.reverse()
# print('\nTop node is ->', myStack.peek())
myStack.getMin()

"""

Revsrse Stack 

Stack items 
E - 5
L - 4
G - 3
O - 2
O - 1
G - 0


after reverse 
G - 5
O - 4
O - 3
G - 2
L - 1
E - 0

"""