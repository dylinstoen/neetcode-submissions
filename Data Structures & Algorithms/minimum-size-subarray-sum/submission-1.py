class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        curSum = 0
        while r < len(nums) and curSum < target:
            curSum += nums[r]
            r += 1
        if curSum >= target:
            res = r - l
        else:
            return 0
        while r < len(nums):
            while curSum >= target:
                res = min(r - l, res)
                curSum -= nums[l]
                l += 1
            if curSum >= target:
                res = min(r - l, res)
            while r < len(nums) and curSum < target:
                curSum += nums[r]
                r += 1
            if curSum >= target:
                res = min(r - l, res)
        while curSum >= target:
            res = min(r - l, res)
            curSum -= nums[l]
            l += 1
        if curSum >= target:
            res = min(r - l, res)
        return res
                
