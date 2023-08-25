#this is the solution of Question 899 on Leetcode
#O(n^2) time, O(n) space complexity


#when we think about it, if k == 1 and smallest letter in the s is: 'b' and there are 3 b's,
#somehow, we need to rotate and make one of those 3 'b's first character in the final string. Because altough each simulation
#starts with the same letter 'b', the consecutive characters will decide which of the 3 simulations is lexicographically smallest.
#but what happens if k > 1? in that case, we can sort the string however we want and we just return sorted version of the original string
#how? for example when k == 3, we have to extra places that we can use as a buffer to change the order of the letters
# s = 'cbafa', k = 2 =>  1: 'afacb' -> 2: 'aacbf' -> 3: 'cbfaa' -> 4: 'cfaab' -> 5: 'aabcs'
# in the example above, when going from step 1 to step 2, we can use the extra 1 buffer to move f to the end and bring the second a to the front
#same move operation can be seen in the steps from step 3 to step 4.

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        #if k > 1, we have extra buffer so we can just sort the string and return lexicographically smallest options
        if k > 1: return ''.join(sorted(list(s)))
        min_letter = min(s)
        result = s
        #if k == 1, and smallest letter is 'b', result string will start with 'b' and we'll choose one of the possible b's in original string.
        for i in range(len(s)):
            if s[i] == min_letter:
                result = min(result, s[i:]+s[:i])
        return result