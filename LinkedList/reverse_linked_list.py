"""
        Reverse a singly-linked list.

        Approach:
        - Use two pointers, `previous` and `current`, to iterate through the list.
        - For each node:
          1. Store the next node in `nextNode`.
          2. Reverse the `current.next` pointer to point to `previous`.
          3. Move `previous` and `current` one step forward.
        - At the end, `previous` will point to the new head of the reversed list.

        Time Complexity:
        - O(n), where n is the number of nodes in the linked list.
          Each node is visited exactly once.

        Space Complexity:
        - O(1), constant extra space.
          Only a few pointers are used regardless of list size.

        Args:
        - head (Optional[ListNode]): Head of the singly-linked list.

        Returns:
        - Optional[ListNode]: Head of the reversed linked list.
        """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initializing pointers for current and previous nodes of linked list 
        current = head
        previous = None

        # navigating all nodes 
        while current is not None: 

            # storing the next node 
            nextNode = current.next 

            # reversing the current node's next pointer 
            current.next = previous 

            # advancing pointers one position ahead 
            previous = current 
            current = nextNode 
        
        return previous     
