# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        return (self.isValidSubTreeBST(root.left, -math.inf, root.val) and
            self.isValidSubTreeBST(root.right, root.val, math.inf))

    def isValidSubTreeBST(self, root: Optional[TreeNode], minVal: int, maxVal: int) -> bool:
        if root == None:
            return True
        if root.val >= maxVal or root.val <= minVal:
            return False
        
        return (self.isValidSubTreeBST(root.left, minVal, root.val) and 
            self.isValidSubTreeBST(root.right, root.val, maxVal))
        