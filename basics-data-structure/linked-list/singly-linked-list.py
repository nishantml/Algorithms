class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next

            curr_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            new_node.next = curr_node
            self.head = new_node

    def delete(self, key):
        if self.head is None:
            return
        if self.head.data == key and self.head.next is None:
            self.head = None

        elif self.head.data == key:
            self.head = self.head.next
        else:
            curr_node = self.head
            prev = None
            while curr_node.next is not None:
                prev = curr_node
                curr_node = curr_node.next
                # print('prev', prev.data)
                # print('curr_node', curr_node.data)
                if curr_node.data == key:
                    if curr_node.next is None:
                        prev.next = None
                    else:
                        prev.next = curr_node.next
                        curr_node = curr_node.next

    def search(self, key):
        curr_node = self.head
        count = 0
        while curr_node:
            if curr_node.data == key:
                print('Data Found at Index ', count)
                return
            count += 1
            curr_node = curr_node.next
        print('Data not found')

    def __len__(self):
        curr_node = self.head
        count = 0
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

    def middle_element(self):
        middle = len(self) // 2
        return self.traverse_to_index(middle)

    def traverse_to_index(self, index):
        if index >= len(self):
            return -1
        count = 0
        curr_node = self.head
        while curr_node:
            if count == index:
                return curr_node.data
            curr_node = curr_node.next
            count += 1
        return -1

    def lookup(self):
        curr_node = self.head

        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next


sLinkedList = SinglyLinkedList()
sLinkedList.append(1)
sLinkedList.append(2)
sLinkedList.append(3)
sLinkedList.append(4)
sLinkedList.append(6)
# sLinkedList.prepend(0)
# sLinkedList.prepend(23)
sLinkedList.search(4)
print(len(sLinkedList))
print('middle element-> ', sLinkedList.middle_element())

sLinkedList.lookup()
