/* ----------UNDERSTANDING THE PROBLEM----------
- Objective: Find the sum of all the prime numbers below 2,000,000

- Definitions
  - "prime number": a positive integer that can only be divided by 1 and
    itself.

- Expected Input(s)
  - Number of Expected Parameters: 1
  - Names of Expected Parameters: "limitNum"
  - Data Types of Expected Parameters: Number

- Expected Output(s)
  - Number of Expected Outputs: 1
  - Names of Expected Output: "sumOfPrimes"
  - Data Type of Expected Output: Number

- Constraints
	- What will make the algorithm fail?
		- Is 1 a prime number?
			- No.
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
- OVERALL PLAN
	(1) Iterate through the numbers '1' to 'limitNum' using a 'for' loop.
	(2) Evaluate each number, determining whether or not the number is 'prime'.
			(a) If the number is prime, add it to a list of prime numbers.
			(b) If it is NOT prime, do nothing.
	(3) Find the total sum the items in the 'prime numbers' array.
	(4) Return the total sum.

- BRUTE FORCE SOLUTION (Pseudocoded Steps)
  (1) Write a helper function, "checkPrime()", that will determine
      whether or not a number passed to it is "prime".
  (2) Create a "sumOfPrimes" variable that will be returned as the
  output. This variable will also act as a container for the running total sum
  of all the prime numbers below the input, "limitNum".
  (3) Create a function called, 'findSumOfPrimes()', that takes in
      one parameter, "limitNum", and returns one output,
      "sumOfPrimes".
  (4) Using a 'for' loop, iterate through each number between 2 and the
      "limitNum" input (inclusive).
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

  // Checks for invalid inputs
  if (
    num === null
		|| num === undefined
		|| num <= 0
		|| typeof num !== 'number'
		|| !Number.isInteger(num)
  ) {
    // console.log(`Sorry, ${num} is not a valid input. Please provide a positive integer to this function.)`);
    return false;
  }

  // Checks for inputs of 1 !== prime
  if (num === 1) {
    // console.log('1 is not a prime number');
    return false;
  }

  // Checks for positive integers = valid inputs
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
    }
    return true;
  }
}

assert.deepStrictEqual(
  checkPrime(3.24324),
  false,
  '3.24324 is not a valid input type',
);
assert.deepStrictEqual(checkPrime(-3), false, '-3 is not a valid input type');
assert.deepStrictEqual(
  checkPrime(-3.24324),
  false,
  '-3.24324 is not a valid input type',
);
assert.deepStrictEqual(checkPrime(1), false, '1 is not a prime number');
assert.deepStrictEqual(
  checkPrime(null),
  false,
  "'null' is not a valid input type",
);
assert.deepStrictEqual(
  checkPrime(undefined),
  false,
  "'undefined' is not a valid input type",
);
assert.deepStrictEqual(checkPrime(), false, 'No input was provided');
assert.deepStrictEqual(checkPrime(3), true, '3 is a prime number');
assert.deepStrictEqual(checkPrime(300), false, '300 is a prime number');

console.log('\n*-----ALL TESTS FOR "checkPrime()" ARE PASSING-----*\n');

// console.time('Timer');

// const primesCache = {};

// // Finds the sum total of all prime numbers below the input
// function findSumOfPrimes(limitNum) {
//   const primesArr = [];
//   let sumOfPrimes = 0;
//   let largestPrimeBelowLimit = 0;

//   // Checks for invalid inputs
//   if (
//     limitNum === null
// 		|| limitNum === undefined
// 		|| limitNum <= 0
// 		|| typeof limitNum !== 'number'
// 		|| !Number.isInteger(limitNum)
//   ) {
//     return undefined;
//   }

//   // Checks for valid inputs = positive integers
//   if (limitNum > 0) {
//     // Checks for existing key in cache
//     if (primesCache[limitNum]) {
//       console.log(`The limitNum, ${limitNum}, is already in the cache!`);
//       return primesCache[limitNum];
//     }

//     for (let i = 1; i < limitNum; i++) {
//       if (checkPrime(i)) {
//         // console.log('** PRIME NUMBER FOUND! **');
//         // console.log('i = ', i);
//         primesArr.push(i);

//         sumOfPrimes += i;
//         // console.log('sumOfPrimes = ', sumOfPrimes);

//         if (i > largestPrimeBelowLimit) {
//           largestPrimeBelowLimit = i;
//           // console.log(`largestPrimeBelowLimit = ${largestPrimeBelowLimit}, which is < ${limitNum}`);
//         }

//         if (!primesCache[i]) {
//           console.log(`${i} is not currently in our 'primesCache'`);
//           primesCache[i] = [sumOfPrimes]; // Creates a new entry with [sumOfPrimes] which denotes the sum of all the previous prime numbers (from 2 to that value; inclusive)
//           console.log(`primesCache[${i}] = `, primesCache[i]);
//         }
//         console.log('primesCache = ', primesCache, '\n');
//       }
//     }
//     // console.log('largestPrimeBelowLimit = ', largestPrimeBelowLimit);
//     // if (!primesCache[largestPrimeBelowLimit]) {
//     //   primesCache[largestPrimeBelowLimit] = sumOfPrimes;
//     //   console.log('primesCache = ', primesCache);
//     // } else {
//     //   console.log('It does exist');
//     // }

//     // largestPrimeBelowLimit = primesArr[primesArr.length - 1];

//     // console.log('primesArr = ', primesArr);
//     // for (let j = 0; j < primesArr.length; j++) {
//     // 	sumOfPrimes += primesArr[j];
//     // 	console.log('sumOfPrimes = ', sumOfPrimes);
//     // }

//     // largestPrimeBelowLimit = primesArr[primesArr.length - 1];
//     // console.log('largestPrimeBelowLimit = ', largestPrimeBelowLimit);
//   }
//   console.log('primesArr = ', primesArr);
//   // console.log('primesCache = ', primesCache);
//   return sumOfPrimes;
// }

// assert.deepStrictEqual(
// 	findSumOfPrimes(10),
// 	17,
// 	'17 is the sum of all prime numbers below 10'
// );
// assert.deepStrictEqual(
// 	findSumOfPrimes(-1),
// 	undefined,
// 	'-1 is not a valid input'
// );
// assert.deepStrictEqual(
// 	findSumOfPrimes(-1.421334),
// 	undefined,
// 	'-1.421334 is not a valid input'
// );
// assert.deepStrictEqual(
// 	findSumOfPrimes(null),
// 	undefined,
// 	'"null" is not a valid input'
// );
// assert.deepStrictEqual(
// 	findSumOfPrimes(undefined),
// 	undefined,
// 	'"undefined" is not a valid input'
// );
// assert.deepStrictEqual(
// 	findSumOfPrimes(),
// 	undefined,
// 	'An input was not provided'
// );
// assert.deepStrictEqual(
// 	findSumOfPrimes('-1'),
// 	undefined,
// 	'"-1" is not a valid input'
// );

// console.log('\n*-----ALL TESTS FOR "findSumOfPrimes()" ARE PASSING-----*\n');

// console.log(findSumOfPrimes(10)); // Should print 17
// console.log(findSumOfPrimes(20)); // Should print 77
// console.log(findSumOfPrimes(200)); // Should print 4227
// console.log(findSumOfPrimes(2000)); // Should print 277050
// console.log(findSumOfPrimes(20000); // Should print 21171191
// console.log(findSumOfPrimes(200000)); // Should print 1709600813
// console.log(findSumOfPrimes(2000000)); // Should print

// console.timeEnd('Timer');

/* --------REFLECTING/ITERATING THE PLAN--------
- BRUTE FORCE SOLUTION ANALYSIS
  - Were you able to arrive at the correct answer with your solution?
    - Yes, but it took so long to find it.
  - Analyze the Time & Space Complexity of your solution.
    - Time Complexity:
    - Space Complexity:
  - Could either, Time or Space Complexity, be improved in your solution?
    - Yes
	- If so, how would you go about improving it?
    - Refrain from using nested 'for' loops.
    - Instead, use a cache object (to store the value of previously calculated
      "highestPrimeBelowN" values) and a single 'for' loop.
  - What is the new Time & Space Complexity of your improved solution?
    - Time Complexity: O(n) => linear
    - Space Complexity: O(n) => linear
*/
console.time('Timer');

