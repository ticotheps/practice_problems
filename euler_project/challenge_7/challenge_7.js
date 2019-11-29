/*----------UNDERSTANDING THE PROBLEM----------
- Objective: to find the 10001st prime number.

- Define "prime number".
  - a positive integer that can only be evenly divided by 1 and itself.

- Expected Input(s):
  - Number of Expected Inputs: 1
  - Type of Expected Input: number
  - Name of Expected Input: 'primeNumPlaceInSeq'

- Expected Output(s):
  - Number of Expected Output: 1
  - Type of Expected Output: number
  - Name of Expected Output: 'primeNumAtIndex'

- Any Constraints?
  - 'primeNumPlaceInSeq' cannot be negative & cannot be a floating point number.
  - The input cannot be 'null' or 'undefined'. We can always expect to 
    receive an input.

- Example:
  - Example Input: 6 (referring to the 6th prime number; assuming the 
    first prime number is 2)
  - Example Output: 13
*/

/*---------------DEVISING A PLAN---------------
- BRUTE FORCE SOLUTION:
  (1) Create a helper function, 'checkPrime()', that will take in one 
      parameter, 'num', and will determine if it is prime number, 
      returning a Boolean value. If the input is prime, it will return
      'true'. If it is not a prime number, it will return 'false'.
  (2) Create a function, 'findPrimeNumAtIndex()', that will take in one
      parameter, 'primeNumPlaceInSeq', and will return one output, 
      'primeNumAtIndex'.
      (3) Create a new variable using the 'const' keyword, 
          'primeNumAtIndex', that will store the value of the prime 
          number at the given 'primeNumPlaceInSeq'.
      (4)) Create another variable using the 'let' keyword, 
          'primeNumsCounter', to store a running count of all the prime 
          numbers encountered thus far.
      (5) Create a 'while' loop that will continue to run as long as
          'primeNumsCounter' is NOT equal to 'primeNumPlaceInSeq'.
          (6) Use a 'for' loop to iterate through a range of numbers 
              beginning with 1 and ending with 'primeNumPlaceInSeq'(inclusive).
              (a) Determine if the number being evaluated is a prime 
                  number by using the 'checkPrime()' helper function.
                  (i)   If it is prime, increment the value of
                        'primeNumsCounter' by 1.
                  (ii)  If it is NOT prime, do nothing and continue.
      (7) Return 'primeNumAtIndex'.
*/

/*------------IMPLEMENTING THE PLAN------------*/

const assert = require("assert");

("use strict");

// A helper function that determines if the given input is prime
function checkPrime(num) {
  if (num === undefined || num === null) {
    // console.log("Please provide a valid input (a positive integer)");
    return false;
  } else if (num <= 1) {
    // console.log(`${num} is not a prime number`);
    return false;
  } else {
    // console.log("num = ", num);
    let divisorCounter = 0;
    // console.log("divisorCounter (start) = ", divisorCounter);

    while (divisorCounter <= 2) {
      for (let i = 1; i <= num; i++) {
        // console.log("\ni = ", i);
        let remainder = num % i;
        // console.log("remainder = ", remainder);
        if (remainder === 0) {
          divisorCounter++;
          // console.log("divisorCounter (changed) = ", divisorCounter);
        }
      }

      if (divisorCounter === 2) {
        // console.log(`\n${num} IS a prime number`);
        // 'num' has only 2 divisors (1 & itself) = it IS prime
        return true;
      }
    }
    // console.log(`\n${num} is NOT a prime number`);
    // 'num' has MORE THAN 2 divisors = it is NOT prime
    return false;
  }
}

assert.deepStrictEqual(checkPrime(null), false, "'null' is not a valid input");
assert.deepStrictEqual(
  checkPrime(undefined),
  false,
  "'undefined' is not a valid input"
);
assert.deepStrictEqual(checkPrime(-1), false, "-1 is NOT a prime number");
assert.deepStrictEqual(checkPrime(0), false, "0 is NOT a prime number");
assert.deepStrictEqual(checkPrime(1), false, "1 is NOT a prime number");
assert.deepStrictEqual(checkPrime(2), true, "2 is a prime number");
assert.deepStrictEqual(checkPrime(3), true, "3 is a prime number");
assert.deepStrictEqual(checkPrime(4), false, "4 is NOT a prime number");
assert.deepStrictEqual(checkPrime(5), true, "5 is a prime number");
assert.deepStrictEqual(checkPrime(6), false, "6 is NOT a prime number");
assert.deepStrictEqual(checkPrime(7), true, "7 is a prime number");
assert.deepStrictEqual(checkPrime(8), false, "8 is NOT a prime number");
assert.deepStrictEqual(checkPrime(9), false, "9 is NOT a prime number");
assert.deepStrictEqual(checkPrime(10), false, "10 is NOT a prime number");
assert.deepStrictEqual(checkPrime(11), true, "11 is a prime number");
assert.deepStrictEqual(checkPrime(12), false, "12 is NOT a prime number");
assert.deepStrictEqual(checkPrime(13), true, "13 is a prime number");

console.log("***** ALL TESTS FOR 'checkPrime()' HAVE PASSED *****");

