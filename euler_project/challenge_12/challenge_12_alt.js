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
 *       (2)  Create another function, 'findNumOfDivisors()', that takes in 
 *            one input (a number), 'greaterThan', which will loop through the 
 *            'triNumsArr' to find the first triangle number that has a total
 *            number of divisors GREATER THAN the input.
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

console.log("**--- ALL TESTS FOR 'findAllTriNums()' PASSED ---**");