#this is the solution of Question 565 on Leetcode
#O(n) time complexity, O(n) space complexity


#defined sets here work as a cycle and we'll find the length of the longest cycle.
#as we go, we'll keep visited values in a set so that we don't traverse the same cycle again
#we scan the array and start from each value and add the new value to the set until we hit a seen value
#then we find length of the cycle by comparing the length of the current set and initial set.

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        seen = set()
        result = 0
        #scan array
        for num in nums:
            #initial length of the set
            l1 = len(seen)
            curr = num
            #traverse till you find a previously seen value
            while curr not in seen:
                seen.add(curr)
                curr = nums[curr]
            #update the result with the length difference (length of the current cycle)
            result = max(result, len(seen) - l1)
        return result