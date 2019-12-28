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
 * (2)  Create a helper function, 'findAllTriNums()', that takes
 *      in one input, 'maxNumOfTriNums', and returns one output, 
 *      'divisorsCache'.
 *
 * (3)  Create another function, 'findTriNumWithNDivsors()', that takes in 2
 *      inputs, 'divisorsCache' & 'threshold', and returns a single output,
 *      'triNum'. This function will first loop through the keys of the
 *      'divisorsCache' object to see if there is a match for the 'threshold'
 *      number, which is the minimum number of divisors (exclusive) that the 
 *      output, 'triNum', must contain to be returned.
 */

const assert = require("assert");

("use strict");

// Creates an array of all triangle numbers up to the designated input
function findAllTriNums(maxNumOfTriNums) {
  // Checks to make sure input is a natural number
  if (!(Number.isInteger(maxNumOfTriNums) && maxNumOfTriNums > 0)) {
    console.error("Please enter a valid input");
    return false;
  }

  // Holds all the triangle numbers that will be calculated
  const triNumsArray = [];
  let currentTriNum = 0;
  
  // Calculates all triangle numbers (from '1' to the 'maxNumOfTriNums') and 
  // adds them to the 'triNumsArray' array.
  for (let i = 1; i <= maxNumOfTriNums; i++) {
    currentTriNum += i; 
    triNumsArray.push(currentTriNum);
  }

  return triNumsArray;
}

const first10TriNums = findAllTriNums(10);
console.log(first10TriNums);


function findAllDivisors(triNumsArray) {
  if (!(typeof triNumsArray === "object")) {
    console.error("Please enter a valid input");
    return false;
  }

  const divisorsCache = {};

  for (let j = 0; j < triNumsArray.length; j++) {
    let triNumFromArray = triNumsArray[j];
    // console.log("triNumFromArray = ", triNumFromArray);
    let divisorsCounter = 0;

    for (let k = 1; k <= triNumsArray[j]; k++) {
      if (triNumFromArray % k === 0) {
        divisorsCounter++;
      }
    }
    // console.log("divisorsCounter = ", divisorsCounter, "\n");

    if (!divisorsCache[divisorsCounter]) {
      divisorsCache[divisorsCounter] = [triNumFromArray];
    } else {
      divisorsCache[divisorsCounter].push(triNumFromArray);
    }
  }
  return divisorsCache;
}

const allDivisorsFirst10 = findAllDivisors(first10TriNums);
console.log(allDivisorsFirst10);


// console.time("findTriNumWithNDivsors()");
// function findTriNumWithNDivsors(divisorsCache, threshold) {
//   let triNum = 0;
//   let totalDivisors = 0;

//   // console.log(divisorsCache);

//   for (key in divisorsCache) {
//     if (key > threshold) {
//       console.log(`\nTriangle number "${Number(divisorsCache[key][0])}" has ${key} divisors, which is greater than our 'threshold' input of ${threshold}`);

//       triNum = Number(divisorsCache[key][0]);
    
//       return triNum;
//     }
//   }
//   return `\nThere were no triangle numbers in this cache that had MORE THAN ${threshold} divisors`;
// }

// console.log(findTriNumWithNDivsors(first10TriNums, 4));  // should print 28 (6 divisors)
// console.log(findTriNumWithNDivsors(first10, 10));  // should print 'There were no triangle numbers in this cache that had MORE THAN 10 divisors'

// console.log("---** ALL TESTS FOR 'findTriNumWithNDivsors()' PASSED **---\n");

// console.log(findTriNumWithNDivsors(findAllTriNums(20), 5));  // 28
// console.log(findTriNumWithNDivsors(findAllTriNums(20), 6));  // 36
// console.log(divisorsCache);
// console.log(divisorsCache);

// console.log(findTriNumWithNDivsors(findAllTriNums(1000), 20));  // 630
// console.log(findTriNumWithNDivsors(findAllTriNums(1000), 40));  // 5460
// console.log(findTriNumWithNDivsors(findAllTriNums(1000), 80));  // 25200
// console.log(findTriNumWithNDivsors(findAllTriNums(2000), 160)); // 749700
// console.log(findTriNumWithNDivsors(findAllTriNums(5000), 500));

// console.log(findTriNumWithNDivsors(firstTenThousandTriNums, 100), "\n");  // should print 73920 in ~51.178ms
// console.log(findTriNumWithNDivsors(firstTenThousandTriNums, 200));  // should print 2031120 in ~5.275s
// console.log(findTriNumWithNDivsors(firstTenThousandTriNums, 300));  // should print 2162160 in ~11.003s

// console.timeEnd("findTriNumWithNDivsors()");