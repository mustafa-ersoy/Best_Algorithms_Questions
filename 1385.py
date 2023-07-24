#this is the solution of Question 1385 on Leetcode
#len(arr1) = m, len(arr2) = n
#O((m+n)*lg(n)) time O(n) space complexity


#brute force solution in that question would be selecting each element in arr1 and scanning through arr2 to decide
#Brute force solution would take O(m*n) time. Let's optimize this
#if we sort the arr2. Then select a number from arr1 and we can do bisection method and find closest 2 elements in arr2.
#arr1 = [4,7,0], arr2 = [-3,3,6,7], d = 2
#let's choose 4 and do a bisection method. In this method 4 would go between 3 and 6 in arr2 which means ind=2
#we got ind2 for number 4. Now we only need to look at closest numbers to 4 in arr2 and these are
#left and right values of ind = 2 =>    arr2[ind-1]=3 and arr2[ind]=6
#if these closest values are okey, everything else will be okey because they will be even further from number 4.

from bisect import bisect as bisect
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        #sort the arr2 to be able to use bisection method
        arr2.sort()
        m,n = len(arr1), len(arr2)
        count = 0
        #scan through arr1 elements
        for i in range(m):
            #do a bisection method, find index to discover the closest elements in arr2 for that number arr1[i]
            ind = bisect(arr2, arr1[i])
            #if both left and right closest elements are okey, we can increase count by 1
            #edge case. If arr1[i] is larger than every number in arr2, we only need to look at ind-1. we shouldn't look for ind = n.
            if ind == n:
                count += abs(arr2[n-1] - arr1[i]) > d
            else:
                count += abs(arr2[ind-1] - arr1[i]) > d and abs(arr2[ind] - arr1[i]) > d
        return count