# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        new_head = self._reverseListHelper(head)
        return new_head

    def _reverseListHelper(self, head: ListNode):
        # Take of of case for length 1 list
        # 1 -> 2 -> 3 -> 4 -> None
        if not head.next:
            return head
        new_head = self._reverseListHelper(head.next)
        head.next.next = head
        head.next = None
        return new_head
