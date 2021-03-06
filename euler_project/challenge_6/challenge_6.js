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
  (2) Create another variable using the 'const' keyword, 'squareOfSum', to
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
  (6) Find the squared value of 'sumOfNums' and set 'squareOfSum' equal 
      to that value.
  (7) Create a new variable using the 'const' keyword, 
      'sumSquareDifference', and set the value of that variable equal to
      'squareOfSum' minus 'sumOfSquares'.
  (8) Return 'sumSquareDifference'.

*/

/*------------IMPLEMENTING THE PLAN------------*/
const assert = require("assert");

("use strict");

function findSumSquareDifference(rangeStartNum, rangeEndNum) {
  let sumOfSquares = 0;
  let sumOfNums = 0;
  let squareOfSum = 0;

  if (rangeStartNum > 0 && rangeEndNum > 0) {
    for (let i = rangeStartNum; i <= rangeEndNum; i++) {
      let iSquared = i ** 2;
      sumOfSquares += iSquared;
      sumOfNums += i;
      squareOfSum = sumOfNums ** 2;
    }
    const sumSquareDifference = squareOfSum - sumOfSquares;
    return sumSquareDifference;
  } else {
    console.log(
      `The inputs provided were not valid. Please provide a positive integer values for each parameter.`
    );
  }
}

assert.deepStrictEqual(
  findSumSquareDifference(1, 10),
  2640,
  "The sumSquareDifference for all natural numbers between 1 and 10 (inclusive) is 2640"
);

assert.deepStrictEqual(
  findSumSquareDifference(1, 100),
  25164150,
  "The sumSquareDifference for all natural numbers between 1 and 10 (inclusive) is 25164150"
);

console.log(`*****ALL TESTS FOR sumSquareDifference() HAVE PASSED!*****`);

// console.log(findSumSquareDifference(1, 100));

/*------------REFLECTING/ITERATING-------------
- BRUTE FORCE SOLUTION:
  - Were you able to find the 'sumSquareDifference' for all natural 
    numbers between 1 and 100 (inclusive)?
    - Yes. 
  - What was the time/space complexity of your BRUTE FORCE SOLUTION?
    - Time Complexity: O(2n) => O(n) => linear time
    - Space Complexity: O(1) => constant space
  - Can you improve the time/space complexity of the BRUTE FORCE SOLUTION
    in some way?
    - Yes! I could consolidate the two 'for' loops into a single 'for' 
      loop.

- ITERATED SOLUTION:
  - Were you able to find the 'sumSquareDifference' for all natural 
    numbers between 1 and 100 (inclusive)?
    - Yes. 
  - What was the time/space complexity of your ITERATED SOLUTION?
    - Time Complexity: O(n) => linear time
    - Space Complexity: O(1) => constant space
 */
