"""

230. Kth Smallest Element in a BST

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        A = []
        res = self.inorder(root, A)
        return A[k - 1]

    def inorder(self, root, A):
        currentNode = root
        if root:
            if currentNode.left:
                self.inorder(currentNode.left, A)
            print(currentNode.val)
            A.append(currentNode.val)
            if currentNode.right:
                self.inorder(currentNode.right, A)
        return A
