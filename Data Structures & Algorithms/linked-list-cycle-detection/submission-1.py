# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set() # Maps the ListNode.val to indices
        temp = head
        while True:
            if temp is None: # Check if at end of list
                return False
            if temp in seen:
                return True
            seen.add(temp)
            temp = temp.next

            