# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 1 # 1
        target = None

        def findKthSmallest(root: Optional[TreeNode]) -> int:
            nonlocal count
            nonlocal target

            if not root:
                return
            findKthSmallest(root.left)
            # count += 1
            if count == k:
                target = root.val
            count += 1
            findKthSmallest(root.right)
            return

        findKthSmallest(root)
        return target