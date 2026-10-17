class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        def rob1(start: int, end: int):
            p1 = 0
            p2 = 0
            for i in range(start, end):
                temp = max(nums[i] + p1, p2)
                p1 = p2
                p2 = temp
            return p2
        
        return max(rob1(0, len(nums) - 1), rob1(1, len(nums)))
