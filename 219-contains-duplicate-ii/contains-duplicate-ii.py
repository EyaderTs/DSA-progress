class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        check = set()

        for i,v in enumerate(nums):

            if v in check:
                return True
            check.add(v)

            if len(check) > k:
                check.remove(nums[i-k])
                 
        return False
        