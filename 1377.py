#this is the solution of Question 1377 on Leetcode
#O(n) time, O(n) space complexity (because it is a tree, it has O(n) edges)


#in this question, we'll do a modified BFS and carry proabilities from one node to the next node.
#to reach target in, we have only have 1 valid path because the graph is a tree.
#at the beginning, if we have 3 nodes, that means we need to select the rigth node with 1/3 probability.
#after selecting the right node, we have a 4 unvisited nodes so we need to select the right one with 1/4 probability.
#And that makes 1/3 * 1/4 = 1/12 probability and so on.
#when we visit a node, we can remove it from graph to avoid visiting it later.
#during bfs, if current time is larger than given t, it means an unsuccessful search, time will only increase
#and we'll never get given t so we return False


from collections import defaultdict, deque
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = defaultdict(set)
        #we build the graph with defaultdict set
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)
        #start with (node, time, probability)
        q = deque([(1, 0, 1.0)])

        while q:
            node, time, prob = q.popleft()
            #if time > t, we return False because time will only increase, not decrease during search.
            if time > t: return 0
            neig_count = len(graph[node])
            if node == target:
                #if we reach target, there are two possibilities for success:
                #reach to target during time = t or reach target before but have no next node to go and wait at the target.
                if time == t or (time < t and len(graph[node]) == 0): return prob
                else: return 0
            for neig in graph[node]:
                q.append((neig, time+1, float(prob)/float(neig_count)))
                #after getting the next node, we remove the original node from graph
                graph[neig].remove(node)
        #if unsuccessful, return 0 probability.
        return 0