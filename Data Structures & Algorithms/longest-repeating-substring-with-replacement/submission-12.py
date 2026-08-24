class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        characterCount = defaultdict(int)
        maxRepeatingCharacter = 0
        for r in range(len(s)):
            if s[r] not in characterCount:
                characterCount[s[r]] = 1
            else:
                characterCount[s[r]] += 1
            maxRepeatingCharacter = max(maxRepeatingCharacter, characterCount[s[r]])
            lengthOfSubarray = r - l + 1
            while maxRepeatingCharacter + k < lengthOfSubarray:
                
                characterCount[s[l]] -= 1
                if characterCount[s[l]] == 0:
                    characterCount.pop(s[l], None)
                l += 1
                maxRepeatingCharacter = max(maxRepeatingCharacter, characterCount[s[r]])
                lengthOfSubarray = r - l + 1
            res = max(res, r - l + 1)
        return res

            