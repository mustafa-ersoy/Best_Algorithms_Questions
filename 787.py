#this is the solution of Question 787 on Leetcode


#This is like a shortest path problem but we have a limitation on number of stops when traveling.
#for shortest path, we can just use Djisktra algorithm but here we'll change it slightly.

import heapq as heap
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #building the graph
        G = self.build(flights)
        
        #heap will be as: [(total_price_sofar  ,  number_of_stops_sofar  ,  node_number)]
        #heap will give the array with minimum first element and that means we'll always pop minimum total_price_sofar in our search
        cost_heap = [(0,0,src)]
        heap.heapify(cost_heap)
        #we create a seen hashmap and as key : value => node : minimum_stops_for_this_node
        #if we can reach a node in 3 steps and with 40$ we don't need to consider the option
        #where we reach it in 6 steps and 60$. First one is already better and heap will give us the minimum prices always.
        seen = {}
        #we'll do a breadth first search as long as something remains in heap
        while cost_heap:
            cost_sum, k1, node = heap.heappop(cost_heap)
            #if we reach node, thanks to heap this is the lowest we can get and also number of stops <= given k. That proves it is true
            if node == dst: return cost_sum
            #as explained above, if there is a lower stops with lower cost, we don't need to consider higher cost with higher stops.
            if node in seen and seen[node] <= k1: continue
            seen[node] = k1
            #we can push k+1 to heap because if k+1 travel stop == destination, this is still acceptable. but we don't push k+2 or above.
            if k1 > k: continue
            for neig, cost in G[node]:
                heap.heappush(cost_heap, (cost_sum+cost,k1+1,neig))
        return -1

    #helper function to build graph
    def build(self, flights):
        G = defaultdict(list)
        for f,t,p in flights:
            G[f].append((t,p))
        return G

        