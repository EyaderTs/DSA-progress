class Solution(object):
    def rob(self, nums):
        
        n=len(nums)
        if n==1:
            return nums[0]
        memo = [0]*n
        memo [0] = nums[0]
        memo [1] = max(memo[0],nums[1])

        for i in range(2,n):
            memo[i] = max(memo[i-1],memo[i-2]+nums[i])
        return memo[-1]
        