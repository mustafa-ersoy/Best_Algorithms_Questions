#this is the solution of Question 2673 on Leetcode
#O(n) time, O(1) space complexity


#let's go to the leaf nodes and select sibling pairs from left to right. By looking at Example 1 image in Leetcode: node4 and node5 are siblings.
#if there is a difference between siblings, we need to handle it right there because if we increase a parent, 
#both will increase the same amount and initial difference will stay same
#lets say node4 = 2, node5 = 3, to make them equal, we make node4 = 3 now they are equal and lets move on to their parent node2
#initially, node2 = 5 and value 3 will come from their children and node2 = 5+3 = 8.
#when we do the same for sibling node3, node3 = 2+3 = 5. difference between node2 ano node3 is 8-5=3, so we need to increase node3 by 3 and so on.

class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        result = 0
        #starting the for loop from last node in leaf and decreasing by two because we deal with siblings.
        #n-1 will match with n-2. so next iteration is n-3 to match it with n-4..
        for i in range(n-1,0,-2):
            #result increase means amount increase to equalize the smaller node value to larger node value.
            result += abs(cost[i] - cost[i-1])
            #after equalizing, we pass the larger node value to their parents to keep the path cost for each node
            cost[(i-1)//2] += max(cost[i], cost[i-1])
        return result