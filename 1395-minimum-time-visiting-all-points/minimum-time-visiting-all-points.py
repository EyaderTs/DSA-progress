class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        minTime = 0
        # print (len(points))
        for i in range(len(points)):
            if i == len(points)-1:
                return minTime
            x1,y1 = points[i]
            x2,y2 = points[i+1]
            
            minTime += max(abs(y2-y1),abs(x2-x1))
        