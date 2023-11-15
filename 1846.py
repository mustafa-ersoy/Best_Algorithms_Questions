#this is the solution of Question 1846 on Leetcode
#O(n*lgn) time complexity, O(n) space complexity

# we can rearrange the order and we can only decrease the values not increase them.
# let's first sort the array, make the first value 1 as stated in the question
# when sorted, arr[i] >= arr[i-1] but if arr[i] - arr[i-1] > 1, we'll bring the difference down to 1, otherwise we'll not touch it

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        #if the next current value is larger, difference can only be 1, so we make sure it is 1.
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]+1:
                arr[i] = arr[i-1]+1
        return arr[-1]
