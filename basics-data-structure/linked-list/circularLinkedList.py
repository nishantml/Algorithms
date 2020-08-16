class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            curr_node = self.head
            while curr_node.next != self.head:
                curr_node = curr_node.next

            curr_node.next = new_node;
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        curr_node = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = self.head
        else:
            while curr_node.next != self.head:
                curr_node = curr_node.next
            curr_node.next = new_node

        self.head = new_node

    def lookup(self):
        curr_node = self.head

        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
            if curr_node == self.head:
                break


circularLls = CircularLinkedList()
circularLls.append(1)
circularLls.append(2)
circularLls.append(3)
circularLls.append(4)
circularLls.prepend(0)
circularLls.prepend(-1)
circularLls.lookup()
