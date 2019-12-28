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

console.time("findTriNumWithNDivsors()");

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

// const triNums10Array = findAllTriNums(10);
// console.log(triNums10Array);
const triNums100Array = findAllTriNums(100);
// console.log(triNums100Array);
// const triNums1000Array = findAllTriNums(1000);
// console.log(triNums1000Array);
// const triNums10000Array = findAllTriNums(10000);
// console.log(triNums10000Array);


const divisorsCache = {};

// Creates an object of all possible numbers of divisors that the triangle
// numbers from the input array could have.
function findAllDivisors(triNumsArray) {
  if (!(typeof triNumsArray === "object")) {
    console.error("Please enter a valid input");
    return false;
  }

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

// const allDivisors10Cache = findAllDivisors(triNums10Array);
// console.log(allDivisors10Cache);
const allDivisors100Cache = findAllDivisors(triNums100Array);
console.log(allDivisors100Cache);
// const allDivisors1000Cache = findAllDivisors(triNums1000Array);
// console.log(allDivisors1000Cache);
// const allDivisors10000Cache = findAllDivisors(triNums10000Array);
// console.log(allDivisors10000Cache);


// Finds the FIRST triangle number that has MORE divisors than the input
// 'threshold' provided.
function findTriNumWithNDivsors(divisorsCache, threshold) {
  let triNum = 0;

  for (key in divisorsCache) {
    if (key > threshold) {
      console.log(`\nTriangle number "${Number(divisorsCache[key][0])}" has ${key} divisors, which is greater than our 'threshold' input of ${threshold}`);

      triNum = Number(divisorsCache[key][0]);
    
      return triNum;
    }
  }
  return `\nThere were no triangle numbers in this cache that had MORE THAN ${threshold} divisors`;
}

const over5DivisorsTriNum = findTriNumWithNDivsors(allDivisors100Cache, 5);
console.log(over5DivisorsTriNum);  // 28
console.timeEnd("findTriNumWithNDivsors()");