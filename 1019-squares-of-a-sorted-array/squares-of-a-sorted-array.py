class Solution(object):
    def sortedSquares(self, nums):
        l,r = 0, len(nums)-1
        q= deque()
        while l<= r:
            left = abs(nums[l])
            right = abs(nums[r])
            if left>right:
                q.appendleft(left*left)
                l+=1            
            else:
                q.appendleft(right*right)
                r-=1
        return list(q)

