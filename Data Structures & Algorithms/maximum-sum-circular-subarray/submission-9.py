class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMin = nums[0]
        resMin = nums[0]
        curMax = nums[0]
        resMax = nums[0]
        total = nums[0]
        positiveValue = nums[0] > 0
        for i in range(1, len(nums)):
            curMin = min(curMin + nums[i], nums[i])
            resMin = min(curMin, resMin)
            curMax = max(curMax + nums[i], nums[i])
            resMax = max(curMax, resMax)
            positiveValue |= (nums[i] > 0)
            total += nums[i]
        if not positiveValue:
            return resMax
        return max(total - resMin, resMax)