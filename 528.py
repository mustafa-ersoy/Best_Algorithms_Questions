#this is the solution of Question 528 on Leetcode
#O(log(n)) time complexity for each pickIndex operation, O(n) space complexity


# we need to do a weighted random selection and probability of each element increases with its value
# we can do a prefix sum and choose a random number between 0 and last number in array.
# then we'll do a binary search to find the index of that number.
# if ith element is large, after prefix sum, arr[i] - arr[i-1] will be large and probability of selecting a random
# int between arr[i-1] and arr[i] will increase


import random
from bisect import bisect_left
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        #doing the prefix sum
        for i in range(1, len(w)):
            self.w[i] += self.w[i-1]

    def pickIndex(self) -> int:
        #selecting a random value and doing binary search to find which index it hit
        value = random.randint(1, self.w[-1])
        return bisect_left(self.w, value)