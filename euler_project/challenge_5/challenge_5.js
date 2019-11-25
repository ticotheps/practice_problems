/* ----------UNDERSTANDING THE PROBLEM----------
- Objective: Find the smallest positive number that is evenly divisible
  by all of the numbers from 1 to 20.

- Expected Input(s): 
  - Number of Expected Inputs: 2
  - Names of Expected Inputs: 'startNum', 'endNum' (both represent
    a range of numbers that the output can be divide by evenly)
  - Types of the Expected Inputs:
    - 'startNum' => number
    - 'endNum' => number

- Expected Output(s):
  - Number of Expected Outputs: 1
  - Name of Expected Output: 'smallestCommonMultiple'
  - Type of the Expected Output: 'smallestCommonMultiple' => number

- Any Constraints?
  - Can the output be negative?
    - No. It must be positive.
  - Can the numbers that define the range be negative?
    - No. They must be positive.
  - Can the numbers that define the range be floating point numbers?
    - No. They must be integers.

- Example #1:
  - Example Inputs: 
    - 'startNum' = 1
    - 'endNum' = 10
  - Example Output:
    - 'smallestCommonMultiple' = 2520
 */

/* ---------------DEVISING A PLAN---------------
- BRUTE FORCE SOLUTION:
  (1) Create a variable, 'smallestCommonMultiple', using a 'let'
      statement. This variable will hold the current smallest multiple
      that can be evenly divided by each of the numbers in the range
      from 'startNum' to 'endNum' (inclusively).
  (2) Use a 'while' loop to calculate multiples of the 'endNum' as long
      as 'smallestCommonMultiple' is equal to 0.
  (3) Create a variable, 'currentDivisor', using a 'let' statement to
      hold the value of the current divisor being tested. Set the value
      of 'currentDivisor' to 'endNum - 1'.
  (4) Beginning with 'currentDivisor', evaluate each multiple to see if
      it can be evenly divided by 'currentDivisor'.
      (a) Use a 'while' loop that continues as long as 'multiple % 
          currentDivisor === 0'. 
      (b) If the multiple can be evenly divided by 'currentDivisor',
          subtract 1 from 'currentDivisor' and evaluate whether or not
          that 'currentDivisor' can evenly divide into the multiple.
      (c) If that multiple cannot be evenly divided by 'currentDivisor',
          move to the next multiple and set the value of 'currentDivisor'
          back to 'endNum'.
  (5) Return 'smallestCommonMultiple'.
 */

/* ------------IMPLEMENTING THE PLAN------------ */
const assert = require("assert");
("use strict");

const cache = {};
// console.log("cache = ", cache);

function findSmallestCommonMultiple(startNum, endNum) {
  let smallestCommonMultiple = 0;
  let largestKey = 0;
  let useCache = false;
  // console.log("useCache = ", useCache);

  if (Object.keys(cache).length === 0) {
    // console.log(
    //   `Currently, there are no keys in the 'cache' object to utilize :(`
    // );
  } else {
    for (key in cache) {
      if (endNum >= key) {
        // console.log(
        //   `'endNum' is greater than or equal to the key '${key}' in the 'cache' object!`
        // );
        largestKey = key;
        // console.log("largestKey = ", largestKey);
      }
    }
    useCache = true;
    // console.log("useCache = ", useCache);
  }

  if (useCache) {
    // console.log("Let's use the 'cache' object to speed things up!");
    let currentMultipleWithCache = cache[largestKey];
    // console.log("currentMultipleWithCache = ", currentMultipleWithCache);
    if (currentMultipleWithCache % endNum === 0) {
      smallestCommonMultiple = currentMultipleWithCache;
      return smallestCommonMultiple;
    }
  }

  let i = 1;
  let j = 1;

  while (smallestCommonMultiple === 0) {
    let currentMultiple = endNum * i;
    // console.log("currrentMultiple = ", currentMultiple);

    let currentDivisor = endNum - j;

    while (currentMultiple % currentDivisor === 0) {
      // console.log("currrentDivisor = ", currentDivisor);
      currentDivisor -= 1;
      // console.log(
      //   `YAY! ${currentMultiple} IS divisible by ${currentDivisor}! :) \nOn to the next DIVISOR: ${currentDivisor}\n`
      // );

      if (currentDivisor === startNum) {
        // console.log(
        //   `YAY! ${currentMultiple} IS divisible by ${currentDivisor} too! ;)`
        // );
        smallestCommonMultiple = currentMultiple;
        // console.log(
        //   `Guess WHAT? \n${currentMultiple} is the smallest common multiple for all numbers between ${startNum} & ${endNum} (inclusive)!`
        // );

        cache[endNum] = smallestCommonMultiple;
        // console.log("cache = ", cache);
        return smallestCommonMultiple;
      }
    }
    // console.log("currrentDivisor = ", currentDivisor);
    // console.log(
    //   `SORRY! :( ${currentMultiple} is NOT divisible by ${currentDivisor}! \nOn to the next MULTIPLE of ${endNum}!\n`
    // );
    i++;
    j = 1;
  }
  return "There is no common multiple for the range of numbers provided.";
}

assert.deepStrictEqual(
  findSmallestCommonMultiple(1, 10),
  2520,
  "The smallest common multiple between 1 and 10 is 2520"
);

console.log(findSmallestCommonMultiple(1, 10)); // should be 2520
console.log(findSmallestCommonMultiple(1, 11)); // should be 27720
console.log(findSmallestCommonMultiple(1, 12)); // should be 27720
console.log(findSmallestCommonMultiple(1, 13)); // should be 360360
console.log(findSmallestCommonMultiple(1, 14)); // should be 360360
console.log(findSmallestCommonMultiple(1, 15)); // should be 360360
console.log(findSmallestCommonMultiple(1, 16)); // should be 720720
console.log(findSmallestCommonMultiple(1, 17)); // should be 12252240
console.log(findSmallestCommonMultiple(1, 18)); // should be 12252240
console.log(findSmallestCommonMultiple(1, 19)); // should be 232792560
console.log(findSmallestCommonMultiple(1, 20)); // should be 232792560

/* ------------REFLECTING/ITERATING-------------
- BRUTE FORCE SOLUTION
  - Were you able to find the lowest common multiple for the example 
    input provided?
    - Yes. I my brute force solution found it quickly.
  - What was the Time/Space Complexity of this solution?
    - Time Complexity: O(n^2) = quadratic time 
    - Space Complexity: O(1) = constant space
  - Could you improve the Time/Space Complexity of this solution?
    - YES!
    - How?
      - Use a 'cache' object to store the lowest common multiples that 
        were for calculated for previous inputs.
      - If a provided input shares the same 'startNum' AND has a larger
        'endNum' than the largest key in the 'cache' object, use the
        O(1) lookup run time of the cache object to begin our search at
        the value of the largest key in the 'cache' object.
 */
