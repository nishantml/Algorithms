"""
Implement two stacks in an array 
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
        if self.length == 0:
            return -1
        poped = self.array[-1]
        self.array.pop(self.length - 1)
        self.length -= 1
        return poped

"""
stack  |  operation | 
"""
    
# stackOperation = [[1, 1 ,2],[1, 1 ,3],[2 ,1 ,4],[1 ,2],[2 ,2],[2 ,2]]
stackOperation = [[1, 1, 2 ],[2 ,2],[1 ,2],[2 ,2]]

myStack1 = Stack()
myStack2 = Stack()
out = []
for operation in stackOperation:
    if operation[1] == 1: # this is push operation
        if operation[0] == 1: #  this is stack no 
            myStack1.push(operation[-1])
        elif operation[0] == 2:
            myStack2.push(operation[-1])
    elif operation[1] == 2:
        if operation[0] == 1: #  this is stack no 
            out.append(myStack1.pop())
        elif operation[0] == 2:
            out.append(myStack2.pop())

print(out)
            