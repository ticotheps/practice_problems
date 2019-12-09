/*----------UNDERSTANDING THE PROBLEM----------
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

/*---------------DEVISING A PLAN---------------
- BRUTE FORCE SOLUTION (Pseudocoded Steps)
  (1) Write a helper function, "checkPrime()", that will determine 
      whether or not a number is prime.
  (2) Create a "sumOfPrimes" variable that will be returned as the 
      output.
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

/*------------IMPLEMENTING THE PLAN------------*/
const assert = require("assert");

("use strict");

// Returns 'True' or 'False' to determine if a number is prime
function checkPrime(num) {
  console.log("num = ", num);

  if (num <= 1) {
    return false;
  } else {
    for (let i = num; i > 0; i--) {
      let factorCounter = 0;

      if (num % i == 0) {
        factorCounter += 1;
        console.log("Found another factor!");
        console.log("factorCounter = ", factorCounter);
      } else {
        console.log(`${i} is not a factor of ${num}!`);
      }
    }
    return true;
  }
  return false;
}

console.log(checkPrime(3)); // should print True
console.log(checkPrime(4)); // should print False

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
