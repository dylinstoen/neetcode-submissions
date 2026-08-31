class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(startIndex, cur):
            res.append(cur[:])
            for i in range(startIndex, len(nums)):
                cur.append(nums[i])
                dfs(i + 1, cur)
                cur.pop()

        dfs(0, [])
        return res