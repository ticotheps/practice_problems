/*----------UNDERSTANDING THE PROBLEM----------
- What is a 'natural number'?
  - a positive integer that is used for counting or ordering in math.

- Objective
  - Find the difference between the SUM of the squares of the first 100
    natural numbers and the SQUARE of the sum of the first 100 natural
    numbers.
  
- Expected Inputs(s):
  - Number of Inputs: 
    - 2 inputs
  - Types of Each Input (respectively): 
    - number
    - number
  - Names of Inputs:
    - 'rangeStartNum' = defines the start of the range for our natural 
      numbers.
    - 'rangeEndNum' = defines the end of the range for our natural 
      numbers.

- Expected Output(s):
  - Number of Outputs:
    - 1 output
  - Name of Output:
    - 'sumSquareDifference' = defines the difference between the sum of 
      the squares of the first 100 natural numbers and the square of the
      sum of the first 100 natural numbers.
  - Type of Output: 
    - number

- Any Constraints?
  - Can the numbers be negative?
    - No. 'Natural numbers' are positive integers.
  - Can the numbers be floating point numbers?
    - No. 'Natural numbers' must be integers (whole numbers).
  - How high can we expect the input 'rangeEndNum' to reach?
    - Only expect the input 'rangeEndNum' to reach 100.

- Example
  - Example Input(s): 1, 10 (inclusive)
  - Example Output: 2640 (3025 - 385 = 2640)
 */

/*---------------DEVISING A PLAN---------------
- BRUTE FORCE SOLUTION
  (1) Create a function, 'findSumSquareDifference()', which takes in two
      parameters, 'rangeStartNum' & 'rangeEndNum', and returns only one 
      output.
  (2) Create a variable using the 'let' keyword, 'sumOfSquares', to store
      a TOTAL SUM of the squared values of each number between 
      'rangeStartNum' and 'rangeEndNum' (inclusive).
  (2) Create another variable using the 'const' keyword, 'squareOfSums', to
      store the SQUARED VALUE of the total sum of all the numbers between 
      'rangeStartNum' and 'rangeEndNum' (inclusive).
  (3) Use a 'for' loop to iterate through each natural number between 
      'rangeStartNum' and 'rangeEndNum' in order to: 
      (a) find the squared value of the current natural number.
      (b) add that value to the existing 'sumOfSquares' value.
      (c) continue until each number in the range has been accounted for.
  (4) Create a different variable using the 'let' keyword, 'sumOfNums',
      to store the total sum of all the natural numbers in the range.
  (5) Use a separate 'for' loop to iterate through each natural number in
      the range in order to:
      (a) add the value of the current natural number to the existing
          'sumOfNums' value.
      (b) continue until each number in the range has been accounted for.
  (6) Find the squared value of 'sumOfNums' and set 'squareOfSums' equal 
      to that value.
  (7) Create a new variable using the 'const' keyword, 
      'sumSquareDifference', and set the value of that variable equal to
      'squareOfSums' minus 'sumOfSquares'.
  (8) Return 'sumSquareDifference'.

*/

/*------------IMPLEMENTING THE PLAN------------*/

/*------------REFLECTING/ITERATING-------------
 */
