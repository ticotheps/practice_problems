"""
Depth-First Search

You're given a 'Node' class that has a 'name' and an array of optional
'children' nodes. When put together, nodes form an acyclic tree-like structure.

Implement the 'depthFirstSearch' method on the 'Node' class, which takes in an
empty array, traverses the tree using the Depth-First Search approach
(specifically navigating the tree from left to right), stores all of the nodes'
names in the input array, and returns it.  
"""
"""
UNDERSTAND PHASE

- Objective:
    - Create a function, 'depthFirstSearch()', that takes in a single input,
      'empty_arr', and returns a single output, 'result_arr'. 
      
- Defining Terms:
    - "Node": the smallest unit of measure that can combine with others like it
      to form a tree-like structure.
      
    - "Depth First Traversal": a method used to visit each node within a tree
      using a 'go deep' before you 'go broad' strategy.
"""