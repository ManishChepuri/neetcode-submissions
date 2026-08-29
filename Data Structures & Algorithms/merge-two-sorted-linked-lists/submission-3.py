# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2

        head = None
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        temp = head
        while list1 and list2: # FIXME: both lists aren't at the end
            if list1.val < list2.val:
                temp.next = list1
                temp = temp.next
                list1 = list1.next # Now None
            else:
                temp.next = list2
                temp = temp.next
                list2 = list2.next
        
        if list1 is None:
            temp.next = list2
        else:
            temp.next = list1
        
        return head

