class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sumOfWindow = 0
        r = 0
        while r < len(arr) and r < k:
            sumOfWindow += arr[r]
            r += 1
        l = 0
        res = 0
        while r < len(arr):
            print(l, " ", r, " ",  sumOfWindow)
            if sumOfWindow / k >= threshold:
               res += 1
            sumOfWindow -= arr[l]
            sumOfWindow += arr[r]
            r += 1
            l += 1
        if sumOfWindow / k >= threshold:
            res += 1
        return res 