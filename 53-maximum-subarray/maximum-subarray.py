class Solution(object):
    def maxSubArray(self, nums):
        n=len(nums)
        dp = [0]*len(nums)

        for i,n in enumerate (nums):
            dp[i] = max(n, n+dp[i-1])
        return max(dp)      