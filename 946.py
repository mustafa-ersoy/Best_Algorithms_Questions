#this is the solution of Question 946 on Leetcode
#O(n) time, O(n) space complexity


#to solve this question, we'll use an actual stack and try to simulate the actual situation to see whether it is doable or not.
#we'll have push_pointer for pushed array and pop_pointer for popped array.
#we create a stack and in the iteration we push values from pushed array to stack and increase the pointer by 1
# if the last element in the stack is equal to the next popped element, we pop it from stack and increase popped pointer by 1


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        in_the_stack = set()
        #we create a stack with -1 in it to avoid empty stack edge cases.
        stack = [-1]
        n = len(pushed)
        #we have push_pointer and pop_pointer starting from zero
        push_pointer = 0
        pop_pointer = 0
        while pop_pointer < n and push_pointer < n+1:
            #if the last element in stack we built is equal to next popped element, we need to pop it now before pushing another value
            if stack[-1] == popped[pop_pointer]:
                stack.pop()
                pop_pointer += 1
            #if last value in the stack is not equal, we need to push next value.
            #Also if push pointer >= n there is nothing left to push, that is a failure and we return False
            else:
                if push_pointer >= n: return False
                stack.append(pushed[push_pointer])
                push_pointer += 1
        #if these operations are possible, we need to pop every pushed element in the stack and be left with initial stack which is: [-1]
        return len(stack) == 1