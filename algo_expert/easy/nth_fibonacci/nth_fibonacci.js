const assert = require('assert');

('use strict');

function getNthFib(n) {
	// Declare the output variable to be returned.
	let nthFibNum = 0;

	// Initialize an array, with values 0 and 1 (respectively), to store
	// the Fibonacci sequence.
	const fibArr = [0, 1];

	if (n <= 0) {
		return 'Sorry. Please pass an input value greater than 0.';
	} else if (n === 1) {
		return 0;
	} else if (n === 2) {
		return 1;
	} else {
		const startIndex = 2;
		for (let i = startIndex; i < n; i++) {
			const twoNumsPrev = fibArr[i - 2];
			const oneNumPrev = fibArr[i - 1];
			const newFibNum = twoNumsPrev + oneNumPrev;
			// console.log(`fibArr_before = ${fibArr}`);
			fibArr.push(newFibNum);
			// console.log(`fibArr_after = ${fibArr}`);
		}
		nthFibNum = fibArr[n - 1];
		return nthFibNum;
	}
}

console.log('------------------TEST CASES------------------');
assert.deepStrictEqual(
	getNthFib(0),
	'Sorry. Please pass an input value greater than 0.',
	'There is no such thing as a "0th Fibonacci number."'
);
assert.deepStrictEqual(getNthFib(2), 1, '1 is the 2nd Fibonacci number');
assert.deepStrictEqual(getNthFib(4), 2, '2 is the 4th Fibonacci number');
assert.deepStrictEqual(getNthFib(6), 5, '5 is the 6th Fibonacci number');
console.log('----------ALL TEST CASES ARE PASSING----------');

// console.log(getNthFib(0)); // should return "Sorry. Please pass an input value greater than 0."
// console.log(getNthFib(2)); // should return 1
// console.log(getNthFib(4)); // should return 2
// console.log(getNthFib(6)); // should return 5
