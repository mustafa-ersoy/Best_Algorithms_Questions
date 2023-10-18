#this is the solution of Question 2517 on Leetcode
#price value: p, len(price) = p
#O(n*log(p)) time complexity, O(1) space complexity



#we'll select k different candies and minimum price difference of any 2 candies will be maximized.
#maximum result can be: max(candies) - min(candies), minimum result can be 0
#we can use a binary search to guess the correct maximum difference result we can get.
#when we select a difference result such as 27, we can scan the array, and find pairs that has differences >= 27
#to do that easily, we can sort the array, select the first number (smallest one) and select another first_number+27 or higher
#after second one, select second_number+27 or higher and so on... eventually if we more than or equal to k numbers,
#this value works and we'll continue binary search


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        #sort the price and decide on minimum and maximum va