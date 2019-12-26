/**
 * UNDERSTAND: 
 * - Find the FIRST triangle number that has MORE THAN 500 divisors.
 * - What is a "triangle number"?
 *    - A triangle number is a number from a sequence of sums that are made up
 *      by adding a natural number to its previous adjacent natural number
 *      (beginning with 1 as the first natural and first triangle number).
 *
 * PLAN: (1)  Create a function, 'findAllTriNums()', that takes in one input,
 *            'upperLimitNum', which denotes the total number of triangle 
 *            numbers to be returned in an array, 'triNumsArr'. 
 * 
 *       (2)  Create another function, 'findTriNumWithNDivsors()', that takes 
 *            in 2 inputs, 'triNumsArr' & 'greaterThan'. This function will 
 *            loop through the 'triNumsArr' to find the first triangle number 
 *            that has a total number of divisors GREATER THAN the 
 *            'greaterThan' input.
 */

const assert = require("assert");

("use strict");

const firstFourTriNums = [1, 3, 6, 10];
const firstTenTriNums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55];

function findAllTriNums(upperLimitNum) {
  if (Number.isInteger(upperLimitNum) && upperLimitNum > 0) {
    let currentTriNum = 0;
    const triNumsArr = [];
  
    for (let i = 1; i <= upperLimitNum; i++) {
      currentTriNum += i; 
      triNumsArr.push(currentTriNum);
    }
  
    return triNumsArr;
  }

  // console.error("Please enter a valid input");
  return false;
}

assert.deepStrictEqual(findAllTriNums(4), firstFourTriNums, "The first four triangle numbers are: 1, 3, 6, and 10.");
assert.deepStrictEqual(findAllTriNums(10), firstTenTriNums, "The first four triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 45, & 55.");
assert.deepStrictEqual(findAllTriNums(-4), false, "The input type must be a positive integer");
assert.deepStrictEqual(findAllTriNums(1.5), false, "The input type must be a positive integer");

console.log("\n**--- ALL TESTS FOR 'findAllTriNums()' PASSED ---**");




const firstHundredTriNums = findAllTriNums(100);
const firstThousandTriNums = findAllTriNums(1000);
const firstTenThousandTriNums = findAllTriNums(10000);
const firstHundredThousandTriNums = findAllTriNums(100000);

console.time("findTriNumWithNDivsors()");
function findTriNumWithNDivsors(triNumsArr, greaterThan) {
  let triNum = 0;

  for (let i = 0; i < triNumsArr.length; i++) {
    triNum = triNumsArr[i];
    // console.log(`\ntriNum = ${triNumsArr[i]}`);
    
    let triNumFactors = [];

    for (let j = 1; j <= triNumsArr[i]; j++) {
      if (triNumsArr[i] % j === 0) {
        triNumFactors.push(j);
      }
    }
    // console.log(`The factors for ${triNumsArr[i]} = ${triNumFactors}`);

    if (triNumFactors.length > greaterThan) {
      // console.log(`\n${triNumsArr[i]} is the FIRST tri num with GREATER THAN ${greaterThan} divisors! (${triNumFactors.length} total)`);
      // console.log(`The factors for ${triNumsArr[i]} = ${triNumFactors}`);
      return triNum;
    }
    
  }
  return `\nThere were no triangle numbers in this array that had MORE THAN ${greaterThan} divisors`;
}

assert.deepStrictEqual(findTriNumWithNDivsors(firstTenTriNums, 4), 28, "The first triangle number with more than 4 divisors is 28");
assert.deepStrictEqual(findTriNumWithNDivsors(firstTenTriNums, 5), 28, "The first triangle number with more than 5 divisors is 28");
assert.deepStrictEqual(findTriNumWithNDivsors(firstTenTriNums, 6), 36, "The first triangle number with more than 6 divisors is 36");
assert.deepStrictEqual(findTriNumWithNDivsors(firstHundredTriNums, 20), 630, "The first triangle number with more than 6 divisors is 36");
assert.deepStrictEqual(findTriNumWithNDivsors(firstHundredTriNums, 50), "\nThere were no triangle numbers in this array that had MORE THAN 50 divisors", "This array has no triangle numbers with more than 50 divisors");

console.log("---** ALL TESTS FOR 'findTriNumWithNDivsors()' PASSED **---\n");
console.timeEnd("findTriNumWithNDivsors()");