class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # when not turbalent there is two scenarios
        # 1. value is increasing or decreasing
            # solution: set l to be 1 behined where its at
        # 2. value is equal
            # solution: set l to be where its at
        
        # i dont care about what came before just if it was increasing or decreasing
        if len(arr) == 1:
            return 1
        prev = ""
        l = 0
        r = 1
        res = 0
        while r < len(arr):
            if arr[r] > arr[r - 1] and prev != "greater":
                res = max(r - l + 1, res)
                prev = "greater"
                r += 1
            elif arr[r] < arr[r - 1] and prev != "lessThan":
                res = max(r - l + 1, res)
                prev = "lessThan"
                r += 1
            else:
                l = r if arr[r] == arr[r - 1] else r - 1
                r = r + 1 if arr[r] == arr[r - 1] else r
                res = max(1, res)
                prev = ""
        return res
