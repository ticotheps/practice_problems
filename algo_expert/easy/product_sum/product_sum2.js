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
 * BRUTE FORCE SOLUTION
 *  (1) Use recursion to find the product sum.
 *  (2)
 *
 */

let outermostArray = [];
let currArrayDepth;
function findSum(array) {
	currArrayDepth = 1;
	for (let i = 0; i < array.length; i++) {
		console.log('INITIAL outermostArray = ', outermostArray);
		console.log('INITIAL currArrayDepth = ', currArrayDepth);
		if (Number.isInteger(array[i])) {
			const itemProductSum = currArrayDepth * array[i];
			console.log(
				`array[${i}] = `,
				array[i],
				'(NUMBER Data Type => add to outermostArray)'
			);
			console.log(
				`itemProductSum @ array[${i}] = ${array[i]} * ${currArrayDepth}(currArrayDepth)`,
				itemProductSum,
				'(add to outermostArray)'
			);
			outermostArray.push(itemProductSum);
			console.log('NEW outermostArray = ', outermostArray, '\n');
		} else {
			console.log(
				`array[${i}] = `,
				array[i],
				'(OBJECT Data Type => recursive call)'
			);
			currArrayDepth += 1;
			console.log('NEW currArrayDepth = ', currArrayDepth);
			console.log('-----CAUTION! ENTERING AN INNER ARRAY----');
			findSum(array[i]);
			// innerArray.push(innerItemProductSum);
			// console.log('innerArray = ', innerArray);
		}
	}

	const productSum = outermostArray.reduce((acc, num) => {
		return (acc += num);
	}, 0);

	return productSum;
}

// console.log(findSum([1, 3, 5]));
console.log(findSum([1, [3], 5]));
