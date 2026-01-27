class Solution(object):
    def longestMountain(self, arr):
        largestMtLen = 0

        for i in range(1,len(arr)-1):
           
            if arr[i-1] <arr[i]>arr[i+1]:
                l=i-1
                r=i+1

                while l > 0 and arr[l] > arr[l-1]:
                    l-=1
                while r + 1 < len(arr) and arr[r] > arr[r+1]:
                    r+=1
                if l == 1 and arr[l]>arr[0]:
                    l-=1
                if r == len(arr)-2 and arr[r] > arr[len(arr)-1]:
                    r+=1
                largestMtLen = max(largestMtLen, r-l+1)

        return largestMtLen