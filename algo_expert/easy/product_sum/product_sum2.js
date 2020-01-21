/**
 * (ALTERNATE SOLUTION TO THE "PRODUCT SUM" PROBLEM)
 *
 * UNDERSTANDING THE PROBLEM
 *  - Iterate through the given 'special' array and add up each of the positive integers to
 *    find the total 'productSum' of that array.
 *
 *  - Before being added to the 'productSum', each positive integer of the array
 *    will be multiplied by a variable, 'multiplier', that is indicative of the
 *    level of depth of that positive integer (with regards to the original
 *    given 'special' array).
 *
 *  - For an array with integers all at level 1 depth:
 *    - Imagine if [1, 3, 5] is your 'special' given array:
 *      - (1*(1)) + (1*(3)) + (1*(5)) => 1 + 3 + 5 => 9
 *
 *  - For an array with some integers at level 1 & some at level 2 depth:
 *    - Imagine if [1, [3], 5] is your 'special' given array:
 *      - (1*(1)) + (2*(3)) + (1*(5)) => 1 + 6 + 5 => 12
 *
 *  - For an array with some integers at level 1, level 2, & level 3 depth:
 *    - Imagine if [1, [3, [5]]] is your 'special' given array:
 *      - (1*(1)) + ((2*(3)) + (2*(3*(5))) => 1 + (6 + 30) => 37
 *
 */

/**
 * DEVISING A PLAN
 *
 * BRUTE FORCE SOLUTION (Recursive Solution)
 *  (1) Create a variable called 'productSum' to store the value of the running
 *  total of all the product sums from the given special array.
 *
 *  (2) Create a function called 'findProductSum()' that takes in 2 parameters,
 *  'specArr' (a special array) and 'multiplier', which has a default value of 1
 *  because every element in the special array will have a depth of AT LEAST 1.
 *  The output of 'findProductSum()' will be a variable called 'productSum',
 *  which will just be a number representing the sum total of all the product
 *  sums in the original special given array.
 *
 *  (3) Iterate through the given special array to determine if the element
 *  being iterated on is either a "Number" data type or an "Object" data type
 *  (arrays are of type "Object" in JavaScript).
 *
 *  (4) If the element is a "Number" data type, add the value of that element
 *  to the value of 'productSum'.
 *
 *  (5) If the element is an "Object" data type, recursively call the
 *  'findProductSum()' function on the element.
 *
 * 	(6) Return 'productSum'.
 *
 */

const assert = require('assert');

('use strict');

function findProductSum(specArr, multiplier = 1) {
	let productSum = 0;
	console.log(`multiplier = ${multiplier}`);

	console.log(`productSum = ${productSum}`);
	return productSum;
}

findProductSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]);
