class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sorted_nums = sorted(nums)
        smaller =[]
        for i,v in enumerate (nums):
            count = sorted_nums.index(v)
            # smaller[len(smaller)] = count
            smaller.insert(len(smaller), count)
        return smaller
        