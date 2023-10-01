#this is the solution of Question 2596 on Leetcode
#O(n^2) time, O(n^2) space complexity

#because each value is distinct, we can store location of value between 0 and n^2-1.
#starting from (0,0) if the absolute difference of next location is in the form of (1,2) or (2,1) it is okay, we continue
#else, we return false because knight can't reach next location.
#we don't have to store locations. We can just look for 8 possible next locations to see if one of them contains value+1
#in that case, time and space complexity becomes O(8*n^2) time and O(1) space but code would be less clean.


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        if grid[0][0] != 0: return False
        coordsMap = {}
        #we map values to coordinates.
        for r in range(n):
            for c in range(n):
                coordsMap[grid[r][c]] = (r,c)
        #we scan through numbers from 1 to n^2 and find absolute row and col differences.
        for value in range(1, n**2):
            r_dist = abs(coordsMap[value][0] - coordsMap[value-1][0])
            c_dist = abs(coordsMap[value][1] - coordsMap[value-1][1])

            if (r_dist == 1 and c_dist == 2) or (r_dist == 2 and c_dist == 1): continue
            return False
        return True