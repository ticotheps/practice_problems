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
    
    (5) Initialize a 'closest' variable that will contain the 'value' of
        the a traversed node that currently contains the closest value to
        the 'target' input.
 */

/*------------IMPLEMENTING THE PLAN------------
 */
var assert = require('assert');

// Declares a class that allows for the creation of new 'Node' instances
class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
  }

  // adds new nodes to the BST
  insert(value) {
    var newNode = new Node(value);

    // if a root node doesn't exist, add it
    if (!this.root) {
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

const findClosestValueInBst = (tree, target) => {
  console.log(tree);
  return target;
};

const bst = new BinarySearchTree();
bst.insert(10);
bst.insert(5);
bst.insert(15);
bst.insert(2);
bst.insert(6);
bst.insert(13);
bst.insert(22);
bst.insert(1);
bst.insert(14);

console.log(findClosestValueInBst(bst, 13));

// TESTS
assert.equal(10, bst.root.value, 'the value of root is 10');

assert.equal(5, bst.root.left.value, 'the value of root.left is 5');
assert.equal(2, bst.root.left.left.value, 'the value of root.left.left is 2');
assert.equal(6, bst.root.left.right.value, 'the value of root.left.right is 6');
assert.equal(
  1,
  bst.root.left.left.left.value,
  'the value of root.left.left.left is 1'
);
assert.equal(15, bst.root.right.value, 'the value of root.right is 15');
assert.equal(
  13,
  bst.root.right.left.value,
  'the value of root.right.left is 13'
);
assert.equal(
  22,
  bst.root.right.right.value,
  'the value of root.right.right is 22'
);
assert.equal(
  14,
  bst.root.right.left.right.value,
  'the value of root.right.left.right is 14'
);

/*-------------REFLECTING/ITERATING------------
 */
