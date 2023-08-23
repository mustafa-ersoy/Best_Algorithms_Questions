#this is the solution of Question 675 on Leetcode
#len(forest) = m, len(forest[0]) = n
#O(m^2 * n^2) time, O(m * n) space complexity


#we need to cut trees in height order and every tree has distinct height. For example, we'll cut tree_A, then walk 5 steps to reach
#next tree which is tree_B, after cutting tree_B, we'll walk 7 steps to cut tree_C and we'll count the total steps along the way.


from collections import deque
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m,n = len(forest), len(forest[0])
        trees = [[0,0,0]]

        #we define the helper bfs function to reach from tree_A to tree_B etc. it takes coordinates
        #and returns number of steps from (r1, c1) to (r2, c2)
        def bfs(r1,c1, r2,c2):
            q = deque([(r1,c1,0)])
            seen = set([(r1,c1)])
            #this is the regular bfs with a double ended queue and we uses FIFO concept, append to right, pop from left.
            while q:
                r,c,dist = q.popleft()
                if r == r2 and c == c2: return dist
                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    if 0 <= r+dr < m and 0 <= c+dc < n and forest[r+dr][c+dc] > 0 and (r+dr, c+dc) not in seen:
                        seen.add((r+dr, c+dc))
                        q.append((r+dr, c+dc, dist+1))
            return None


        #we store trees in a list and sort them based their height because we need to cut them in height order. This array will be handy.
        for r in range(m):
            for c in range(n):
                if forest[r][c] > 1: trees.append([forest[r][c], r, c])
        trees.sort()
        ind = 1
        total_dist = 0
        
        #we scan through sorted trees array and cut every tree in order. After cutting tree_A, we need to reach tree_B and we get number
        #of steps needed via helper bfs function. If there is no way to reach from tree_A to tree_B, we return -1.

        while ind < len(trees):
            _, prev_r, prev_c = trees[ind-1]
            _, curr_r, curr_c = trees[ind]
            curr_dist = bfs(prev_r, prev_c, curr_r, curr_c)
            if curr_dist == None: return -1
            total_dist += curr_dist
            ind += 1
        #after completing all steps, we return total number of steps
        return total_dist