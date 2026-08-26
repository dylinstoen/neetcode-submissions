class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev = 1
        cur = 2
        res = 0
        for i in range(n - 3, -1, -1):
            res = prev + cur
            prev = cur
            cur = res
        return res