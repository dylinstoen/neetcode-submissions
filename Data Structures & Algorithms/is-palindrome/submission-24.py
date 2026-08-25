class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while r > l:
            while r > l and not s[r].isalnum():
                print(s[r])
                r -= 1
            while r > l and not s[l].isalnum():
                print(s[r])
                l += 1
            
            if s[r].lower() != s[l].lower():
                print(s[r])
                return False
            r -= 1
            l += 1
        return True