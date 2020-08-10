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

    def reverse(self):
        for i in range(self.length - 1):
            temp = self.array[i]
            self.array[i] = self.array[i + 1];
            self.array[i + 1] = temp

        self.lookup()


myStack = Stack()
print('Length of node is ->', myStack.length)
myStack.push('google')
myStack.push('gmail')
myStack.push('check')
myStack.push('facebook')
myStack.lookup()
print('Length of node is ->', myStack.length)
print('Top node is ->', myStack.peek())
print('Poped node is ->', myStack.pop())
myStack.lookup()
print('Length of node is ->', myStack.length)
print('\nStacked reversed ')
myStack.reverse()
print('\nTop node is ->', myStack.peek())
