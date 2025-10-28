class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a= list(range(1, (len(nums)+1)))
        missing = list(set(a)- set(nums))
        return missing
        
        
        # a = list(range(1,(len(nums)+1)))
        # set_nums = set(nums)
        # missings = [n for n in a if n not in set_nums]
        # return missings