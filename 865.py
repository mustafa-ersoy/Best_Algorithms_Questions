#this is the solution of Question 865 on Leetcode
#O(n) time, O(log(n)) space complexity


#we can solve it via recursion. In each recursion level, left child gives: (left_node, depth_left) and right child gives: (right_node, depth_right)
#if depths are equal, current node should be the root of subtree with the most depth currently.
#if left depth_left > depth_right, we need to consider the node selected by the left side as the answer
#and we'll increase depth_left by 1 when going upwards in the tree
#vice versa for depth_right > depth_left situation.


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        #we create the recursion dfs function
        def dfs(node):
            #if current node is Null, then we need to return the node itself (Null) and depth = 0 as base case
            if not node: return None, 0
            #we handle the recursions and compare their values. l = [left_side_chosen_node, left_depth] this is the format of data.
            l,r = dfs(node.left), dfs(node.right)
            #if depths are equal, the current should be the root current full substring because it needs to contain both left and right sides.
            #we also increase second variable by 1 which is current depth
            if l[1] == r[1]:
                return node, l[1]+1
            #if depth of left side if larger, the winner if left side and we'll forget about the right side.
            #root of substring will be node selected by the left side = l[0]. that node can be 2-3 level below the current node, it is not necessarily left child.
            elif l[1] > r[1]:
                return l[0], l[1]+1
            #if depth_right is larger, we do the opposite.
            return r[0], r[1]+1
        #this function will return something like: selected_node, 7 which means selected node from the recursion and max depth in the whole tree
        #we return selected node. if depth of right and left side is equal, selected_node will the root itself.
        return dfs(root)[0]