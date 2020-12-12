"""
NODE DEPTHS

The distance between a node in the Binary Tree and the tree's root is called the
node's "depth".

Write a function that takes in a Binary Tree and returns the sum of its nodes'
depths.

Each "BinaryTree" node has an integer, 'value', a 'left' child node, and 'right'
child node.

Children nodes can either be "BinaryTree" nodes themselves or None/null.

- Sample Input:
    tree =      1                   <- the depth of this node is 0
              /   \                 
            2       3               <- the depth of each of these nodes is 1 (1 * 2 = 2)
          /   \   /   \
         4     5 6     7            <- the depth of each of these nodes is 2 (2 * 4 = 8)
       /   \
      8     9                       <- the depth of each of these nodes is 3 (3 * 2 = 6)
      
- Sample Output:
    - 16 (2 + 8 + 6 = 16)
    
"""

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def nodeDepths(root, depth = 0):
	if root is None:
		return 0
	
	return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)
	