class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None;
        self.last = None;
        self.length = 0;

    def enqueue(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node;
            self.last = new_node;
        else:
            self.last.next = new_node;  # point new_node to the lastNode next pointer
            self.last = new_node;  # new creaed should be the last of itself
        self.length += 1
        return self

    def dequeue(self):
        if self.first is None:
            return None;

        if self.first == self.last:
            self.last = None;

        leaderNode = self.first
        self.first = self.first.next
        self.length -= 1
        return leaderNode.data

    def peek(self, position='first'):
        if (self.length == 0):
            return self.first
        else:
            if (position == 'first'):
                return self.first.data
            else:
                return self.last.data

    def lookup(self):
        cur_node = self.first
        if cur_node is None:
            print("Stack Underflow")
        else:
            while cur_node is not None:
                print('<-', cur_node.data, end=' ')
                cur_node = cur_node.next
            print('')
            return


myQueue = Queue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
print('\nLast node is ->', myQueue.peek('last'))
print('\nFirst node is ->', myQueue.peek())
print('Before deleting')
myQueue.lookup();
print('After deleting')
myQueue.dequeue()
myQueue.dequeue()
# myQueue.dequeue()

myQueue.lookup();
