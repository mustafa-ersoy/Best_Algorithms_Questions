#this is the solution of Question 2554 on Leetcode
#O(n) time, O(n) space complexity


# if we want to get the maximum number of integers, we need to choose smallest possible elements
# however, some of the numbers are banned and can't be used. range for n is relatively small, 10**4.
# so we can check every value between 1 and n and if value is not in banned, we can add use it
# for fast lookup, we can convert the banned array into a set.


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        count = 0
        sum1 = 0
        #we go from 1 to n and if a value is not in banned, we add it to sum
        # if sum exceeds maxSum, that is the end and we return total count.
        for i in range(1,n+1):
            if i not in banned:
                if sum1 + i <= maxSum:
                    count += 1
                    sum1 += i
                else: return count
        return count