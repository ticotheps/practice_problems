/*---------------UNDERSTANDING THE PROBLEM---------------
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
        - (a) two integers, from the input array, IF those two integers 
              sum up to the second provided input (target sum integer).
        - (b) no contents (empty), IF no two integers from the input 
              array sum up to the second provided input (target sum 
              integer).

Any Constraints?
  - Can the integers be negative?
    -Yes
  - Define 'integers' 
    -whole numbers only; no fractions
  - Assume that there will be AT MOST only ONE pair of integers that sum
    up to the provided second input
    
Examples:
  - Input #1a: [1, 2, 3, 4, 5]
  - Input #1b: 8
  - Output #1: [3, 5]

  - Input #2a: [2, 4, 6, 8, 10]
  - Input #2b: 15
  - Output #2: []

  - Input #3a: [-1, 2, 3, 5, 7]
  - Input #3b: 4
  - Output #3: [-1, 5]

  - Input #4a: [-8, 22, 4, -5, 3]
  - Input #4b: 17
  - Output #4: [-5, 22]

  - Input #5a: [-123, -492, 40, 181, 319, 79, -43, -12, 3, 99]
  - Input #5b: -393
  - Output #5: [-492, 99]
*/

/*---------------DEVISING A PLAN---------------

BRUTE FORCE SOLUTION:
  - Runtime Complexity: O(n^2); quadratic
  - Space Complexity: O(1); constant
  - Iterates through the array using nested 'for' loops to individually
    check for any pairs of numbers that sum up to the target sum.

  - Pseudocode:
    - (1) Create a variable 'resultArray' and set it equal to an empty 
          array.
    - (2) Iterate through the array using the first of two 'for' loops.
    - (3) While inside of the first 'for' loop, iterate AGAIN through the
          array with a nested 'for' loop.
    - (4) While inside of the nested 'for' loop, evaluate whether or not
          your two 'for' loop variables sum up to the 'targetSum' input
          that was initially provided.
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

//---------------IMPLEMENTING THE PLAN---------------

const twoNumberSum = (array, targetSum) => {
  const resultArray = [];

  for (let i = 0; i < array.length; i++) {
    // console.log(`OUTER LOOP; i = ${i}`);
    for (let j = 0; j < array.length; j++) {
      // console.log(`---INNER LOOP; j = ${j}`);
      if (i !== j && array[i] + array[j] === targetSum) {
        // console.log('We have ints that add up to targetSum!');
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

console.log('\n---------------BRUTE FORCE SOLUTION---------------');
console.log(twoNumberSum([1, 2, 3, 4, 5], 8)); // returns [3, 5]
console.log(twoNumberSum([2, 4, 6, 8, 10], 15)); // returns []
console.log(twoNumberSum([-1, 2, 3, 5, 7], 4)); // returns [-1, 5]
console.log(twoNumberSum([-8, 22, 4, -5, 3], 17)); // returns [-5, 22]
console.log(
  twoNumberSum([-123, -492, 40, 181, 319, 79, -43, -12, 3, 99], -393)
); // returns [-492, 99]
console.log('---------------BRUTE FORCE SOLUTION---------------\n');

/*---------------REFLECTING/ITERATING---------------
- Brute Force Solution Runtime Complexity: O(n^2)
- Brute Force Solution Space Complexity: O(1)

- Can I make my brute force solution FASTER?
  - Yes.
- How much faster & space-efficient will your new solution be?
  - O(n) runtime complexity; O(n) space complexity
- How will you do it?
  - First, create a new variable called 'cache' and set it equal to
    an empty object (i.e. - {}). We will achieve O(1), linear time,
    with lookup using this object instead of an array.
  - Use ONE 'for' loop + 'caching' instead of using 2 nested 'for' loops.
  - The single 'for' loop will iterate through the given array.
    - While inside of the 'for' loop, the difference between 'array[i]' &
      'targetSum' will be calculated and stored as an integer in a new
      locally-scoped variable calledd 'diff'.
    - While still inside of the 'for' loop, we will evaluate whether or 
      not 'array[i]' exists as a value for any of the keys in the 'cache'
      object.
        - If 'array[i]' ALREADY exists as a key in the 'cache' object, 
          this means that 'array[i]' can be added to the matching key's 
          value (another integer from the input array) to sum up to the
          'targetSum'.
          - If 'array[i]' is smaller than 'cache[key]', then return an
            an array '[array[i], cache[key]]'.
          - If 'array[i]' is larger than 'cache[key]', then return an
            an array '[cache[key], array[i]]'.
        - If 'array[i]' DOES NOT ALREADY exist as a key in the 'cache'
          object, store a new key-value pair in the 'cache' object,
          where the calculated integer value of 'diff' is the key
          and 'array[i]' is the value of that key.
  - Return an empty array if there are no satisfied conditions from all
    the iterations of the 'for' loop.
*/

const twoNumberSumImproved = (array, targetSum) => {
  const cache = {};

  for (let i = 0; i < array.length; i++) {
    let diff = targetSum - array[i];
    // console.log(`FOR LOOP; i = ${i}, diff = ${diff}`);

    if (array[i] in cache) {
      // console.log(`array[${i}] exists as a key in the 'cache'!`);
      const keysValue = cache[array[i]];

      if (array[i] < keysValue) {
        return [array[i], keysValue];
      } else {
        return [keysValue, array[i]];
      }
    } else {
      // console.log("Just added a new key-value pair to the 'cache'!");
      cache[diff] = array[i];
    }
  }
  return [];
};

console.log('---------------IMPROVED SOLUTION---------------');
console.log(twoNumberSumImproved([1, 2, 3, 4, 5], 8)); // returns [3, 5]
console.log(twoNumberSumImproved([2, 4, 6, 8, 10], 15)); // returns []
console.log(twoNumberSumImproved([-1, 2, 3, 5, 7], 4)); // returns [-1, 5]
console.log(twoNumberSumImproved([-8, 22, 4, -5, 3], 17)); // returns [-5, 22]
console.log(
  twoNumberSumImproved([-123, -492, 40, 181, 319, 79, -43, -12, 3, 99], -393)
); // returns [-492, 99]
console.log('---------------IMPROVED SOLUTION---------------\n');
