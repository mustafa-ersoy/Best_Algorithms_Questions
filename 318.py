#this is the solution of Question 318 on Leetcode
#O(n^2*s) time complexity, O(n*s) space complexity. n = len(words), s = len(words[i])

# we can store sets of letters appearing in each word.
# when we compare two words, we'll check if there is any intersections between their letter sets.
# if intersection is empty, they don't have a common letter, we can multiply their lengths.

from collections import Counter as cntr
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        counts = []
        n, max_value = len(words), 0
        #create sets and append to counts array
        for i in range(n):
            counts.append(set(words[i]))
        
        #check whether sets of 2 words have an intersection or not.
        for i in range(n-1):
            for j in range(i+1, n):
                if len(words[i])*len(words[j]) > max_value and len(counts[i].intersection(counts[j])) == 0:
                    max_value = len(words[i])*len(words[j])
        return max_value