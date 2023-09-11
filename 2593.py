#this is the solution of Question 2593 on Leetcode
#O(n*lgn) time, O(n) space complexity

#we need to select minimum number in each operation so we can use heaps. In case of equality, we'll choose smaller index so,
#we build heap with two parameters as: [(value1, ind1), (value2,ind2), (value3, ind3)]..
#every time we pop from heap, we know the index so we'll mark ind-1, ind, ind+1 as -1 in the original array.

import heapq as heap
class Solution:
    def findScore(self, nums: List[int]) -> int:
        minHeap = []
        heap.heapify(minHeap)
        n = len(nums)
        #build the heap with 2 parameters
        for i in range(n):
            heap.heappush(minHeap,(nums[i], i))
        
        score = 0
        for i in range(n):
            value, ind = heap.heappop(minHeap)
            #pop from heap if the ind is not marked, mark ind-1, ind, ind+1 in the original array.
            #if the index is marked, we don't do anything and continue.
            if nums[ind] != -1:
                score += value
                nums[ind] = -1
                nums[max(0, ind-1)] = -1
                nums[min(n-1, ind+1)] = -1
        return score