class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}
        for i,v in enumerate(nums):
            diff = target - v

            if diff in hashmap:
                return [i,hashmap[diff]]
            hashmap[v] = i


        # twoSumIndices=[]
        # for num in nums:
        #     diff = target - num
            
        #     if diff in nums and diff != num:
        #         twoSumIndices.append(nums.index(num))
        #         twoSumIndices.append(nums.index(diff))
        #         return twoSumIndices
        #     elif diff == num and nums.count(diff) > 1:    
        #         twoSumIndices = [i for i,n in enumerate(nums) if n == diff]
        #         return twoSumIndices
            
