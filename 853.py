#this is the solution of Question 853 on Leetcode
#O(n) time, O(n) space complexity

#this is a great stack question.
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []
        n = len(position)
        #first we need to calculate times for each car to arrive finish position
        for i in range(n):
            times.append((target-position[i])/speed[i])
        #we need to sort arriving times based on their starting positions
        #if car A starts behind car B and times[A] <= times[B], then they will merge
        #we can model this by stack. when we sorted times based on start position,
        #if a car starts later but have a higher time, it will block previous cars and that means
        #it will pop previous cars from stack. That means previous cars will slow down to match that new car.
        times = [i for _,i in sorted(zip(position, times))]
        st = []
        for t in times:
            #that statement means, there were previous cars and they were faster than the current car
            #but they will have to reduce to current low speed-high time car so we need to get them out of stack by popping
            while st and st[-1] <= t:
                st.pop()
            st.append(t)
        #finally, length of the stack will give you number of bottleneck cars which total fleets created due those cars.
        return len(st)