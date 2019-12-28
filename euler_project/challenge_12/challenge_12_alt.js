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

// Holds all the triangle numbers that will be calculated
const triNumsArray = [];
let counter = 0;

// Creates an array of all triangle numbers up to the designated input
function findAllTriNums(maxNumOfTriNums) {
  // Checks to make sure input is a natural number
  if (!(Number.isInteger(maxNumOfTriNums) && maxNumOfTriNums > 0)) {
    console.error("Please enter a valid input");
    return false;
  }

  let currentTriNum = 0;
  
  // console.log("length = ", triNumsArray.length);
  if (triNumsArray.length !== 0) {
    // lastItem = triNumsArray.length - 1;
    currentTriNum = triNumsArray[triNumsArray.length - 1];
    // console.log("currentTriNum = ", currentTriNum);

    // for (let j = counter + 1; j <= maxNumOfTriNums; j++) {
    //   console.log("j = ", j);
    //   // if (triNumsArray[j] !== currentTriNum) {
    //     // currentTriNum = triNumsArray[triNumsArray.length - 1] + j; 
    //     currentTriNum += j; 
    //     triNumsArray.push(currentTriNum);
    //     counter++;
    //     console.log(`ADD ${currentTriNum} to the array; counter = ${counter}`);
    //   // }
    // }
  }
    // currentTriNum = 0;
    // Calculates all triangle numbers (from '1' to the 'maxNumOfTriNums') and 
    // adds them to the 'triNumsArray' array.
    for (let i = counter + 1; i <= maxNumOfTriNums; i++) {
      currentTriNum += i; 
      triNumsArray.push(currentTriNum);
      counter++;
      // console.log(`Add ${currentTriNum} to the array; counter = ${counter}`);
    }
  // console.log("counter = ", counter);
  return triNumsArray;
}

// const triNums10Array = findAllTriNums(10);
// console.log(triNums10Array);
// const triNums50Array = findAllTriNums(50);
// console.log(triNums50Array);
// const triNums100Array = findAllTriNums(100);
// console.log(triNums100Array);
// const triNums1000Array = findAllTriNums(1000);
// console.log(triNums1000Array);
// const triNums10000Array = findAllTriNums(10000);
// console.log(triNums10000Array);
// const triNums20000Array = findAllTriNums(20000);
// console.log(triNums20000Array);


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
      divisorsCache[divisorsCounter] = triNumFromArray;
    }
  }
  return divisorsCache;
}

// const allDivisors10Cache = findAllDivisors(triNums10Array);
// console.log(allDivisors10Cache);
// const allDivisors100Cache = findAllDivisors(triNums100Array);
// console.log(allDivisors100Cache);
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
      console.log(`\nAt ${key} divisors, "${Number(divisorsCache[key])}" is the 1st triNum to have >${threshold} divisors.`);

      triNum = Number(divisorsCache[key]);
    
      return triNum;
    }
  }
  console.log(`\nNone of the triNums in the cache had >${threshold} divisors.`);
  console.log("Try a larger cache of triNums.");
  return false;
}

// const over5DivisorsTriNum = findTriNumWithNDivsors(allDivisors100Cache, 5);
// console.log(over5DivisorsTriNum);  // 28

function bruteForceSolution(maxNumOfTriNums, threshold) {
  const triNumsArr = findAllTriNums(maxNumOfTriNums);
  const divisorsCache = findAllDivisors(triNumsArr);
  const solution = findTriNumWithNDivsors(divisorsCache, threshold);
  return solution;
}

console.log(bruteForceSolution(100, 10)); // 276 => 12 divisors
console.log(bruteForceSolution(100, 25)); // 3570 => 32 divisors
console.log(bruteForceSolution(100, 50)); // false; runtime = 18.141ms

console.log(bruteForceSolution(1000, 50)); // 64980 => 54 divisors
console.log(bruteForceSolution(1000, 100)); // 97029 => 108 divisors
// console.log(bruteForceSolution(1000, 200)); // false; runtime = 1.719s

// console.log(bruteForceSolution(2000, 200)); // false; runtime = 5.526s

console.log(bruteForceSolution(3000, 200)); // 2031120 => 240 divisors
console.log(bruteForceSolution(3000, 300)); // 2162160 => 320 divisors
// console.log(bruteForceSolution(3000, 400)); // false; runtime = 45.547s

// console.log(bruteForceSolution(3500, 400)); // false; runtime = 54.536s

// console.log(bruteForceSolution(4000, 400)); // false; runtime = 1:06.332 (m:ss.mmm)

// console.log(bruteForceSolution(5000, 400)); // false; runtime = 1:42.189 (m:ss.mmm)

// console.log(bruteForceSolution(6000, 500)); // false; runtime = 2:28.853 (m:ss.mmm)

// console.log(bruteForceSolution(10000, 500)); // false; runtime = 9:39.659
// (m:ss.mmm)

console.log(bruteForceSolution(15000, 500)); // 76576500 => 576 divisors
console.timeEnd("findTriNumWithNDivsors()");

// console.timeEnd("findTriNumWithNDivsors()");