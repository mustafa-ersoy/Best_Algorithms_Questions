#This is the solution of Question 399 on Leetcode


#first of all we need to recognize this is a graph question. WHY?
#if I can evaluate A/B and B/C then I can evaluate A/C as A/C = A/B * B/C
#This is like if I can reach from A to B and B to C, then I can reach from A to C indirectly.
#This means we can model the question as doing breadth first search in a graph

#we need to import defaultdict to build graph and deque for popping and appending in the BFS part
from collections import defaultdict as defdic
from collections import deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defdic(list)
        n,m = len(equations), len(queries)
        #we need to build the graph by considering both sides. if A/B = 3 then B/A  = 1/3. This is how we built graph with division values.
        for i in range(n):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1.0/values[i]))

        #creating the result array with default -1 value
        result = [-1.0 for i in range(m)]
        for i in range(m):
            seen = set()
            #we define start and destination from the query and do a BFS from start to destination. If we can't find a result, it stays as -1
            start, dest = queries[i][0], queries[i][1]
            if start not in graph or dest not in graph: continue
            q = deque([(start, 1.0)])
            
            #BFS from start to destination
            while q:
                #inside the queue, we need to keep the node and multiplication so far because we need to use chain multiplication. (A/C = A/B * B/C)
                node, prevdivision = q.popleft()
                seen.add(node)
                #if we can find the destination, it is over for this query, we can just update the result array and break while and continue with next query
                if node == dest:
                    result[i] = prevdivision
                    break
                for j,k in graph[node]:
                    if j not in seen:
                        q.append((j, prevdivision*k))
        return result
