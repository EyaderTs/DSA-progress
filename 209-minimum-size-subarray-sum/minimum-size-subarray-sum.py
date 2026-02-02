class Solution(object):
    def minSubArrayLen(self, target, nums):
        l=0
        total = 0
        minimum = float('inf')

        for r in range (len(nums)):
            total += nums[r]
            while total >= target:
                minimum = min (minimum, r-l+1)
                total -= nums[l]
                l+=1
        if minimum == float('inf'):
            return 0
        return minimum

        