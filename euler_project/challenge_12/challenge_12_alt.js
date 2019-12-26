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

function findAllTriNumsAndFactors(maxNumOfTriNums) {
  if (Number.isInteger(maxNumOfTriNums) && maxNumOfTriNums > 0) {
    let currentTriNum = 0;
    const triNumsCache = {};
  
    for (let i = 1; i <= maxNumOfTriNums; i++) {
      currentTriNum += i; 
      triNumsCache[currentTriNum] = false;
    }

    for (key in triNumsCache) {
      let numOfKeysDivisors = 0;
      for (let j = 1; j <= key; j++) {
        if (key % j === 0) {
          numOfKeysDivisors += 1;
        }
      }
      // console.log(`numOfKeysDivisors @ ${key} = ${numOfKeysDivisors}`);
      triNumsCache[key] = numOfKeysDivisors;
    }
    // console.log(triNumsCache);
    return triNumsCache;
  }

  console.error("Please enter a valid input");
  return false;
}

const first5 = findAllTriNumsAndFactors(5);
const first10 = findAllTriNumsAndFactors(10);
// findAllTriNumsAndFactors(10);

assert.deepStrictEqual(findAllTriNumsAndFactors(5), first5, "The first 5 triangle numbers are: 1, 3, 6, 10, & 15.");
assert.deepStrictEqual(findAllTriNumsAndFactors(10), first10, "The first 5 triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55.");
// assert.deepStrictEqual(findAllTriNumsAndFactors(10), firstTenTriNums, "The first four triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 45, & 55.");
// assert.deepStrictEqual(findAllTriNumsAndFactors(-4), false, "The input type must be a positive integer");
// assert.deepStrictEqual(findAllTriNumsAndFactors(1.5), false, "The input type must be a positive integer");

console.log("\n**--- ALL TESTS FOR 'findAllTriNumsAndFactors()' PASSED ---**\n");


// const firstHundredTriNums = findAllTriNumsAndFactors(100);
// const firstThousandTriNums = findAllTriNumsAndFactors(1000);
// const firstTenThousandTriNums = findAllTriNumsAndFactors(10000);
// const firstHundredThousandTriNums = findAllTriNumsAndFactors(100000);


console.time("findTriNumWithNDivsors()");
function findTriNumWithNDivsors(triNumsCache, threshold) {
  let triNum = 0;
  let totalDivisors = 0;
  let largestCacheKey = 0;

  console.log(triNumsCache);

  for (key in triNumsCache) {
    if (triNumsCache[key] > threshold) {
      console.log("\nA key with a value greater than our input already exists in the cache");
      console.log("triNumsCache key = ", key);
      console.log("numOfDivisors @ key = ", triNumsCache[key]);

      console.log("\nBEFORE triNum = ", triNum);
      triNum = key;
      console.log("AFTER triNum = ", triNum);

      return triNum;

    } else if (triNumsCache[key] <= threshold) {
      if (key > largestCacheKey) {
        console.log("\nBEFORE largestCacheKey = ", largestCacheKey);
        largestCacheKey = key;
        console.log("AFTER largestCacheKey = ", largestCacheKey);

        console.log("\nBEFORE totalDivisors = ", totalDivisors);
        totalDivisors = triNumsCache[key];
        console.log("AFTER totalDivisors = ", totalDivisors);
      }
    }
  }


  // for (let i = 0; i < triNumsCache.length; i++) {
  //   triNum = triNumsCache[i];
  //   // console.log(`\ntriNum = ${triNumsCache[i]}`);
    
  //   let triNumFactors = [];

  //   for (let j = 1; j <= triNumsCache[i]; j++) {
  //     if (triNumsCache[i] % j === 0) {
  //       triNumFactors.push(j);
  //     }
  //   }
  //   // console.log(`The factors for ${triNumsCache[i]} = ${triNumFactors}`);

  //   if (triNumFactors.length > threshold) {
  //     // console.log(`\n${triNumsCache[i]} is the FIRST tri num with GREATER THAN ${threshold} divisors! (${triNumFactors.length} total)`);
  //     // console.log(`The factors for ${triNumsCache[i]} = ${triNumFactors}`);
  //     return triNum;
  //   }
    
  // }
  return `\nThere were no triangle numbers in this cache that had MORE THAN ${threshold} divisors`;
}

// console.log(findTriNumWithNDivsors(firstTenTriNums, 4));  // should print 28

// assert.deepStrictEqual(findTriNumWithNDivsors(firstTenTriNums, 4), 28, "The first triangle number with more than 4 divisors is 28");
// assert.deepStrictEqual(findTriNumWithNDivsors(firstTenTriNums, 5), 28, "The first triangle number with more than 5 divisors is 28");
// assert.deepStrictEqual(findTriNumWithNDivsors(firstTenTriNums, 6), 36, "The first triangle number with more than 6 divisors is 36");
// assert.deepStrictEqual(findTriNumWithNDivsors(firstHundredTriNums, 20), 630, "The first triangle number with more than 6 divisors is 36");
// assert.deepStrictEqual(findTriNumWithNDivsors(firstHundredTriNums, 50), "\nThere were no triangle numbers in this array that had MORE THAN 50 divisors", "This array has no triangle numbers with more than 50 divisors");

// console.log("---** ALL TESTS FOR 'findTriNumWithNDivsors()' PASSED **---\n");

// console.log(findTriNumWithNDivsors(firstTenTriNums, 4));  // should print 25200 in ~13.541ms


// console.log(findTriNumWithNDivsors(firstTenThousandTriNums, 100), "\n");  // should print 73920 in ~51.178ms
// console.log(findTriNumWithNDivsors(firstTenThousandTriNums, 200));  // should print 2031120 in ~5.275s
// console.log(findTriNumWithNDivsors(firstTenThousandTriNums, 300));  // should print 2162160 in ~11.003s

console.timeEnd("findTriNumWithNDivsors()");