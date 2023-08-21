#this is the solution of Question 2825 on Leetcode
#len(str1) = m, len(str2) = n
#O(m+n) time, O(1) space complexity


#in this question, we can change the content of str1 to make str2 a subsequence of str1.
#for each element in str1, we can only cyclically increase the element.
#if we think in reverse direction, if the first letter in str2 is 'd', in str1, we need to see letter 'd' oo 'c' because we can increase 'c' to 'd'.
#therefore, we'll scan through str1 and try to find each letter of str2 or letter-1 (like 'd' and 'c') in order.


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        #created a helper function to to get previous letter elements. ('c'->'d', 'z'->'a')
        def get_prev_char(c):
            value = ord(c)-97
            value = (value+1)%26
            return chr(value+97)
        
        n1,n2,ind2 = len(str1), len(str2), 0

        for i in range(n1):
            #we scan through the str1 and if str2[ind2] = 'd', we check if str1[i] = 'd' or 'c'
            if str1[i] == str2[ind2] or get_prev_char(str1[i]) == str2[ind2]:
                ind2 += 1
                if ind2 == n2: return True
        #if we couldn't finish the str2 ind, that means we couldn't create str2 via letters in str1, so subsequence is not possible.
        return False