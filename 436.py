#this is the solution of Question 436 on Leetcode
#O(n*lgn) time complexity, O(n) space complexity

#we can store all the start points in a sorted order and for a given end point, we can find the
#next greater start point via binary search.

from bisect import bisect_left
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        start_to_index = {}
        start_values = []
        #store start points in an array, and create a hashmap of indexes for different start points.
        for i, (s, e) in enumerate(intervals):
            start_values.append(s)
            start_to_index[s] = i
        #sort the list of start values to be able to use binary search
        start_values.sort()
        n = len(intervals)
        result = []
        #for each end value, do a binary search on sorted start values and then get original index of that start point from hash table.
        for s,e in intervals:
            ind = bisect_left(start_values,e)
            if ind == n:
                result.append(-1)
            else:
                result.append(start_to_index[start_values[ind]])
        return result