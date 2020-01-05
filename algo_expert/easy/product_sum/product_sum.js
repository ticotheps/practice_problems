/*----------UNDERSTANDING THE PROBLEM----------
- Objective 
  - Find the 'product sum' of the given "special" array.

- Definitions
  - Characteristics of a "special array":
    - The array will always be non-empty
    - It can only contain either integers or OTHER special arrays.

  - "Product Sum": the value that results when all the items in the array are
    added together and then multiplied by the level of their depth. 
    - For example, an array containing only integers will have its sum
      multiplied by 1 because it doesn't contain any nested OTHER special arrays
      within it.
    - However, if an array contains integers AND other nested special arrays,
      the 'multiplier' for those nested special arrays will differ from the
      multiplier used with the integers of the outermost special array.

- Expected Input(s)
  - Number of Expected Parameters: 1
  - Names/Data Types of Expected Parameters
    - "specialArr" (an array; must only contain Number or Array data types)

- Expected Output(s)
  - Number of Expected Outputs: 1
  - Names/Data Types of Expected Output
    - "productSum" (a number)

- Constraints
  - Will the following make the algorithm fail?
    - Negative numbers?
      - No.
    - Number data types?
      - No.
    - Floating point numbers?
      - Yes.
      - Must be integers only.
    - Non-alphanumeric characters in the inputs?
      - Yes.
      - Must be integers (negative or positive) only.

- Example #1
  - Example #1 Input(s): [1, 2, 3, 4, 5]
  - Example #1 Output(s): 15 (=> 1 * (1 + 2 + 3 + 4 + 5))

- Example #2
  - Example #2 Input(s): [1, [2, 3], 4, 5]
  - Example #2 Output(s): 20 (=> 1 * (1 + (2 * (2 + 3)) + 4 + 5))

- Example #3
  - Example #3 Input(s): [1, [2, [3, 4], 5]]
  - Example #3 Output(s): 57 (=> 1 * (1 + (2 * (2 + (3 * (3 + 4)) + 5)))
*/

/*---------------DEVISING A PLAN---------------
- BRUTE FORCE SOLUTION (Pseudocoded Steps) 
  (1) Create a helper function ("findItemProductSum()") that will take in an
      item from the special array and return its product sum.
  (2) Create a variable ("multiplier") that will hold the value of the number
      to be multiplied to the sum at each depth.
  (3) Create another variable ("totalProductSum") that will hold the running 
      total of all the product sums added together.
  (4) Find the length of the given special array.
  (5) Iterate through the given special array.
  (6) Based on the number of items in the array, which can be either an integer
      or another special array, call the helper function on each item.
  (7) Return the "totalSum" variable.
*/

/*------------IMPLEMENTING THE PLAN------------*/

const assert = require('assert');

('use strict');

// helper function - produces product sum of each individual item in the given
// special array
function findItemProductSum(item) {
	// console.log(`item = ${item}`);
	let totalProductSum = 0;

	// checks for proper input (number, integer)
	if (typeof item === 'number' && Number.isInteger(item)) {
		console.log("\nInput is a 'number' data type");

		totalProductSum += item;
		console.log(`totalProductSum (mutated) = ${totalProductSum}`);
	} else if (typeof item === 'object') {
		console.log("\nInput is an 'object' data type (array)");

		for (let i = 0; i < item.length; i++) {
			console.log(`i[${i}] = ${item[i]}`);
		}
	} else {
		console.log(`\nInput, "${item}", is NOT an 'object' or 'number' data type`);
		return `Input is NOT a 'number' or 'object' data type; please try different data type`;
	}

	return totalProductSum;
}

assert.deepStrictEqual(
	findItemProductSum(1),
	1,
	"When 'item' is passed to this function, 'item' is also returned"
);
assert.deepStrictEqual(
	findItemProductSum(-1),
	-1,
	"When 'item' is passed to this function, 'item' is also returned"
);
assert.deepStrictEqual(
	findItemProductSum([4, 3, 2, 1]),
	0,
	"When 'item' is passed to this function, 'item' is also returned"
);
assert.deepStrictEqual(
	findItemProductSum(true),
	"Input is NOT a 'number' or 'object' data type; please try different data type",
	"True is NOT a 'number' or 'object' data type; it is a Boolean value"
);

console.log("***---ALL TESTS FOR 'findItemProductSum' PASSED---***");

/*--------REFLECTING/ITERATING THE PLAN--------
- BRUTE FORCE SOLUTION ANALYSIS
  - Were you able to arrive at the correct answer with your solution?
    - Yes/No
  - Analyze the Time & Space Complexity of your solution.
    - Time Complexity: 
    - Space Complexity: 
  - Could either, Time or Space Complexity, be improved in your solution?
    - Yes/No
  - If so, how would you go about improving it?
  - What is the new Time & Space Complexity of your improved solution?
*/
