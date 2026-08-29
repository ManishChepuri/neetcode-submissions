# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pos1, pos2 = 0, 0
    
        def traverse(head: Optional[ListNode], n: int) -> Optional[ListNode]:
            nonlocal pos1
            nonlocal pos2

            if head is None:
                return
            pos1 += 1
            pos2 += 1
            traverse(head.next, n)
            pos2 -= 1
            # print(f"{head.val}, {Solution.pos1 - Solution.pos2}, {Solution.pos1}, {Solution.pos2}")
            if pos1 - pos2 == n + 1:
                head.next = head.next.next
            if pos2 == 0 and pos1 - pos2 == n:
                return head.next
            
            return head
        
        return traverse(head, n)