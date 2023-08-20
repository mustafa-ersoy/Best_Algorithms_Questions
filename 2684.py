#this is the solution of Question 2684 on Leetcode
#O(m*n) time, O(m*n) space complexity


#this seems like a DFS problem but we can change it to a DP problem by utilizing DFS+Memoization
#basic idea is that when we select a cell, there can only be constant amount of moves we can make from that cell
#and how we reached that cell doesn't matter. If number of moves from cell (2,3) is 4, it is always 4 no matter how we reach that cell.
#Therefore, we'll memoize number of moves for each cell so we can reduce
#exponential DFS time complexity to m*n because there can be at most m*n states (due to m*n cells).

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        #we apply memoization via cache decorator. Inside the recursion, we apply DFS for 3 allowed directions.
        @cache
        def dfs(r,c,m,n):
            curr_result = 0
            for dr, dc in ((-1,1), (0,1), (1,1)):
                if 0<=r+dr<m and 0<=c+dc<n and grid[r+dr][c+dc] > grid[r][c]:
                    #if conditions are met for new neighbour cell, we continue recursion.
                    #we add +1 because we can jump from current cell to next cell and that is already an extra 1 valid move.
                    curr_result = max(curr_result, 1+dfs(r+dr, c+dc, m,n))
            return curr_result
        result = 0
        #we try every cells in the first column and return the max result.
        for i in range(m):
            result = max(result, dfs(i,0,m,n))
        return result