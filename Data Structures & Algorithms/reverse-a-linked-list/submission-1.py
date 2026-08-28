# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head

        new_head = self.reverseListHelper(head)
        head.next = None
        return new_head

    def reverseListHelper(self, node):
        if not node.next:
            return node # this is the head of the reversed list
        head = self.reverseListHelper(node.next)
        node.next.next = node
        return head
        
