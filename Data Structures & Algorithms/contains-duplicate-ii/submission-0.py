class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        r = 0
        uniqueNumbers = set()
        while r < len(nums) and r < k:
            if nums[r] in uniqueNumbers:
                return True
            uniqueNumbers.add(nums[r])
            r += 1
        l = 0
        while r < len(nums):
            if nums[r] in uniqueNumbers:
                return True
            uniqueNumbers.add(nums[r])
            uniqueNumbers.remove(nums[l])
            l += 1
            r += 1
        return False