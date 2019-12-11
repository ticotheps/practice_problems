/* eslint-disable no-console */
/**
 * Write a recursive algorithm for the Fibonacci sequence
 *
 * Fibonacci Sequence
 * fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
 *
 * Each number is the sum of the previous two numbers.
 *
 * Write a program that prints out the nth Fibonacci number.
 *
 * The user can enter any value for 'n'.
 *
 * Constraints:
 *  - Will we always have a valid input? Yes.
 *    - Input will always be between 0 and 10^15
 *  - What is the expected output?
 *    - Just a single number on a line.
 *  - How performant is it?
 *    - Delivers the 1000000th (millionth) number in < 1 second.
 */
const fibArr = []; // memoization
function findNthFibNum(n) {
	console.log(`n = ${n}`);

	if (n === 0) {
		return 1;
	} else if (n === 1) {
		return 2;
	} else {
		return findNthFibNum(n - 1) + findNthFibNum(n - 2);
	}
}

function printFibNum(n) {
	for (let i = 1; i <= 11; i++) {
		console.log(`The ${n} Fibonacci Number is: ${findNthFibNum(n)}`);
	}
}

console.log(printFibNum(0));
console.log(printFibNum(1));
console.log(printFibNum(2));
console.log(printFibNum(3));
console.log(printFibNum(4));
console.log(printFibNum(5));
console.log(printFibNum(6));
console.log(printFibNum(7));
console.log(printFibNum(8));
console.log(printFibNum(9));
console.log(printFibNum(10));
console.log(printFibNum(100));