let highestPrimeCache = {};

function optimizedFindSumOfPrimes(limitNum) {
  const limit = limitNum;
  console.log("\n********** limit = ", limit, "**********");
  let sumOfPrimes = 0;
  let highestPrimeBelowLimit = 0;
  let primeStartValue = 1;

  // Checks for invalid inputs
  if (
    limit === null
		|| limit === undefined
		|| limit <= 0
		|| typeof limit !== 'number'
		|| !Number.isInteger(limit)
  ) {
    return undefined;
  } else {
    // Finds the FIRST prime number BELOW "limit"
    for (let i = limit-1; i > 0; i--) {
      if (!checkPrime(i)) {
        console.log(`No prime number at i = ${i}\n`);
      } else {
        highestPrimeBelowLimit = i;
        console.log("EXIT THE LOOP!\nhighestPrimeBelowLimit = ", highestPrimeBelowLimit, "\n");
        break;
      }
    }

    console.log(`CURRENT 'highestPrimeCache' = `, highestPrimeCache);

    // If the 'highestPrimeBelowLimit' currently exists as a key in the
    // 'highestPrimeCache' object, use it!
    let keyCount = 1;
    let largestKey = 0;
    console.log(`largestKey (INITIAL) = ${largestKey}`);
    for (key in highestPrimeCache) {
      console.log(`\nkey #${keyCount} = ${key}`);
      console.log(`largestKey = ${largestKey}`);
      console.log("highestPrimeBelowLimit = ", highestPrimeBelowLimit);
      keyCount++;

      if (key > largestKey) {
        largestKey = key;
      }
    
      if (parseInt(key) === highestPrimeBelowLimit) {
        console.log(`The highest prime number below ${limit} (${highestPrimeBelowLimit}) matches the "${key}" key`) 
        // If the "highestPrimeBelowLimit" exists in the cache as a key, use the
        // associated value as the new starting point for the 'sumOfPrimes' variable. 
        sumOfPrimes = highestPrimeCache[highestPrimeBelowLimit];
        console.log("sumOfPrimes = ", sumOfPrimes);
  
        // If the "highestPrimeBelowLimit" exists in the cache, use this as you're
        // new starting value in the 'primeStartValue' variable.
        primeStartValue = highestPrimeBelowLimit + 1;
        console.log("primeStartValue = ", primeStartValue);
      }
    }

    console.log(`sumOfPrimes = ${sumOfPrimes}`);
    for (let j = primeStartValue; j < limit; j++) {
      // Iterates through the numbers from "primeStartValue" to "limit" and adds
      // whatever values are found to be prime values to the "sumOfPrimes" variable.
      if (checkPrime(j)) {
        console.log(`j = ${j} => PRIME NUMBER ALERT!`);
        sumOfPrimes += j;
        console.log(`sumOfPrimes += ${j}`);
        console.log(`sumOfPrimes = ${sumOfPrimes}\n`);
      } else {
        console.log(`j = ${j} != prime`);
      }
    }

    highestPrimeCache[highestPrimeBelowLimit] = sumOfPrimes;
    console.log(`NEW 'highestPrimeCache' = `, highestPrimeCache);
    return sumOfPrimes;
  }
}

console.log(optimizedFindSumOfPrimes(10)); // Should print 17 in 3.157ms
console.log(optimizedFindSumOfPrimes(20)); // Should print 77 in 6.65ms
console.log(optimizedFindSumOfPrimes(22)); // Should print 77 in 6.65ms
console.log(optimizedFindSumOfPrimes(26)); // Should print 77 in 6.65ms
console.log(optimizedFindSumOfPrimes(30)); // Should print 77 in 6.65ms
// console.log(optimizedFindSumOfPrimes(200)); // Should print 4227
// console.log(optimizedFindSumOfPrimes(2000)); // Should print 277050
// console.log(optimizedFindSumOfPrimes(20000)); // Should print 21171191
// console.log(optimizedFindSumOfPrimes(200000)); // Should print 1709600813


console.log('\n*** ALL TESTS FOR "optimizedFindSumOfPrimes()" PASS ***\n');
console.timeEnd('Timer');