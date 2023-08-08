#this is the solution of Question 2679 on Leetcode
#m = # of rows, n = # of cols
#O(m*n*log(n)) time, O(1) space complexity


#In each operation, we need to select the max element in each row and find the max element selected from each row and add it to the score.
#because we select max/min element in each iteration, this seems like a heap problem. We'll heapify each row and pop from them in each iteration
#that will give us minimum element in each iteration and that is OK too. We are just doing it in a reverse order but still taking the max chosen element.
#after heapify, we'll make #cols different iteration because #cols = number of max elements we'll choose and add to score
#in each iteration, we pop from each row and decide on max popped element by updating the curr_score
#at the end of each iteration, we'll add selected max value to score.


import heapq as heap
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        rows, cols = len(nums), len(nums[0])

        #heapifying each node to be able to pop minimum values constantly.
        for r in range(rows):
            heap.heapify(nums[r])
        score = 0

        #we'll make #cols iterations, this is number of elements to be added to the score
        for c in range(cols):
            #we start curr_score in each iteration with negative infinite and update later.
            curr_score = -float('inf')
            for r in range(rows):
                #we pop from current row, and compare popped value with curr_score to update it
                popped_value = heap.heappop(nums[r])
                curr_score = max(curr_score, popped_value)
            #at the end of iterations, we add curr_score which is max value we got in that iteration to score.
            score += curr_score
        return score