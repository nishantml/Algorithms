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

    # inoder traversal of the BST
    def inorder(self, root):
        currentNode = root
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)


bst = BST()
bst.insert(1)
bst.insert(3)
bst.insert(10)
bst.insert(4)
bst.insert(5)
bst.insert(6)
print('Search {10} in bst', bst.lookup(10))
print('Search {21} in bst', bst.lookup(21))
print('\nInorder traverse of BST')
bst.inorder(bst.root)
