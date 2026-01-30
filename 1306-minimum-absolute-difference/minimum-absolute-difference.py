class Solution(object):
    def minimumAbsDifference(self, arr):
        list = []
        i,j=0,1
        arr.sort()
        minimum = abs (arr[i] -arr[j])
        while j<len(arr):
            dif = abs(arr[i]-arr[j])
            if dif <= minimum:
                if minimum != dif:
                    list = []
                    minimum = dif
                list.append([arr[i],arr[j]])            
            i+=1
            j+=1
        return list


        