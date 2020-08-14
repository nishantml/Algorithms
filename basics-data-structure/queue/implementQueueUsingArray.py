class Queue:
    def __init__(self):
        self.array = []
        self.length = 0

    # adding the data to the end of the array
    def enqueue(self, data):
        self.array.append(data)
        self.length += 1
        return

    # popping the data to the start of the array
    def dequeue(self):
        poped = self.array[0]
        self.array.pop(0)
        self.length -= 1
        return poped

    # array traverse
    def lookup(self):
        for val in self.array:
            print(' <-', val, end="")

    def peek(self):
        return self.array[0]


myQueue = Queue()
print('\nLength of array is ->', myQueue.length)
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)
myQueue.lookup()
print('\nLength of array is ->', myQueue.length)
print('\nFirst in array is ->', myQueue.peek())
print('\ndequeue value is ->', myQueue.dequeue())
myQueue.lookup()
print('\nLength of array is ->', myQueue.length)
print('\nFirst in array is ->', myQueue.peek())
