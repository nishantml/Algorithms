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

    def insert_after_node(self, key, data):
        curr_node = self.head

        while curr_node:
            if curr_node.data == key and curr_node.next is None:
                self.append(data)
                return self
            elif curr_node.data == key:
                new_node = Node(data)
                nxt = curr_node.next
                curr_node.next = new_node
                new_node.next = nxt
                new_node.prev = curr_node
                nxt.prev = new_node
                return self
            curr_node = curr_node.next

    def insert_before_node(self, key, data):
        curr_node = self.head

        while curr_node:
            if curr_node.data == key and curr_node.prev is None:
                self.prepend(data)
                return self
            elif curr_node.data == key:
                new_node = Node(data)
                prev = curr_node.prev

                prev.next = new_node
                curr_node.prev = new_node

                new_node.prev = prev
                new_node.next = curr_node

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
# myDOList.delete(2)
# myDOList.insert_after_node(4, 5)
# myDOList.insert_after_node(-1, 5)
myDOList.insert_before_node(-1, 5)
myDOList.insert_before_node(3, 5)

myDOList.lookup()
