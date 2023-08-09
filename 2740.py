#this is the solution of Question 2740 on Leetcode
#O(n*log(n)) time, O(n) space complexity (due to sorting)

#this is actually not a difficult question. parameter to minimize is abs(max(nums1) - min(nums2))
#so we only deal with max of nums 1 and min of nums2 and this every other element will be smaller in nums1, every other element is larger in nums2
#[5,2,9,6,0,14], in that example, we need to put the some portion of the minimum elements to nums1, and remaning larger elements to nums2
#but where do we cut. let's sort the array: [0,2,5,6,9,14] here if we cut from 6, we have: nums1=[0,2,5,6], nums2=[9,14], result = abs(6-9) = 3, not optimal
#basically to solve the question, we sort the array and try to find a sweet spot for minimum value as calculated above.
#minimum value would be minimum difference of consequtive pairs. above, it would be 5 and 6 => nums1 = [0,2,5], nums2 = [6,9,14]

class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        #create an infinite value to compare and update later.
        ans = float('inf')
        for i in range(len(nums)-1):
            #scan through the array and try to find minimum difference between pairs and it is our result.
            ans = min(nums[i+1]-nums[i],ans)
        return ans