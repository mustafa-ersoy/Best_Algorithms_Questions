#this is the solution of Question 807 on Leetcode
#O(n^2) time, O(n) space complexity



#every row has one maximum building size, every column has one maximum building size.
#if we want to analyze the building at row:r, col:c, we can find the maximum building size at that row and at that column.
#let's say grid[r][c] = 4, max building size at that row: 9, max building size at that column:7
#in that case, we can increase that 4 to 7 and it wouldn't make a difference in any view
#because columnwise, there was another 7 already and row-wise there was a bigger building with a size 9 and it wouldn't make a difference
#therefore, we can increase building sizes but new size has to be lower than => min(max_row[r], max_col[c])


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        maxrows, maxcols = [], []
        #creating arrays to keep track of max building sizes at different rows and cols.
        #calculating max building size at different rows. maxrows[3] means max building size at row=3
        for i in grid:
            maxrows.append(max(i))
        #similarly, maxcols[4] means max building size at column=4
        for i in range(n):
            cols = [grid[j][i] for j in range(n)]
            maxcols.append(max(cols))
        
        total = 0
        #we scan through entire array, and compare current building size with the minimum of max size at that row and max size at that column.
        #we can increase current building size with the difference but difference has to be non-negative. We accumulate the total and return it.
        for r in range(n):
            for c in range(n):
                total += max(0, min(maxrows[r], maxcols[c])- grid[r][c])
        return total