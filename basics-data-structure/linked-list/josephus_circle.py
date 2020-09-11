"""
Link -> https://www.geogebra.org/m/ExvvrBbR
Josephus Problem

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        curr_node = self.head
        count = 0
        while curr_node:
            count += 1
            curr_node = curr_node.next
            if curr_node == self.head:
                break
        return count

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

    def delete_node(self, node):
        if self.head is None:
            return
        if self.head == node:
            curr_node = self.head
            while curr_node.next != self.head:
                curr_node = curr_node.next
            curr_node.next = self.head.next
            self.head = self.head.next

        else:
            curr_node = self.head
            prev = None
            while curr_node.next != self.head:
                prev = curr_node
                curr_node = curr_node.next
                # print('ss',curr_node.data)
                if curr_node == node:
                    prev.next = curr_node.next
                    curr_node = curr_node.next

    def josephus_circle(self, step):
        curr_node = self.head

        while len(self) > 1:
            count = 1
            while count != step:
                curr_node = curr_node.next
                count += 1
            print('Killed Node is -> ', curr_node.data)
            self.delete_node(curr_node)
            curr_node = curr_node.next

    def lookup(self):
        curr_node = self.head

        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
            if curr_node == self.head:
                break


circularLls = CircularLinkedList()
n = 6
k = 3
for i in range(1, n + 1):
    circularLls.append(i)

circularLls.josephus_circle(k)
print('\n')
circularLls.lookup()
