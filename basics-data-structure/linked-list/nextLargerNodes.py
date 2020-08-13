"""

We are given a linked list with head as the first node.  Let's number the nodes in the list: node_1, node_2, node_3, ... etc.

Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.  If such a j does not exist, the next larger value is 0.

Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.

 

Example 1:

Input: [2,1,5]
Output: [5,5,0]
Example 2:

Input: [2,7,4,3,5]
Output: [7,0,5,5,0]
Example 3:

Input: [1,7,5,1,9,2,5,1]
Output: [7,9,9,9,0,5,0,0]

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        curr_main_node = head
        
        
        while curr_main_node is not None:
            if curr_main_node.next is None:
                # print('end')
                curr_main_node.val = 0
                break
            # print('outside ->',curr_main_node.val)
            maxVal = curr_main_node.val
            curr_node = curr_main_node.next
            while curr_node is not None :
                # print('inside ->',curr_node.val)
                if maxVal < curr_node.val:
                    maxVal = curr_node.val
                    break;
                    
                curr_node = curr_node.next
                
            if  curr_main_node.val == maxVal:
                curr_main_node.val = 0
            else:
                curr_main_node.val = maxVal
            curr_main_node = curr_main_node.next
            
        new_node = head
        
        # return new_node
        lst = []   
        while new_node is not None :
            # print(new_node.val)
            lst.append(new_node.val)
            new_node = new_node.next
            
        return lst
            
            
        