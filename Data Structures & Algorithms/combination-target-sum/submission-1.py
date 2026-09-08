class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def _backtrack(i: int, current: List[int], total: int):
            if total == target:
                res.append(current.copy())
                return
            if total > target or i >= len(nums):
                return
            
            current.append(nums[i])
            _backtrack(i, current, total + nums[i])
            current.pop()
            _backtrack(i + 1, current, total)

        _backtrack(0, [], 0)
        return res