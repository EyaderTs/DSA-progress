class Solution(object):
    def sortedSquares(self, nums):
        q= deque()
        l,r = 0, len(nums)-1
        while l <= r:
            lsq = nums[l] * nums[l]
            rsq = nums[r] * nums[r]
            if lsq < rsq:
              q.appendleft(rsq)
              r-=1
            else:
              q.appendleft(lsq)
              l+=1        
        return list(q)        
        