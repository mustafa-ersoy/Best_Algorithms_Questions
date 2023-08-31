#this is the solution of Question 2641 on Leetcode
#O(n) time, O(height) height:(log(n) OR n) space complexity


#cousins occur in each level and every other node except sibling is considered as a cousin.
#basically, when we selected a node, we need to sum every other node in the same level except its sibling.
#that means: node.value = level_order_sum - node.value - node_sibling.value

from collections import Counter
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total_values = Counter()
        #we traverse the array for level order sum and keep sum values inside a hash map
        def traverse(node, level):
            if not node: return

            total_values[level] += node.val
            traverse(node.left, level+1)
            traverse(node.right, level+1)
            return
        traverse(root, 0)

        #we perform another traverse to actually change the values of nodes
        def change_values(node, level):
            if not node: return
            children_total = 0
            #to change the values of the children of a node, we check if it has left and right children.
            if node.left: children_total += node.left.val
            if node.right: children_total += node.right.val
            #if it has left child, we subtract total value of children from level sum and assign it to left child. Same for right child as well.
            if node.left: node.left.val = total_values[level+1]-children_total
            if node.right: node.right.val = total_values[level+1]-children_total
            #continue recursion with left and right children
            change_values(node.left, level+1)
            change_values(node.right, level+1)
            return
        root.val = 0
        change_values(root, 0)
        return root