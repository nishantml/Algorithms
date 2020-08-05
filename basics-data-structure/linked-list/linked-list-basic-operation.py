"""

1. Print a Linked List
2. Length of a linked list
3. Node at a given index in linked list
4. Delete a node by index
5. Append

Explanation

address
node[data,next]

1. initial
2001
[None,None]

2. Secondly
2001            3001
[None,3001] -> [3,None]

3. Continue repeat
2001            3001        4001        5001
[None,3001] -> [3,4001] -> [4,5001] -> [5,None]


"""


class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        # the head node is not going to contain any data it will only used to referene the first node address
        self.head = node()
        self.length = 0
        self.tail = self.head

    def headNode(self):
        if self.head.next is not None:
            return myLst.head.next.data
        else:
            return None

    # Adds new node containing 'data' to the end of the linked list.
    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node
        self.length += 1
        self.tail.next = new_node
        self.tail = new_node

    # Returns the length (integer) of the linked list.
    def getlength(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total

    def deleteAtIndex(self, index):
        if self.length <= index:
            return 'index out of bound'
        curr_node = self.head;
        curr_index = 0;

        if index == 0:
            val = curr_node.next.data
            curr_node.next = curr_node.next.next
            return val
        while curr_node is not None:
            curr_node = curr_node.next;
            if curr_index == index - 1:
                val = curr_node.next.data
                curr_node.next = curr_node.next.next
                return val
            curr_index += 1

    def middleElement(self):
        middle = self.length//2;
        curr_node = self.head;
        curr_index = 0;
        while curr_node is not None:
            curr_node = curr_node.next;
            if curr_index == middle:
                return curr_node.data
            curr_index += 1


    def traverseToIndex(self, index):
        if self.length <= index:
            return 'index out of bound'
        curr_node = self.head;
        curr_index = 0;
        while curr_node is not None:
            curr_node = curr_node.next;
            if curr_index == index:
                return curr_node.data
            curr_index += 1

    # Prints out the linked list in traditional Python list format.
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        return elems


myLst = linked_list();
print('Length of the list', myLst.getlength())
myLst.append(3)
myLst.append(4)
myLst.append(5)
myLst.append(6)
myLst.append(7)
myLst.append(8)
print('2nd way to get Length of the list', myLst.length)
# print('head node', myLst.head.next.data) // this is not the right way will get error when there is empty list
# print('head node', myLst.headNode())
print('Print Linked List', myLst.display())
print('Value at Linked List Index', myLst.traverseToIndex(0))
# print('Value at Linked List Index', myLst.traverseToIndex(3))
# print('Value at Linked List Index', myLst.traverseToIndex(4))
# print('Value deleted at Linked List Index 0 with value ', myLst.deleteAtIndex(3))
print('Print Linked List', myLst.display())
print('Print middle element in Linked List', myLst.middleElement())
