class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSumIndices=[]
        for num in nums:
            diff = target - num
            
            if diff in nums and diff != num:
                twoSumIndices.append(nums.index(num))
                twoSumIndices.append(nums.index(diff))
                return twoSumIndices
            elif diff == num and nums.count(diff) > 1:    
                twoSumIndices = [i for i,n in enumerate(nums) if n == diff]
                return twoSumIndices
            
