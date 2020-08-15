class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            new_node.prev = curr_node
            curr_node.next = new_node

    def prepend(self, data):
        new_node = Node(data);
        if self.head is None:
            self.head = new_node
        else:
            leaderNode = self.head
            new_node.next = leaderNode
            leaderNode.prev = new_node
            self.head = new_node

    def lookup(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next


myDOList = DoublyLinkedList()
myDOList.prepend(0)
myDOList.append(1)
myDOList.append(2)
myDOList.append(3)
myDOList.append(4)
myDOList.prepend(-1)

myDOList.lookup()
