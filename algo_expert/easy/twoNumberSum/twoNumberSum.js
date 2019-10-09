/* UNDERSTANDING THE PROBLEM
Expected Inputs:
- 2 inputs
  - (1) type: array
    - non-empty
    - contains DISTINCT integer
  - (2) type: integer
    - represents a target sum

Expected Outputs:
- 1 output
  - type: array
    - contains one of the following:
      - (a) two integers, from the input array, IF those two integers sum
            up to the second provided input (target sum integer)
      - (b) no contents (empty), IF no two integers from teh input array
            sum up to the second provided input (target sum integer)

Any Constraints?
  - Can the integers be negative?
    -Yes
  - Define 'integers' 
    -whole numbers only; no fractions
  - Assume that there will be AT MOST only ONE pair of integers that sum
    up to the provided second input
*/

/*
Examples:
  - Input #1a: [1, 2, 3, 4, 5]
  - Input #1b: 8
  - Output #1: [3, 5]

  - Input #2a: [2, 4, 6, 8, 10]
  - Input #2b: 15
  - Output #2: []

  - Input #3a: [-1, 1, 3, 5, 7]
  - Input #3b: 4
  - Output #3: [-1, 5]

  - Input #4a: [-8, 22, 4, -5, 3]
  - Input #4b: 17
  - Output #4: [-5, 22]
*/

/* DEVISING A PLAN

BRUTE FORCE SOLUTION:
  - Iterate through the array using nested 'for' loops to individually
    check for any pairs of numbers that sum up to the target sum.
    - Runtime Complexity: O(n^2); quadratic
    - Space Complexity: O(1); constant
  
  - Pseudocode:
    - (1) Create a variable 'resultArray' and set it equal to an empty array
    - (2) Iterate through the array using the first of two 'for' loops
    - (3) While inside of the first 'for' loop, iterate AGAIN through the
          array with a nested 'for' loop
    - (4) While inside of the nested 'for' loop, evaluate whether or not
          your two 'for' loop variables sum up to the 'targetSum' input
          that was initially provided
    - (5) While inside the conditional 'if' statement, if the 2 integers
          being compared DO sum up to the target sum, evaluate which of
          the two integers is smaller and push that integer into the
          resultArray' first, and then push the other integer into the
          'resultArray' afterwards.
    - (6) While inside the conditional 'if' statement, if any 2 integers
          being compared DO NOT sum up to the target sum, continue on to
          the next interation.
    - (7) After completely iterating through both nested 'for' loops,
          return 'resultArray'.
*/

// IMPLEMENTING THE PLAN

const array1 = [1, 2, 3, 4, 5];
const targetSum1 = 8;

const twoNumberSum = (array, targetSum) => {
  const resultArray = [];

  for (let i = 0; i < array.length; i++) {
    console.log(`OUTER LOOP; i = ${i}`);
    for (let j = 0; j < array.length; j++) {
      console.log(`---INNER LOOP; j = ${j}`);
      if (i !== j && array[i] + array[j] === targetSum) {
        console.log('We have a pair of ints that add up to targetSum!');
        if (array[i] < array[j]) {
          resultArray.push(array[i]);
          resultArray.push(array[j]);
        } else {
          resultArray.push(array[j]);
          resultArray.push(array[i]);
        }
        return resultArray;
      }
    }
  }
  return resultArray;
};

console.log(twoNumberSum(array1, targetSum1));
