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

    def delete(self, key):
        curr_node = self.head

        while curr_node:
            if curr_node.data == key and curr_node == self.head:  # if we have to remove head Node
                if not curr_node.next:  # if head.next is None 1
                    curr_node = None
                    self.head = None
                    return self
                else:  # if head.next.next is None 2
                    nxt = curr_node.next
                    curr_node.next = None
                    curr_node = None
                    nxt.prev = None
                    self.head = nxt
                    return self
            elif curr_node.data == key:
                if curr_node.next:  # curr_node.next is not None (not a last node)
                    prev = curr_node.prev
                    nxt = curr_node.next
                    prev.next = nxt
                    nxt.prev = prev
                    curr_node.next = None
                    curr_node.prev = None
                    curr_node = None
                    return self
                else:  # if curr_node.next is None (last node)
                    prev = curr_node.prev
                    prev.next = None
                    curr_node.prev = None
                    curr_node = None
                    return self
            curr_node = curr_node.next

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
myDOList.delete(2)

myDOList.lookup()
