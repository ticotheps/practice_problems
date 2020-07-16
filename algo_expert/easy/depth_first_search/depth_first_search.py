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
      'lst' (an empty list), and returns a single output, 'lst'. 
      
- Defining Terms:
    - "Node": the smallest unit of measure that can combine with others like it
      to form a tree-like structure.
      
    - "Depth First Traversal": a method used to visit each node within a tree
      using a 'go deep' before you 'go broad' strategy.
      
- Expected Inputs & Outputs:
    - Inputs:
        - Number: 1
        - Data Type: array (Python list)
        - Name: 'lst'
        
    - Outputs:
        - Number: 1
        - Data Type: array (Python list)
        - Name: 'lst
"""
"""
PLAN PHASE

- BRUTE FORCE SOLUTION:
    (1) Create a "Node" class.
    
    (2) Define an "__init__()" method that takes in two parameters, "self" and
    "name".
    
    (3) Define an "addChild()" method that takes in two parameters, "self" and
    "name", that will append a child node to the "self.children" property.
    
    (4) Define a "depthFirstSearch()" method that takes in two parameters,
    "self" and "lst" (an empty list), and returns a list of each node that was
    traversed through.
    
        (a) Append the node's name to the "lst" list.
        
        (b) Use a "for" loop to iterate through all the children nodes of that node...

            (i) ...and make a recursive function call to "depthFirstSearch()" on each child node, passing in the "lst" var as the argument.
            
        (c) Return the "lst" list.

"""
# EXECUTE PHASE

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
        
    def __repr__(self):
        return f"{self.name}: {self.children}"
        
    def addChild(self, name):
        self.children.append(Node(name))
        return self
    
    def depthFirstSearch(self, lst):
        print(f"Node name = {self.name}")
        lst.append(self.name)
        
        for child in self.children:
            print(f"----Child Node name = {child.name}")
            child.depthFirstSearch(lst)
            
        return lst
            
    
my_node = Node(1)
my_node.addChild(2)
my_node.addChild(3)
my_node.addChild(4)

print(my_node.depthFirstSearch([]))
    
