class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def _backtrack(i: int, current: List[int], total: int):
            if total >= target or i >= len(nums):
                if total == target:
                    res.append(current)
                return
            
            current.append(nums[i])
            _backtrack(i, current.copy(), total + nums[i])
            current.pop()
            _backtrack(i + 1, current.copy(), total)

        _backtrack(0, [], 0)
        return res