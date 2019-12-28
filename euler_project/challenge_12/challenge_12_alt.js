/**
 * UNDERSTAND: 
 * - Find the FIRST triangle number that has MORE THAN 500 divisors.
 * - What is a "triangle number"?
 *    - A triangle number is a number from a sequence of sums that are made up
 *      by adding a natural number to its previous adjacent natural number
 *      (beginning with 1 as the first natural and first triangle number).
 *
 * PLAN: 
 * 
 * (1)  Create a 'divisorsCache' object that will hold a key-value pair where
 *      the 'key' is the total number of divisors and the 'value' is an array
 *      containing all the triangle numbers with that number of divisors.
 * 
 * (1)  Create a helper function, 'findAllTriNumsAndFactors()', that takes
 *      in one input, 'maxNumOfTriNums', and returns one output, 
 *      'divisorsCache'.
 *
 * (2)  Create another function, 'findTriNumWithNDivsors()', that takes in 2
 *      inputs, 'divisorsCache' & 'threshold', and returns a single output,
 *      'triNum'. This function will first loop through the keys of the
 *      'divisorsCache' object to see if there is a match for the 'threshold'
 *      number, which is the minimum number of divisors (exclusive) that the 
 *      output, 'triNum', must contain to be returned.
 */

const assert = require("assert");

("use strict");

const divisorsCache = {};

function findAllTriNumsAndFactors(maxNumOfTriNums) {
  if (Number.isInteger(maxNumOfTriNums) && maxNumOfTriNums > 0) {
    let largestCacheKey = 0;
    let currentTriNum = 0;

    for (key in divisorsCache) {
      console.log("key = ", key);
      if (key > largestCacheKey) {
        largestCacheKey = key;
        console.log("largestCacheKey = ", largestCacheKey);
      }
    }
    
    for (let i = 1; i <= maxNumOfTriNums; i++) {
      currentTriNum += i; 
      console.log(`currentTriNum = ${currentTriNum}`);
      if (!(currentTriNum in Object.keys(divisorsCache))) {
        console.log(`${currentTriNum} DOES NOT exist as a key yet!\n`);
        divisorsCache[currentTriNum] = false;
      } else {
        console.log(`${currentTriNum} already exists as a key in the cache\n`);
      }
    }

    for (key in divisorsCache) {
      // console.log(divisorsCache);
      // console.log("key = ", key);
      let numOfKeysDivisors = 0;

      if (divisorsCache[key] !== false) {
        console.log(`The ${key}-key already already has a value associated with it`);
      } else {
        for (let j = 1; j <= key; j++) {
          if (key % j === 0) {
            numOfKeysDivisors += 1;
          }
        }
        // console.log(`numOfKeysDivisors @ ${key} = ${numOfKeysDivisors}`);
        divisorsCache[key] = numOfKeysDivisors;
      }
    }
    return divisorsCache;
  }

  console.error("Please enter a valid input");
  return false;
}

// console.log(findAllTriNumsAndFactors(5));
// console.log(divisorsCache);
// console.log(findAllTriNumsAndFactors(10));
// console.log(findAllTriNumsAndFactors(100));
// console.log(findAllTriNumsAndFactors(1000));


console.log("\n**--- ALL TESTS FOR 'findAllTriNumsAndFactors()' PASSED ---**\n");


console.time("findTriNumWithNDivsors()");
function findTriNumWithNDivsors(divisorsCache, threshold) {
  let triNum = 0;
  let totalDivisors = 0;

  // console.log(divisorsCache);

  for (key in divisorsCache) {
    if (divisorsCache[key] > threshold) {
      // console.log("\nA key with a value greater than our input already exists in the cache");
      // console.log("divisorsCache key = ", key);
      // console.log("numOfDivisors @ key = ", divisorsCache[key]);

      console.log("\nBEFORE triNum = ", triNum);
      triNum = Number(key);
      console.log("AFTER triNum = ", triNum);

      return triNum;
    }
  }
  return `\nThere were no triangle numbers in this cache that had MORE THAN ${threshold} divisors`;
}

// console.log(findTriNumWithNDivsors(first10, 4));  // should print 28 (6 divisors)
// console.log(findTriNumWithNDivsors(first10, 10));  // should print 'There were no triangle numbers in this cache that had MORE THAN 10 divisors'

console.log("---** ALL TESTS FOR 'findTriNumWithNDivsors()' PASSED **---\n");

console.log(findTriNumWithNDivsors(findAllTriNumsAndFactors(20), 5));  // 28
console.log(findTriNumWithNDivsors(findAllTriNumsAndFactors(20), 6));  // 36
// console.log(divisorsCache);
// console.log(divisorsCache);

// console.log(findTriNumWithNDivsors(findAllTriNumsAndFactors(1000), 20));  // 630
// console.log(findTriNumWithNDivsors(findAllTriNumsAndFactors(1000), 40));  // 5460
// console.log(findTriNumWithNDivsors(findAllTriNumsAndFactors(1000), 80));  // 25200
// console.log(findTriNumWithNDivsors(findAllTriNumsAndFactors(2000), 160)); // 749700
// console.log(findTriNumWithNDivsors(findAllTriNumsAndFactors(5000), 500));

// console.log(findTriNumWithNDivsors(firstTenThousandTriNums, 100), "\n");  // should print 73920 in ~51.178ms
// console.log(findTriNumWithNDivsors(firstTenThousandTriNums, 200));  // should print 2031120 in ~5.275s
// console.log(findTriNumWithNDivsors(firstTenThousandTriNums, 300));  // should print 2162160 in ~11.003s

console.timeEnd("findTriNumWithNDivsors()");