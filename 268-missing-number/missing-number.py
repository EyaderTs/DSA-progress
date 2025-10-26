class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)
        
        # n=len(nums)
        # for i in range(n+1):
        #     if i not in nums:
        #         return i

        