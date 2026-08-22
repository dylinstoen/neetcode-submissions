class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        subString = set()
        for r in range(len(s)):
            while s[r] in subString:
                subString.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            subString.add(s[r])
        return res

