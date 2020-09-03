class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BST:
    def __init__(self):
        self.root = None
        self.length = 0

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            self.length += 1
        else:
            currentNode = self.root
            while (True):
                #                 print(currentNode.val)
                if currentNode.val < new_node.val:
                    if currentNode.right is None:
                        currentNode.right = new_node
                        self.length += 1
                        return self.length
                    else:
                        currentNode = currentNode.right
                else:
                    if currentNode.left is None:
                        currentNode.left = new_node
                        self.length += 1
                        return self.length
                    else:
                        currentNode = currentNode.left

    def lookup(self, value):
        if self.root is None:
            return False
        currentNode = self.root;
        while currentNode:
            if value < currentNode.val:
                currentNode = currentNode.left
            elif value > currentNode.val:
                currentNode = currentNode.right
            elif value == currentNode.val:
                return currentNode.val

        return False

    def minValueNode(self):
        curr_node = self.root
        while curr_node.left is not None:
            curr_node = curr_node.left

        return curr_node.val

    def maxValueNode(self):
        curr_node = self.root
        while curr_node.right is not None:
            curr_node = curr_node.right

        return curr_node.val

    def inorder(self, root):
        currentNode = root
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

    def breadthFirstSearch(self):
        """Breadth First Search"""
        currentNode = self.root
        queue = []
        bfsList = []
        queue.append(currentNode)

        while len(queue) > 0:
            currentNode = queue.pop(0)
            #             print(currentNode.val)
            bfsList.append(currentNode.val)

            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        return bfsList


bst = BST()
# bst.insert(1)
bst.insert(3)
bst.insert(10)
bst.insert(4)
bst.insert(5)
bst.insert(6)
# print('Search {10} in bst', bst.lookup(10))
print('Search {21} in bst', bst.lookup(21))
print('\nInorder traverse of BST')
bst.inorder(bst.root)

print('min value in bst -> ', bst.minValueNode())
print('max value in bst -> ', bst.maxValueNode())
