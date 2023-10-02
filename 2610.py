#this is the solution of Question 2610 on Leetcode
#O(n) time, O(n) space complexity

#given array can have duplicates but each row can only contain distinct numbers.
#arr = [3,4,3,2,3,3,3,4], here, there are 5 occurances of 3 and it is the most frequent number.
#that means we need to have 5 rows because each one of 3s has to be in different rows.
#so, number of rows is frequency of most frequent number and we'll distribute numbers to each row with brute force.


from collections import Counter
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        #we count the occurances in given array.
        counter = Counter(nums)
        rows = max(counter.values())
        #we create an empty matrix, row count is equal to occurance of most frequent element in array.
        res = [[] for i in range(rows)]
        #we take each key and place all its occurances to a different row in matrix.
        for key in counter:
            for row in range(counter[key]):
                res[row].append(key)
        return res