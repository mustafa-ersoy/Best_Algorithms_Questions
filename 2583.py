#this is the solution of Question 2583 on Leetcode
#number of nodes = n, tree height = m
#O(n+m*log(m)) time, O(n+k) space complexity


#in this question, we can just do a level order traversal in an iterative way and sum node values for each level as we go.
#we'll start from root in a queue as: [[root, 0]] which means our first object is root and its level is 0.
#Then we pop root and push its children to queue and it becomes as: [[root_left_child, 1], [root_right_child], 1]
#which means left and right child at level 1. we'll continue to do this over the entire tree and sum values at each level inside total_values dict.
#finally, we scan through the total_values dictionary with a heap to find the kth largest value. (We may also sort values and take kth value as well.)


import heapq as heap
from collections import Counter, deque

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        #edge case
        if not root: return -1
        #create total values dict and queue to travers the tree
        total_values = Counter()
        q = deque([[root,0]])

        while q:
            #we pop current node and level from queue
            node, level = q.popleft()
            #add node's value to the dict
            total_values[level] += node.val
            #if node has children, push their children to queue but with level+1 because children are 1 level below
            if node.left: q.append([node.left, level+1])
            if node.right: q.append([node.right, level+1])
        
        #if number of levels is smaller than k, it is impossible to get kth largest value, return -1
        if len(total_values) < k: return -1

        sum_heap = []
        heap.heapify(sum_heap)

        for level in total_values:
            #to get the kth largest value, we created a heap and pushed values from total_values.
            #whenever heap size exceeds k, we pop the minimum element because we don't need it, we just need to keep k largest values
            heap.heappush(sum_heap, total_values[level])
            if len(sum_heap) > k: heap.heappop(sum_heap)
        #finally, heap will contain k largest values and in that case minimum value would be kth largest value in levels.
        #to get that value, we just pop minimum value from heap.
        return heap.heappop(sum_heap)