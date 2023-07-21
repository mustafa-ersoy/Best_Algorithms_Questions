#this is the solution of Question 114 on Leetcode
#O(n) time, O(n) space complexity

#in this question, we need to a preorder traversal, store node in an array in the correct order
#Then assign the next node in the array as the right child array[0].right = array[1]..
#we'll also make left child null for each node.


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root: return
        #we create an array to store nodes by doing a preorder traversal
        nodelist = []
        def dfs(node):
            if not node: return None
            nodelist.append(node)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        #after we collect all the nodes in the correct order, we need to assign next node in the array
        #as right child and we need to make left child null.
        for i in range(len(nodelist)-1):
            nodelist[i].left = None
            nodelist[i].right = nodelist[i+1]
        nodelist[-1].left = None
        nodelist[-1].right = None
        