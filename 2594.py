#this is the solution of Question 2594 on Leetcode
#O(n*lgk) time, O(1) space complexity where k = min(ranks)*cars**2, n = len(ranks)

#when we think about it, there has to be an answer k where for any number >= k, all cars can be repaired.
#ranks = [4,2,3], and let's say k = 18
#first element is 4. 4 * n**2 <= 18 and n here can be 2 at most. Therefore, for a given array,
#and k = 18, first mechanic can repair 2 cars and we can do the same of other mechanics and sum total cars.
#that way we can convert this question into a binary search problem where we try to find the minimum possible time.


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        #we check whether a given time value is enough to fix all the cars.        
        def is_good(time):
            total_cars = 0
            for rank in ranks:
                total_cars += int((time//rank)**0.5)
            return total_cars >= cars

        #we start with a left and right values and do a binary search and check whether it is enough or not.
        left, right = 0, min(ranks)*cars**2
        while left < right:
            mid = (left+right)//2
            enough = is_good(mid)

            if enough: right = mid
            else: left = mid+1
        
        return left