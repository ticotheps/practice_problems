/*----------UNDERSTANDING THE PROBLEM----------
  - Define "BST".
    - "BST" = Binary Search Tree
    - BST has three types of 'nodes':
      (1) Root: top node of a tree structure; does not have a parent node.
      (2) Parent: a predecessor node of another node (child).
        (i) can have a maximum of 2 children nodes ('left', 'right')
      (3) Child: a successor of a parent node.
    - All the keys in a BST are DISTINCT and UNIQUE.
      - A BST is NOT allowed to have duplicate keys and will actually
        decline a request to insert a new node if the key is a duplicate
        of an existing key.
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
    (1) Create a 'Node' class from which you can create new nodes.
    (2) Create a 'BST' class from which you can create a new BST.
    (3) Create an 'insertNode()' function inside of the 'BST' class that
        will allow you to add nodes to your BST.
    (4) Create a function called 'findClosestValueInBst()' that takes in
        two arguments, 'tree' and 'target'.
    
    (5)     
 */

/*------------IMPLEMENTING THE PLAN------------
 */

class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class BST {
  constructor() {
    this.root = null;
  }

  insert(value) {
    let newNode = new Node(value);

    if (this.root === null) {
      this.root = newNode;
    } else {
      this.insertNode(this.root, newNode);
    }
  }

  insertNode(node, newNode) {
    if (newNode.value < node.value) {
      if (node.left === null) {
        // if 'left' is vacant, insert node into value of 'left'
        node.left = newNode;
      } else {
        /*  if 'left' is NOT vacant, call 'insertNode()' until you find a
            null value where the newNode can be inserted. */
        this.insertNode(node.left, newNode);
      }
    } else if (newNode.value > node.value) {
      if (node.right === null) {
        // if 'right' is vacant, insert node into value of 'right'
        node.right = newNode;
      } else {
        /*  if 'right' is NOT vacant, call 'insertNode()' until you find a
            null value where the newNode can be inserted. */
        this.insertNode(node.right, newNode);
      }
    }
  }
}

const bst = new BST();
bst.insert(12);

console.log(bst);

/*-------------REFLECTING/ITERATING------------
 */
