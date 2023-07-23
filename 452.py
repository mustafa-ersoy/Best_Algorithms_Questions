#this is the solution of Question 452 on Leetcode
#O(n*lg(n)) time, O(n) space complexity (due to sorting)


#this is a greedy problem. points array is given random order and we need to arrange it in an optimal order to process our algorithm.
#let's sort the array with respect to second element in the subarray such as:
#[(8,9), (3,10), (4,10), (10,13), (12,19), (3,21)]
#if we burst a balloon at 9, it bursts the first 3 balloons in this sorted list. It doesn't burst array[3] because array[3][0] > 9
#therefore, we'll sort the array wrt. second element then, we'll shot arrows at the rightmost side of the first subarray
#This will be enough to burst the first balloon and give best oppurtunity to burst the next balloons because it is the rightmost possible point
#If that point is larger than consecutive element, that means we burst them as well till we reach a point where we can't burst its first value
#In that case, we need another arrow and increase the count by 1

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #sort the array based on second element in the subarray
        points.sort(key=lambda x: (x[1], x[0]))
        ind, cnt = 0, 0
        #scan array and move forward till you can't burst the first element in a subarray.
        while ind < len(points):
            lg = points[ind][1]
            while ind < len(points) and points[ind][0] <= lg:
                ind += 1
            #when inner while loop breaks, that means we need another arrow.
            cnt += 1
        return cnt