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
  return "Please enter a valid value for 'n'";
}

assert.deepStrictEqual(findNthTriNum(4), 10, "The 4th triangle number is 10");
assert.deepStrictEqual(findNthTriNum(5), 15, "The 5th triangle number is 15");
assert.deepStrictEqual(findNthTriNum(-1), "Please enter a valid value for 'n'", "-1 is not a valid 'n' because it is negative");
assert.deepStrictEqual(findNthTriNum(1.342), "Please enter a valid value for 'n'", "1.342 is not a valid 'n' because it is a floating point number");
console.log("*---* ALL TESTS FOR 'findNthTriNum()' PASSED *---*")

function findTotalDivisors(triNum) {
  if (triNum > 1 && Number.isInteger(triNum)) {
    let triNumDivisors = 0;

    for (let j = triNum; j > 0; j--) {
      if (triNum % j === 0) {
        triNumDivisors++;
      }
    }
    
    return triNumDivisors;
  }
  return "Please enter a valid value for 'triNum'";
}

assert.deepStrictEqual(findTotalDivisors(10), 4, "The triangle number 10 has 4 total divisors");
assert.deepStrictEqual(findTotalDivisors(-1), "Please enter a valid value for 'triNum'", "-1 is not a valid 'triNum' because it is negative");
assert.deepStrictEqual(findTotalDivisors(1.342), "Please enter a valid value for 'triNum'", "1.342 is not a valid 'triNum' because it is a floating point number");
console.log("**---** ALL TESTS FOR 'findTotalDivisors()' PASSED **---**")

console.time("findFirstTriNumWithNDivisors");
function findFirstTriNumWithNDivisors(divisorsNumExclusive) {
  console.log("divisorsNumExclusive = ", divisorsNumExclusive);

  const reallyBigNum = Number.MAX_SAFE_INTEGER;
  let foundTriNum = false;
  let currentTriNum = 0;

  while (foundTriNum !== true) {
    for (let n = 1; n < reallyBigNum; n++) {
      currentTriNum = findNthTriNum(n);
      console.log("currentTriNum = ", currentTriNum);

      totalDivisors = findTotalDivisors(currentTriNum);
      console.log("totalDivisors = ", totalDivisors);

      if (totalDivisors > divisorsNumExclusive) {
        foundTriNum = true;
        break;
      }
    }
    break;
  }
  return currentTriNum
}

console.log(findFirstTriNumWithNDivisors(4));
console.log(findFirstTriNumWithNDivisors(10));
console.log(findFirstTriNumWithNDivisors(50));
console.log(findFirstTriNumWithNDivisors(100));
// console.log(findFirstTriNumWithNDivisors(500));
console.timeEnd("findFirstTriNumWithNDivisors");

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
