class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        uniqueValues = set()
        res = []
        def dfs(startIndex, cur):
            tupleCur = tuple(sorted(cur))
            if tupleCur not in uniqueValues:
                res.append(tupleCur)
                uniqueValues.add(tupleCur)
            for i in range(startIndex, len(nums)):
                cur.append(nums[i])
                dfs(i + 1, cur)
                cur.pop()
        dfs(0, [])
        return res