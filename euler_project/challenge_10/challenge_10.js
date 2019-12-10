/* ----------UNDERSTANDING THE PROBLEM----------
- Objective: Find the sum of all the prime numbers below 2,000,000

- Definitions
  - "prime number": a positive integer that can only be divided by 1 and
    itself.

- Expected Input(s)
  - Number of Expected Parameters: 1
  - Names of Expected Parameters: "limitSummationOfPrimes"
  - Data Types of Expected Parameters: Number

- Expected Output(s)
  - Number of Expected Outputs: 1
  - Names of Expected Output: "sumOfPrimes"
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
  - Example #1 Input: 10
  - Example #1 Output: 17 (2 + 3 + 5 + 7 = 17)
*/

/* ---------------DEVISING A PLAN---------------
- BRUTE FORCE SOLUTION (Pseudocoded Steps)
  (1) Write a helper function, "checkPrime()", that will determine
      whether or not a number is prime.
  (2) Create a "sumOfPrimes" variable that will be returned as the
  output. This variable will also act as a container for the running total sum
  of all the prime numbers below the input, "limitForSumOfPrimes".
  (3) Create a function called, 'findSumOfPrimes()', that takes in
      one parameter, "limitForSumOfPrimes", and returns one output,
      "sumOfPrimes".
  (4) Using a 'for' loop, iterate through each number between 2 and the
      "limitForSumOfPrimes" input (inclusive).
      (a) Call the helper function, "checkPrime()", to determine if the
          number is prime.
          (i)   If the number is prime, add the value to the current value
                of "sumOfPrimes".
          (ii)  If the number is NOT prime, don't do anything.
  (5) Return "sumOfPrimes".
*/

/* ------------IMPLEMENTING THE PLAN------------*/
const assert = require('assert');

('use strict');

// Returns 'True' or 'False' to determine if a number is prime
function checkPrime(num) {
  // console.log('\nnum(input) = ', num);

  if (num === null || num === undefined || num <= 0 || typeof num !== "number" || !Number.isInteger(num)) {
    // console.log(`Sorry, ${num} is not a valid input. Please provide a positive integer to this function.)`);
    return undefined;
  } else {
    if (num === 1) {
      // console.log('1 is not a prime number');
      return false;
    }
    
    if (num > 1) {
      let factorCounter = 0;
      for (let i = num; i > 0; i--) {
        if (num % i == 0) {
          // console.log(`\n${i} IS a factor of ${num}!`);
          factorCounter += 1;
          // console.log('factorCounter = ', factorCounter, '\n');
        } else {
          // console.log(`\n${i} is NOT a factor of ${num}!`);
          // console.log('factorCounter = ', factorCounter, '\n');
        }
      }
      if (factorCounter > 2) {
        return false;
      } else {
        return true;
      }
    }
  }
}


assert.deepStrictEqual(checkPrime(3.24324), undefined, "3.24324 is not a valid input type");
assert.deepStrictEqual(checkPrime(-3), undefined, "-3 is not a valid input type");
assert.deepStrictEqual(checkPrime(-3.24324), undefined, "-3.24324 is not a valid input type");
assert.deepStrictEqual(checkPrime(1), false, "1 is not a prime number");
assert.deepStrictEqual(checkPrime(null), undefined, "'null' is not a valid input type");
assert.deepStrictEqual(checkPrime(undefined), undefined, "'undefined' is not a valid input type");
assert.deepStrictEqual(checkPrime(), undefined, "No input was provided");
assert.deepStrictEqual(checkPrime(3), true, "3 is a prime number");
assert.deepStrictEqual(checkPrime(300), false, "300 is a prime number");

console.log('\n*-----ALL TESTS FOR "checkPrime()" ARE PASSING-----*\n');

/* --------REFLECTING/ITERATING THE PLAN--------
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
