#this is the solution of Question 173 on Leetcode

#n = number of node, m = number of function calls
#O(n+m) time, O(n) space complexity

#in this questions we basically need to do a inorder traversal and store node values in an array
#then we'll keep a pointer and scan through array from left to right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        #we need to create an empty self.store array, do a inorder traversal in the BST and store in the array.
        #because this is BST, array will be sorted after inorder traversal
        self.cur_index = 0
        self.store = []
        #for inorder traversal, recursive dfs function. First go to left child and finish all recursions
        #then store current value then go to right child and finish all recursions.
        def dfs(node):
            if not node: return
            dfs(node.left)
            self.store.append(node.val)
            dfs(node.right)
        dfs(root)
        
    def next(self) -> int:
        #the first pointer needs be smaller than smallest element (first element in self.store)
        #we started it from 0 so in the first call, we increase it to 1 but give 0th element and it goes on..
        self.cur_index += 1
        return self.store[self.cur_index-1]

    def hasNext(self) -> bool:
        #if current index pointer is equal or larger than length of the array, that means we are at the end of array
        #there is no larger number in the array or BST left and return false or otherwise, return true.
        return self.cur_index < len(self.store)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()