#this is the solution of Question 2708 on Leetcode
#O(n) time, O(1) space complexity


#we can take all the positive numbers because they will only increase our result when multiplying
#we can take all the negative numbers but there needs to be even number of negative numbers to get a positive result after multiplication.
#for example, all the negatives are [-4,-7,-2,-9,-11] this is odd number of negatives. we need to delete one of them to make it even
#we delete the largest negative value which is -2 because it has the lowest contribution to multiplication.
#there are some edges cases we need to look for.

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        #we create negative_count, largest_neg, and positive seen variables to use later
        neg_count, largest_neg, pos_seen = 0, -float('inf'), False
        result = 1
        #we scan array and if a value is not 0, we just directly multiply and change variables.
        for num in nums:
            if num > 0:
                #if we a positive number, we make pos_seen True. This is for dealing edge cases later.
                pos_seen = True
                result *= num
            elif num < 0:
                #if we see a negative number, we directly multiply and increase negative count by 1
                neg_count += 1
                largest_neg = max(largest_neg, num)
                result *= num
        
        #EDGE CASES
        #if number of negatives is odd, we need to omit the largest negative so we divide the result with largest_neg. that ensures the result is positive

        if neg_count%2: result = result//largest_neg
        #if there is no positive number, 2 edge cases:
        if not pos_seen:
            #only one negative number: [-3] or [-3,0]. first one returns -3, second one returns 0
            if neg_count == 1: return max(nums)
            #if everything is 0 there will be no multiplication on result variable and it will be 1 but, we need to return 0.
            if neg_count == 0: return 0
        return result