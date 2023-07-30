#this is the solution of Question 2262 on Leetcode
#O(n) time, O(n) space complexity


#this is DP problem and we need to solve it bottom up by creating a 1-D dp array.
#Let's say: s = 'defeaf' and we create same length dp = [1,0,0,0,0,0]
#dp[i] means total appeal of substrings that end with s[i]
#for i = 0, dp[0] = 1 by default, for i=1, dp[1] = dp[0]+(1+1) = 3. There are 2 substrings that ends with s[1]: 'de' and 'e'
#for appeal score: 'de'+'e' = 2+1 = 3. Let's continue
#for i=2, dp[2] = dp[1]+2+1 = 6. here +2 means we can take everything that ends with previous letter and attacj our current letter
#previous substrings: 'de', 'e', and attached new substrings: 'def','ef'=>3+2 = 5. Also, we can use only 'f' and that is +1 so it is 6.
#formula is dp[-1] + number of previous substring which is i + 1 meaning the letter itself.

#BUT, if we've have seen that letter before, that breaks the algorithm. For example for i=3, all substrings are:
#'defe', 'efe', 'fe', 'e': 3+2+2+1 = 8. so what happened here?
#current letter is e and we've seen it before therefore, substrings before the previous i will decrease our result somehow
#the amount of decrease is equal to (index of previous e+1) because this is the number of substrings that'll have duplicate e's not others.

#dp[i] = dp[i-1]+i+1 - (previous[s[i]]+1)



class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        #this is the previous letter check
        prev_letter_to_index = {s[0]:0}
        dp = [1]+[0]*(n-1)
        for i in range(1,n):
            #applying the formula, assuming no duplicates
            dp[i] = dp[i-1]+i+1
            #but if there is a duplicate, substract number of contaminated substrings which is: previous['e']+1
            if s[i] in prev_letter_to_index:
                dp[i] -= prev_letter_to_index[s[i]]+1
            prev_letter_to_index[s[i]] = i
        #return sum because dp[i] = total appeal for all substrings ending at index i.
        return sum(dp)