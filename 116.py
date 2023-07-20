#this is the solution of Question 116 on Leetcode
#O(n) time, O(n) space complexity


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


#in this question, we need to do level order traversal from left to right and store every node in a level inside an array
#we'll create a all_nodes hash table as: {1:[node6], 2:[node3, node9], 3:[node2, node1, node4,node7]}
#hash table above means: in level 1, we have the node6. In level 2, we have the node3 and node9 from left to right and so on.
#in the end, we need to go through arrays in the hash table and assign array[0].next = array[1], array[1].next = array[2] and so on.


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #create a hash table which contains arrays for each level
        all_nodes = {}
        
        #recursion with preorder traversal which makes sure that it goes from left to right in each level.
        def dfs(node, level):
            if not node: return
            #if that level is not seen, add this level to hash table as a key and value will be an array containing the node.
            if level not in all_nodes: all_nodes[level] = [node]
            else: all_nodes[level].append(node)
            dfs(node.left, level+1)
            dfs(node.right, level+1)
            return
        dfs(root, 0)

        #after we classify nodes based on their levels and store in array, we'll just make 
        #array[0].next = array[1], array[1].next = array[2] and so on. In the end, everything is set, we can return True.
        for i in all_nodes:
            for j in range(len(all_nodes[i])-1):
                all_nodes[i][j].next = all_nodes[i][j+1]
        return root