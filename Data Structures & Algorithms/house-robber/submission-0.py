class Solution:
    def rob(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 0
        for num in nums:
            temp = max(num + p1, p2)
            p1 = p2
            p2 = temp
        return p2