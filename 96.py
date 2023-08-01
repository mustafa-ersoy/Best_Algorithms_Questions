#this is the solution of Question 96 on Leetcode
#O(n^2) time, O(n) space complexity


#this is a DP problem and we can solve it via bottom up. We need to break question into smaller parts.
#for example, n = 8 and we want to find how many different trees are possible when left side has 4 node and right side has 3 node? (root is 1 node.)
#let's say left side has X possible configuration with 4 nodes and right side has Y different configurations with 3 nodes.
#in that case we need to multiply X*Y to get the answer.
#For example X=5, Y=3, there can be 15 configurations because we can select any one of the 5 for left side and any one if the 3 for rigth side.
#we start with a base case where if n=1, result = 1
#for n=6, we'll try all combinations to find result such as: (l:0, r:5)+(l:1, r:4)+(l:2, r:3)+(l:3, r:2)+(l:4, r:1)+(l:5,r:0) = result for n=6.


class Solution:
    def numTrees(self, n: int) -> int:
        #we start a dp matrix including 0 and marking first 2 values as 1 becase n:0=>1, n:1=>1 as a base case and we start from n=2
        dp = [1]*2+[0]*(n-1)
        for i in range(2,n+1):
            count = 0
            #for n=6, we try all combinations from 0-5 including. dp[3] will give how many configurations are possible when n=3.
            for left in range(i):
                l = dp[left]
                r = dp[i-left-1]
                count += r*l
            #we update the dp[i] after trying all the combinations
            dp[i] = count
        #we return dp[n] which means the possible configurations for n node.
        return dp[n]