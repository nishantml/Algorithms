"""
Stack using Linked List
"""

class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None;
        self.bottom = None;
        self.length=0;
        
    
    def push(self,data):
        new_node = node(data);
        if (self.length == 0):
            self.top = new_node
            self.bottom = new_node
        else:
            stackCurrentTop = self.top
            self.top = new_node
            self.top.next = stackCurrentTop

        self.length +=1
        return self

    def pop(self):
        curr_node = self.top;
        if curr_node == None:
            print('Stack Underflow');
            return self
        stackCurrentTop = self.top
        self.top = stackCurrentTop.next
        self.length -=1
        print('Stack Poped Value is ',stackCurrentTop.data)
        

    def lookup(self):
        curr_node = self.top;
        if curr_node == None:
            print('Stack Underflow');
            return self

        while curr_node is not None:
            print('- ',curr_node.data)
            curr_node = curr_node.next;
        return self

    def peek(self):
        """ This return top value of stack """
        return self.top.data

myStack = Stack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.lookup()
myStack.pop()
myStack.lookup()
print('Stack Current Top value is -> ',myStack.peek())