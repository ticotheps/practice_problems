/**
 * ALTERNATE SOLUTION TO THE "PRODUCT SUM" PROBLEM
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

// Helper function that calculates the sum of all items in an array
function findSum(array) {
	let productSum = 0;
	console.log('INITIAL productSum = ', productSum);
	console.log('array = ', array);

	for (let i = 0; i < array.length; i++) {
		productSum += array[i];
		console.log('NEW productSum = ', productSum);
	}

	return productSum;
}

console.log(findSum([1, 3, 5]));
