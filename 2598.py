#this is the solution of Question 2598 on Leetcode
#O(n+value) time, O(value) space complexity


#for each element, we can add or subtract value and convert that number to a value between 0 and value
#it is like taking the modulo of an element and mapping to a remaining value.
#nums = [45,36,27,48,19,60,11,92], value = 5, when we take the modulo of each element array becomes: [0,1,2,3,4,0,1,2]
#based on question definition, we can cover everything until value 5. but we have some duplicate leftovers like [0,1,2] at the end
#we can add value 5 to those values to elongate the number chain. so we add [5,6,7] to chain now we can go up to value 8.
#we'll count the modulo values between 0 and value and modulo with lowest frequency will be the one who break our chain and answer.



class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        counter = {i:0 for i in range(value)}
        #count the modulo values
        for num in nums:
            counter[num%value] += 1
        #select the minimum occcurances
        min_occurance = min(counter.values())
        #scan through 0 to value and get the first modulo which has a frequency of min_occurance
        for i in range(value):
            if counter[i] == min_occurance:
                selected = i
                break
        #if value = 10, counter[selected] = 3 and selected = 6, answer is 10*3 + 6
        #because modulo 6 occurs 3 time and that covers the integers 6, 16, 26. But 36 will be our breaking point in chain.
        return value*counter[selected]+selected