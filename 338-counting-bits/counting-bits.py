class Solution(object):
    def countBits(self, n):
        dp=[-1]*(n+1)
        dp[0] = 0
        offset = 1


        for i in range(1, n+1):
            if 2*offset == i:
                offset = i
            dp[i] = 1 + dp[i-offset]
        return dp
            

            
            
        