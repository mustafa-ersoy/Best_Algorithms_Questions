#this is the solution of Question 526 on Leetcode
#O(n!) time, O(n) space complexity.
#With memoizing solution O(n*2^n) time and O(2^n) space solution can be achieved, it is a tradeoff.

#this is a back tracking problem and we can solve via brute force recursion solution by trying all the possibilities
#we define a global res variable and increase it by one if we can find a successful outcome in recursion tree

class Solution:
    res = 0
    def countArrangement(self, n: int) -> int:
        #we create a dictionary where if d[i] = 1 it means number i hasn't been used yet and it is available currently.
        #id d[i] = 0, number i has already been used in the recursion tree and we can't use it again.
        #because we create a permutation of different numbers, in a recursion branch, we can use each number only once.
        d = {i:1 for i in range(1,n+1)}
        def rec(ind):
            nonlocal n
            #if ind == n+1 this means we placed all the numbers from 1 to n correctly in the permuation array
            #therefore, this was a successful attempt and we increase the res variable by 1.
            if ind > n: self.res += 1
            
            #we iterate through the number keys in d and if d[i] == 1, it is available and we try it
            for i in d:
                #if d[i] == 1, and also if division rules are satisfied, use i and make d[i] = 0 before the next recursion level.
                #here ind means current array index which is between 1 and n
                if d[i] and (i%ind == 0 or ind%i == 0):
                    d[i] -= 1
                    rec(ind+1)
                    #after recursion finishes, undo the effect and bring the dictionary back into the previous version.
                    d[i] += 1
            return
        #start from index 1 of the array (1-indexed) and try all the options with recursion.
        rec(1)
        return self.res