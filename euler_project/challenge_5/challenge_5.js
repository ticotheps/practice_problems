/* ----------UNDERSTANDING THE PROBLEM----------
- Objective: Find the smallest positive number that is evenly divisible
  by all of the numbers from 1 to 20.

- Expected Input(s): 
  - Number of Expected Inputs: 2
  - Names of Expected Inputs: 'startNum', 'endNum' (both represent
    a range of numbers that the output can be divided by evenly)
  - Types of the Expected Inputs:
    - 'startNum' => number
    - 'endNum' => number

- Expected Output(s):
  - Number of Expected Outputs: 1
  - Name of Expected Output: 'smallestCommonMultiple'
  - Type of the Expected Output: 'smallestCommonMultiple' => number

- Any Constraints?
  - Can the output be negative?
    - No. It must be positive.
  - Can the numbers that define the range be negative?
    - No. They must be positive.
  - Can the numbers that define the range be floating point numbers?
    - No. They must be integers.

- Example #1:
  - Example Inputs: 
    - 'startNum' = 1
    - 'endNum' = 10
  - Example Output:
    - 'smallestCommonMultiple' = 2520
 */

/* ---------------DEVISING A PLAN---------------
- BRUTE FORCE SOLUTION:
  (1) Create a variable, 'smallestCommonMultiple', using a 'let'
      statement. This variable will hold the current smallest multiple
      that can be evenly divided by each of the numbers in the range
      from 'startNum' to 'endNum' (inclusively).
  (2) Use a 'while' loop to calculate multiples of the 'endNum' as long
      as 'smallestCommonMultiple' is equal to 0.
  (3) Create a variable, 'currentDivisor', using a 'let' statement to
      hold the value of the current divisor being tested. Set the value
      of 'currentDivisor' to 'endNum - 1'.
  (4) Beginning with 'currentDivisor', evaluate each multiple to see if
      it can be evenly divided by 'currentDivisor'.
      (a) Use a 'while' loop that continues as long as 'multiple % 
          currentDivisor === 0'. 
      (b) If the multiple can be evenly divided by 'currentDivisor',
          subtract 1 from 'currentDivisor' and evaluate whether or not
          that 'currentDivisor' can evenly divide into the multiple.
      (c) If that multiple cannot be evenly divided by 'currentDivisor',
          move to the next multiple and set the value of 'currentDivisor'
          back to 'endNum'.
  (5) Return 'smallestCommonMultiple'.
 */

/* ------------IMPLEMENTING THE PLAN------------ */
const assert = require('assert');
('use strict');

const cache = {};

function findSmallestCommonMultiple(startNum, endNum) {
	let smallestCommonMultiple = 0;
	let largestKey = 0;
	let useCache = false;

	if (!Object.keys(cache).length === 0) {
		for (key in cache) {
			if (endNum >= key) {
				largestKey = key;
			}
		}
		useCache = true;
	}

	if (useCache) {
		let currentMultipleWithCache = cache[largestKey];
		if (currentMultipleWithCache % endNum === 0) {
			smallestCommonMultiple = currentMultipleWithCache;
			return smallestCommonMultiple;
		}
	}

	let i = 1;
	let j = 1;

	while (smallestCommonMultiple === 0) {
		let currentMultiple = endNum * i;
		let currentDivisor = endNum - j;

		while (currentMultiple % currentDivisor === 0) {
			currentDivisor -= 1;

			if (currentDivisor === startNum) {
				smallestCommonMultiple = currentMultiple;
				cache[endNum] = smallestCommonMultiple;
				return smallestCommonMultiple;
			}
		}
		i++;
		j = 1;
	}
	return 'There is no common multiple for the range of numbers provided.';
}

assert.deepStrictEqual(
	findSmallestCommonMultiple(1, 10),
	2520,
	'The smallest common multiple between 1 and 10 is 2520'
);

assert.deepStrictEqual(
	findSmallestCommonMultiple(1, 11),
	27720,
	'The smallest common multiple between 1 and 11 is 27720'
);

assert.deepStrictEqual(
	findSmallestCommonMultiple(1, 12),
	27720,
	'The smallest common multiple between 1 and 12 is 27720'
);

assert.deepStrictEqual(
	findSmallestCommonMultiple(1, 13),
	360360,
	'The smallest common multiple between 1 and 13 is 360360'
);

assert.deepStrictEqual(
	findSmallestCommonMultiple(1, 14),
	360360,
	'The smallest common multiple between 1 and 14 is 360360'
);

assert.deepStrictEqual(
	findSmallestCommonMultiple(1, 15),
	360360,
	'The smallest common multiple between 1 and 15 is 360360'
);

assert.deepStrictEqual(
	findSmallestCommonMultiple(1, 15),
	360360,
	'The smallest common multiple between 1 and 15 is 360360'
);

assert.deepStrictEqual(
	findSmallestCommonMultiple(1, 16),
	720720,
	'The smallest common multiple between 1 and 16 is 720720'
);

assert.deepStrictEqual(
	findSmallestCommonMultiple(1, 17),
	12252240,
	'The smallest common multiple between 1 and 17 is 12252240'
);

assert.deepStrictEqual(
	findSmallestCommonMultiple(1, 18),
	12252240,
	'The smallest common multiple between 1 and 18 is 12252240'
);

assert.deepStrictEqual(
	findSmallestCommonMultiple(1, 19),
	232792560,
	'The smallest common multiple between 1 and 19 is 232792560'
);

assert.deepStrictEqual(
	findSmallestCommonMultiple(1, 20),
	232792560,
	'The smallest common multiple between 1 and 20 is 232792560'
);

console.log(`***** ALL TESTS HAVE PASSED *****`);
console.log(findSmallestCommonMultiple(1, 20)); // 232,792,560

/* ------------REFLECTING/ITERATING-------------
- BRUTE FORCE SOLUTION
  - Were you able to find the lowest common multiple for the example 
    input provided and for all numbers 1 to 20 (inclusive)?
    - No. My brute force solution was only able to find the LCM for
      numbers between 1 and 10 (inclusive).
  - What was the Time/Space Complexity of this solution?
    - Time Complexity: O(n^2) = quadratic time 
    - Space Complexity: O(1) = constant space
  - Could you improve the Time/Space Complexity of this solution?
    - YES!
    - How?
      - Use a 'cache' object to store the lowest common multiples that 
        were for calculated for previous inputs.
      - If a provided input shares the same 'startNum' AND has a larger
        'endNum' than the largest key in the 'cache' object, use the
        O(1) lookup run time of the cache object to begin our search at
        the value of the largest key in the 'cache' object.

- ITERATED SOLUTION
  - Were you able to find the lowest common multiple for the example 
    input provided and for all numbers 1 to 20 (inclusive)?
    - Yes. My iterated solution was able to find the LCM for all
      numbers between 1 and 20 (inclusive).
  - What was the Time/Space Complexity of this solution?
    - Time Complexity: O(n/2) = O(n) = linear time 
    - Space Complexity: O(n) = linear space
 */
