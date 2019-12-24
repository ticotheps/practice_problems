/*----------UNDERSTANDING THE PROBLEM----------
- Objective 
  - Write an algorithm that finds the total number of divisors for a given
    triangle number.

- Definitions
  - "triangle number": the nth number in a sequence of numbers that is
    determined by summing up each previous natural number (beginning with 1) all
    the way up to the nth number.
    - Take a look at these examples below (natural number:triangle number)
      - 1: 1 (1)
      - 2: 3 (1 + 2)
      - 3: 6 (1 + 2 + 3)
      - 4: 10 (1 + 2 + 3 + 4)

- Expected Input(s)
  - Number of Expected Parameters: 1
  - Name of Expected Parameter: "triNum", represents a 'nth' triangle number in
    the sequence
  - Data Types of Expected Parameters: Number

- Expected Output(s)
  - Number of Expected Outputs: 1
  - Names of Expected Output: "totalDivisors"
  - Data Type of Expected Output: Number

- Constraints
  - What will make the algorithm fail?
    - Negative numbers?
      - Yes.
    - Number data types?
      - No.
    - Floating point numbers?
      - Yes.
    - Non-alphanumeric characters in the inputs?
      - Yes.

- Example #1
  - Example #1 Input: 4
  - Example #1 Output: 4 
    - The 4th triangle number is 10 (1 + 2 + 3 + 4) and 10 happens to have 4
      divisors (1, 2, 5, 10).
*/

/*---------------DEVISING A PLAN---------------
- BRUTE FORCE SOLUTION (Pseudocoded Steps)
  (1) <Step 1 here>
  (2) <Step 2 here>
  (3) <Step 3 here>
  ...
*/

/*------------IMPLEMENTING THE PLAN------------*/

const assert = require("assert");

('use strict');

// helper function that finds the value of the nth triangle number from the input
function findNthTriNum(n) {
  if (n > 1 && Number.isInteger(n)) {
    // console.log("n = ", n);
    let triNum = 0;
    for (let i = 1; i <= n; i++) {
      triNum += i;
      // console.log(triNum);
    }

    return triNum;
  }
  return "Please enter a valid value for n";
}




assert.deepStrictEqual(findNthTriNum(4), 10, "The 4th triangle number is 10");
assert.deepStrictEqual(findNthTriNum(5), 15, "The 5th triangle number is 15");
assert.deepStrictEqual(findNthTriNum(-1), "Please enter a valid value for n", "-1 is not a valid n because it is negative");

console.log("*---* ALL TESTS FOR 'findNthTriNum()' PASSED *---*")

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
