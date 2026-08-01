# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d: dict[int, int] = {} # Maps the ListNode.val to indices
        temp = head
        index = 0
        while True:
            if temp is None: # Check if at end of list
                return False
            if d.get(temp.val):
                return True
            d[temp.val] = index
            temp = temp.next
            index += 1

            