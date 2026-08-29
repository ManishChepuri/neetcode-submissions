# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        def initArr(head: Optional[ListNode]) -> None:
            if head is None:
                return
            arr.append(head)
            initArr(head.next)
            head.next = None

        initArr(head)
        
        r = len(arr) - 1
        l = 1

        temp = head
        while True:
            if r >= l:
                temp.next = arr[r]
                r -= 1
                temp = temp.next
            else:
                return None
            if r >= l:
                temp.next = arr[l]
                l += 1
                temp = temp.next
            else:
                return None


        # l = 1, 2
        # r = 3, 2, 1
        # temp = 2 -> 8 -> 4 -> 6
