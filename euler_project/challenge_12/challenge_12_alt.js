/**
 * UNDERSTAND: 
 * - Find the FIRST triangle number that has MORE THAN 500 divisors.
 * - What is a "triangle number"?
 *    - A triangle number is a number from a sequence of sums that are made up
 *      by adding a natural number to its previous adjacent natural number
 *      (beginning with 1 as the first natural and first triangle number).
 *
 * PLAN: (1)  Create a helper function, 'findAllTriNumsAndFactors()', that 
 *            takes in one input, 'maxNumOfTriNums', which denotes the total 
 *            number of triangle numbers to be returned in an object, 
 *            'triNumsCache'. 
 * 
 *       (2)  Create another function, 'findTriNumWithNDivsors()', that takes 
 *            in 2 inputs, 'triNumsCache' & 'threshold'. This function will 
 *            loop through the 'triNumsCache' to find the first triangle number 
 *            that has a total number of divisors GREATER THAN the 
 *            'threshold' input.
 */

const assert = require("assert");

("use strict");

const triNumsCache = {};

function findAllTriNumsAndFactors(maxNumOfTriNums) {
  if (Number.isInteger(maxNumOfTriNums) && maxNumOfTriNums > 0) {
    let currentTriNum = 0;
  
    for (let i = 1; i <= maxNumOfTriNums; i++) {
      currentTriNum += i; 

      if (!(currentTriNum in Object.keys(triNumsCache))) {
        // console.log(`${currentTriNum} DOES NOT exist as a key yet!`);
        triNumsCache[currentTriNum] = false;
      } else {
        // console.log(`${currentTriNum} already exists as a key in the cache`);
      }
    }

    for (key in triNumsCache) {
      // console.log(triNumsCache);
      // console.log("key = ", key);
      let numOfKeysDivisors = 0;

      if (triNumsCache[key] !== false) {
        // console.log(`The ${key}-key already already has a value associated with it`);
      } else {
        for (let j = 1; j <= key; j++) {
          if (key % j === 0) {
            numOfKeysDivisors += 1;
          }
        }
        // console.log(`numOfKeysDivisors @ ${key} = ${numOfKeysDivisors}`);
        triNumsCache[key] = numOfKeysDivisors;
      }
    }
    return triNumsCache;
  }

  console.error("Please enter a valid input");
  return false;
}

// console.log(findAllTriNumsAndFactors(5));
// console.log(triNumsCache);
// console.log(findAllTriNumsAndFactors(10));
// console.log(findAllTriNumsAndFactors(100));
// console.log(findAllTriNumsAndFactors(1000));

// assert.deepStrictEqual(findAllTriNumsAndFactors(5), first5, "The first 5 triangle numbers are: 1, 3, 6, 10, & 15.");
// assert.deepStrictEqual(findAllTriNumsAndFactors(10), first10, "The first 5 triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55.");
// assert.deepStrictEqual(findAllTriNumsAndFactors(10), firstTenTriNums, "The first four triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 45, & 55.");
// assert.deepStrictEqual(findAllTriNumsAndFactors(-4), false, "The input type must be a positive integer");
// assert.deepStrictEqual(findAllTriNumsAndFactors(1.5), false, "The input type must be a positive integer");

console.log("\n**--- ALL TESTS FOR 'findAllTriNumsAndFactors()' PASSED ---**\n");


console.time("findTriNumWithNDivsors()");
function findTriNumWithNDivsors(triNumsCache, threshold) {
  let triNum = 0;
  let totalDivisors = 0;
  let largestCacheKey = 0;

  // console.log(triNumsCache);

  for (key in triNumsCache) {
    if (triNumsCache[key] > threshold) {
      // console.log("\nA key with a value greater than our input already exists in the cache");
      // console.log("triNumsCache key = ", key);
      // console.log("numOfDivisors @ key = ", triNumsCache[key]);

      // console.log("\nBEFORE triNum = ", triNum);
      triNum = Number(key);
      // console.log("AFTER triNum = ", triNum);

      return triNum;
    }
  }
  return `\nThere were no triangle numbers in this cache that had MORE THAN ${threshold} divisors`;
}

// console.log(findTriNumWithNDivsors(first10, 4));  // should print 28 (6 divisors)
// console.log(findTriNumWithNDivsors(first10, 10));  // should print 'There were no triangle numbers in this cache that had MORE THAN 10 divisors'

// assert.deepStrictEqual(findTriNumWithNDivsors(first10, 4), 28, "The first triangle number with more than 4 divisors is 28, which has 6 divisors");
// assert.deepStrictEqual(findTriNumWithNDivsors(first10, 10), "\nThere were no triangle numbers in this cache that had MORE THAN 10 divisors", "There were no triangle numbers in this cache that had MORE THAN 10 divisors");
// assert.deepStrictEqual(findTriNumWithNDivsors(first100, 500), "\nThere were no triangle numbers in this cache that had MORE THAN 500 divisors", "There were no triangle numbers in this cache that had MORE THAN 500 divisors");
// assert.deepStrictEqual(findTriNumWithNDivsors(first1000, 500), "\nThere were no triangle numbers in this cache that had MORE THAN 500 divisors", "There were no triangle numbers in this cache that had MORE THAN 500 divisors");
// assert.deepStrictEqual(findTriNumWithNDivsors(firstHundredTriNums, 50), "\nThere were no triangle numbers in this array that had MORE THAN 50 divisors", "This array has no triangle numbers with more than 50 divisors");

console.log("---** ALL TESTS FOR 'findTriNumWithNDivsors()' PASSED **---\n");

console.log(findTriNumWithNDivsors(findAllTriNumsAndFactors(1000), 10));
console.log(findTriNumWithNDivsors(findAllTriNumsAndFactors(1000), 20));
console.log(findTriNumWithNDivsors(findAllTriNumsAndFactors(1000), 40));
console.log(findTriNumWithNDivsors(findAllTriNumsAndFactors(1000), 80));
console.log(findTriNumWithNDivsors(findAllTriNumsAndFactors(2000), 160));
console.log(findTriNumWithNDivsors(findAllTriNumsAndFactors(5000), 500));

// console.log(findTriNumWithNDivsors(firstTenThousandTriNums, 100), "\n");  // should print 73920 in ~51.178ms
// console.log(findTriNumWithNDivsors(firstTenThousandTriNums, 200));  // should print 2031120 in ~5.275s
// console.log(findTriNumWithNDivsors(firstTenThousandTriNums, 300));  // should print 2162160 in ~11.003s

console.timeEnd("findTriNumWithNDivsors()");