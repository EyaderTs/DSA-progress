class NumArray(object):

    def __init__(self, nums):
        self.dp = [0]

        for num in nums:
            self.dp.append(self.dp[-1]+num)
        
    def sumRange(self, left, right):
        return self.dp[right+1]-self.dp[left]
        