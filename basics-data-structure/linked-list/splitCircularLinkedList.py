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
            self.length += 1
        else:
            curr_node = self.head
            while curr_node.next != self.head:
                curr_node = curr_node.next

            curr_node.next = new_node;
            new_node.next = self.head
            self.length += 1

    def split_list(self):
        size = len(self)
        if size == 0:
            return None
        elif size == 1:
            return self.head

        mid = size // 2
        count = 0
        prev = None
        curr_node = self.head

        while curr_node and count < mid:
            count += 1
            prev = curr_node
            curr_node = curr_node.next

        prev.next = self.head
        new_splitList = CircularLinkedList()

        while curr_node.next != self.head:
            new_splitList.append(curr_node.data)
            curr_node = curr_node.next
        new_splitList.append(curr_node.data)

        self.lookup()
        print("\n ")
        new_splitList.lookup()

    def __len__(self):
        curr_node = self.head
        count = 0
        while curr_node:
            count += 1
            curr_node = curr_node.next
            if curr_node == self.head:
                break
        return count

    def lookup(self):
        curr_node = self.head

        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
            if curr_node == self.head:
                break


initialData = [1, 2, 3, 4, 5, 6]
circularLls = CircularLinkedList()
for val in initialData:
    circularLls.append(val)

# print(circularLls.length)
# print(len(circularLls))
# circularLls.lookup()
circularLls.split_list()
