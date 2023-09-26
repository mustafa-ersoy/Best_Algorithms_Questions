#this is the solution of Question 2563 on Leetcode
#O(n*lgn) time, O(n) space complexity

#we need to provide pairs whose sum is in a range.
#let's say we have value = a and we need another value b where lower <= a+b <= upper
#in that case, lower-a <= b <= upper-a
#in that case, how can we find all b values in that range?
#we can sort the array and do bisection methods from left and right
#this means how many of values is smaller than b and how many of value are larger than b?
#we'll subtract those and get suitable b values in that range.

from bisect import bisect, bisect_left
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        count = 0
        
        # we start from lower values, do a left and right bisection method.
        # to avoid duplications, second value can only have a larger index than the first value
        for i in range(n):
            l,r = bisect_left(nums, lower-nums[i]), bisect(nums, upper-nums[i])
            if r < i: continue
            elif l > i: count += r-l
            else: count += max(0, r-i-1)
        return count