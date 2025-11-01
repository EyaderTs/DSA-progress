class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sorted_nums = sorted (nums)

        value_to_index = {}
        for i,v in enumerate(sorted_nums):
            if v not in value_to_index:
                value_to_index[v] = i

        smaller = []
        for i in nums:
            count = value_to_index[i]
            smaller.append(count)
        return smaller


        # sorted_nums = sorted(nums)
        # smaller =[]
        # for i,v in enumerate (nums):
        #     count = sorted_nums.index(v)
        #     # smaller[len(smaller)] = count
        #     smaller.insert(len(smaller), count)
        # return smaller
        