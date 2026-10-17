class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        p1 = 1
        p2 = 0
        for _ in range(n, 0, -1):
            res = p1 + p2
            p2 = p1
            p1 = res

        return res
