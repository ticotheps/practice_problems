/*----------UNDERSTANDING THE PROBLEM----------
- Objective 
  - Find the 'product sum' of the given "special" array.

- Definitions
  - Characteristics of a "special array":
    - The array will always be non-empty
    - It can only contain either integers or OTHER special arrays.

  - "Product Sum": the value that results when all the items in the array are
    added together and then multiplied by the level of their depth. 
    - For example, an array containing only integers will have its sum
      multiplied by 1 because it doesn't contain any nested OTHER special arrays
      within it.
    - However, if an array contains integers AND other nested special arrays,
      the 'multiplier' for those nested special arrays will differ from the
      multiplier used with the integers of the outermost special array.

- Expected Input(s)
  - Number of Expected Parameters: 1
  - Names/Data Types of Expected Parameters
    - "specialArr" (an array; must only contain Number or Array data types)

- Expected Output(s)
  - Number of Expected Outputs: 1
  - Names/Data Types of Expected Output
    - "productSum" (a number)

- Constraints
  - Will the following make the algorithm fail?
    - Negative numbers?
      - No.
    - Number data types?
      - No.
    - Floating point numbers?
      - Yes.
      - Must be integers only.
    - Non-alphanumeric characters in the inputs?
      - Yes.
      - Must be integers (negative or positive) only.

- Example #1
  - Example #1 Input(s): [1, 2, 3, 4, 5]
  - Example #1 Output(s): 15 (=> 1 * (1 + 2 + 3 + 4 + 5))

- Example #2
  - Example #2 Input(s): [1, [2, 3], 4, 5]
  - Example #2 Output(s): 20 (=> 1 * (1 + (2 * (2 + 3)) + 4 + 5))

- Example #3
  - Example #3 Input(s): [1, [2, [3, 4], 5]]
  - Example #3 Output(s): 57 (=> 1 * (1 + (2 * (2 + (3 * (3 + 4)) + 5)))
*/

/*---------------DEVISING A PLAN---------------
- BRUTE FORCE SOLUTION (Pseudocoded Steps) 
  (1) Create a helper function ("findItemProductSum()") that will take in an
      item from the special array and return its product sum.
  (2) Create a variable ("multiplier") that will hold the value of the number
      to be multiplied to the sum at each depth.
  (3) Find the length of the given special array.
  (4) Iterate through the given special array.
  ...
*/

/*------------IMPLEMENTING THE PLAN------------*/

/*--------REFLECTING/ITERATING THE PLAN--------
- BRUTE FORCE SOLUTION ANALYSIS
  - Were you able to arrive at the correct answer with your solution?
    - Yes/No
  - Analyze the Time & Space Complexity of your solution.
    - Time Complexity: 
    - Space Complexity: 
  - Could either, Time or Space Complexity, be improved in your solution?
    - Yes/No
  - If so, how would you go about improving it?
  - What is the new Time & Space Complexity of your improved solution?
*/
