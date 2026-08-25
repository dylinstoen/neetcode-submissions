class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        r = len(nums) - 1
        while r >= l:
            if nums[l] == nums[l - 1]:
                # Swap
                tmp = nums[l]
                nums[l] = nums[r]
                nums[r] = tmp
                r -= 1
                tmp_r = r
                
                while tmp_r > l:
                    tmp = nums[l]
                    nums[l] = nums[tmp_r]
                    nums[tmp_r] = tmp
                    tmp_r -= 1
                print(nums)
            else:
                l += 1

        print(l, " ", r)
        return r + 1