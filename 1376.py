#this is the solution of Question 1376 on Leetcode
#n = len(manager)
#O(n) time, O(n) space complexity


#when we think about it, this is a graph question. Starting from one node, what is the furhest possible distance to any node?
#we can easily find it via BFS in graph. This will be a graph with a tree structure therefore E = V-1.

#importing necessary libraries to use in BFS
from collections import defaultdict, deque
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        G = defaultdict(list)
        #building the graph. it works like G[manager] = [employee5, employee8]
        #this is a directed graph that goes from upper managers to lower employees.
        #That way, we can start from topmost manager and go towards bottom to find the largest distance from top.
        for i in range(n):
            G[manager[i]].append(i)
        
        #creating a queue to perform BFS, starting from headID, topmost manager.
        q = deque([(headID, 0)])
        max_time = 0

        while q:
            #we pop the next node and current time of till we reach that node. If it is larger than max_time, we update max_time.
            node, curr_time = q.popleft()
            max_time = max(max_time, curr_time)
            #as we go, we append new neighbors and we don't have to remember previously seen nodes
            #because that forms a tree structure going from top to bottom in BFS.
            for neig in G[node]:
                q.append((neig, curr_time+informTime[node]))
        return max_time