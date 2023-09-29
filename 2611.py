#this is the solution of Question 2611 on Leetcode
#O(n*lgn) time, O(n) space complexity

#first mouse only eats from reward1 and second mouse only eats from reward2.
#first mouse eats k cheeses from reward 1 and those cheese indexes is cancelled in reward2
#therefore, we need to be efficient when selecting cheese for first mouse.
#Here, being efficient means selecting the index with highest   reward1[ind] - reward2[ind] value
#because all cheeses are consumed, it makes sense to give highest difference indexes to first mouse
#high difference means high reward1[ind] and low reward2[ind] which means we give high a score to first mouse
#and eliminate a low score for second mouse. We can use heaps to store [(diff1, ind1), (diff2, ind2)..]


import heapq as heap
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        diff_heap = []
        heap.heapify(diff_heap)

        #create a heap to store difference with indexes, later lowest value (highest difference) will be popped k times.
        for i in range(len(reward1)):
            heap.heappush(diff_heap, (reward2[i]-reward1[i], i))
        res = 0
        #we give k different indexes with highest difference to first mouse
        for _ in range(k):
            diff, ind = heap.heappop(diff_heap)
            res += reward1[ind]
        #after popping, we are left with other cheese indexes and we assign those indexes to second mouse.
        for i in range(len(diff_heap)):
            res += reward2[diff_heap[i][1]]
        return res