function findPrimeNumAtIndex(primeNumPlaceInSeq) {
  let primeNumAtIndex = 0;
  let primeNumsCounter = 0;

  if (
    primeNumPlaceInSeq === null ||
    primeNumPlaceInSeq === undefined ||
    primeNumPlaceInSeq < 1
  ) {
    return "Sorry, invalid input. Please provide a positive integer.";
  } else {
    let i = 1;
    while (primeNumsCounter <= primeNumPlaceInSeq) {
      // console.log("\nprimeNumsCounter (start) = ", primeNumsCounter);

      if (primeNumsCounter === primeNumPlaceInSeq) {
        return primeNumAtIndex;
      }

      if (checkPrime(i) === true) {
        // console.log(`${i} is a prime number!`);
        primeNumsCounter++;
        // console.log("primeNumsCounter (changed) = ", primeNumsCounter);
        primeNumAtIndex = i;
        // console.log("primeNumAtIndex= ", primeNumAtIndex);
      } else {
        // console.log(`${i} is NOT a prime number!`);
      }
      i++;
    }
  }
}

assert.deepStrictEqual(
  findPrimeNumAtIndex(null),
  "Sorry, invalid input. Please provide a positive integer.",
  "The only acceptable inputs are positive integers."
);
assert.deepStrictEqual(
  findPrimeNumAtIndex(undefined),
  "Sorry, invalid input. Please provide a positive integer.",
  "The only acceptable inputs are positive integers."
);
assert.deepStrictEqual(
  findPrimeNumAtIndex(-1),
  "Sorry, invalid input. Please provide a positive integer.",
  "The only acceptable inputs are positive integers."
);
assert.deepStrictEqual(
  findPrimeNumAtIndex(0),
  "Sorry, invalid input. Please provide a positive integer.",
  "The only acceptable inputs are positive integers."
);
assert.deepStrictEqual(
  findPrimeNumAtIndex(1),
  2,
  "2 is the 1st prime number in the list of prime numbers."
);
assert.deepStrictEqual(
  findPrimeNumAtIndex(2),
  3,
  "3 is the 2nd prime number, assuming that 2 is the first prime number in a list of sequential order prime numbers."
);
assert.deepStrictEqual(
  findPrimeNumAtIndex(3),
  5,
  "3 is the 2nd prime number, assuming that 2 is the first prime number in a list of sequential order prime numbers."
);
assert.deepStrictEqual(
  findPrimeNumAtIndex(4),
  7,
  "7 is the 4th prime number, assuming that 2 is the first prime number in a list of sequential order prime numbers."
);
assert.deepStrictEqual(
  findPrimeNumAtIndex(5),
  11,
  "11 is the 5th prime number, assuming that 2 is the first prime number in a list of sequential order prime numbers."
);
assert.deepStrictEqual(
  findPrimeNumAtIndex(6),
  13,
  "13 is the 6th prime number, assuming that 2 is the first prime number in a list of sequential order prime numbers."
);
assert.deepStrictEqual(
  findPrimeNumAtIndex(10),
  29,
  "29 is the 10th prime number, assuming that 2 is the first prime number in a list of sequential order prime numbers."
);
assert.deepStrictEqual(
  findPrimeNumAtIndex(25),
  97,
  "97 is the 25th prime number, assuming that 2 is the first prime number in a list of sequential order prime numbers."
);
assert.deepStrictEqual(
  findPrimeNumAtIndex(50),
  229,
  "229 is the 50th prime number, assuming that 2 is the first prime number in a list of sequential order prime numbers."
);
assert.deepStrictEqual(
  findPrimeNumAtIndex(100),
  541,
  "541 is the 100th prime number, assuming that 2 is the first prime number in a list of sequential order prime numbers."
);
assert.deepStrictEqual(
  findPrimeNumAtIndex(1000),
  7919,
  "7919 is the 1000th prime number, assuming that 2 is the first prime number in a list of sequential order prime numbers."
);
assert.deepStrictEqual(
  findPrimeNumAtIndex(2000),
  17389,
  "17389 is the 2000th prime number, assuming that 2 is the first prime number in a list of sequential order prime numbers."
);
assert.deepStrictEqual(
  findPrimeNumAtIndex(4000),
  37813,
  "37813 is the 4000th prime number, assuming that 2 is the first prime number in a list of sequential order prime numbers."
);
assert.deepStrictEqual(
  findPrimeNumAtIndex(6000),
  59359,
  "59359 is the 6000th prime number, assuming that 2 is the first prime number in a list of sequential order prime numbers."
);
assert.deepStrictEqual(
  findPrimeNumAtIndex(8000),
  81799,
  "81799 is the 8000th prime number, assuming that 2 is the first prime number in a list of sequential order prime numbers."
);
assert.deepStrictEqual(
  findPrimeNumAtIndex(10001),
  104743,
  "104743 is the 10001st prime number, assuming that 2 is the first prime number in a list of sequential order prime numbers."
);

console.log("*** ALL TESTS FOR 'findPrimeNumAtIndex()' HAVE PASSED ***");

// console.log(findPrimeNumAtIndex(10));
// console.log(findPrimeNumAtIndex(25));
// console.log(findPrimeNumAtIndex(50));
// console.log(findPrimeNumAtIndex(100));
// console.log(findPrimeNumAtIndex(1000));
// console.log(findPrimeNumAtIndex(2000));
// console.log(findPrimeNumAtIndex(4000));
// console.log(findPrimeNumAtIndex(6000));
// console.log(findPrimeNumAtIndex(8000));
// console.log(findPrimeNumAtIndex(10001));

/*-------------REFLECTING/ITERATING------------*/
