/*----------UNDERSTANDING THE PROBLEM----------
  - Define "BST".
    - "BST" = Binary Search Tree
  - Define BST "node".
    - "BST node":
      - Each node has 3 properties associated with it:
        (1) "value": integer value
        (2) "left": a child BST node that must have a value that is LESS
            THAN the value of the parent BST node.
        (3) "right": a child BST node that must have a value that is
            GREATER THAN OR EQUAL TO the value of the parent BST node.
      - Each BST node must have either: 2, 1, or 0 children nodes that
        are also BST nodes.
        - Examples:
          - BST node #1:
            - "value": 12
            - "left": None (null)
            - "right": None (null)
          - BST node #2:
            - "value": 12
            - "left": 4
            - "right": None (null)
          - BST node #3:
            - "value": 12
            - "left": None (null)
            - "right": 15
    
  - Expected Input(s):
    - Number of Inputs: 2
    - Types of Inputs (respectively): 
      (1) BST data structure (object of objects?).
      (2) a Number (integer), representing the target value we're 
          searching with.
  
  - Expected Output(s):
    - Numer of Outputs: 1
    - Type of Output: a Number (integer)

  - Constraints:
    - Assume that there will only be ONE closest value.

  - Clarifying Questions:
    - What sort of data structure will hold the nodes of a BST?
      - (Had to Google this)
      - 


/*---------------DEVISING A PLAN---------------
  - BRUTE FORCE SOLUTION:
    (1) Create a function called 'findClosestValueInBst()' that takes in
        two arguments, 'tree' and 'target'.
    
    (2)     
 */

/*------------IMPLEMENTING THE PLAN------------
 */

/*-------------REFLECTING/ITERATING------------
 */
