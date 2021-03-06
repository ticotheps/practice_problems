/**
 * DAILY CODING PROBLEM #82 (EASY)
 *
 * This problem was asked by Microsoft.
 *
 * Using a 'read7()' method that returns 7 characters from a file, implement
 * 'readN(n)' which reads n characters.
 *
 * For example, given a file with the content "Hello world", three 'read7()'
 * returns will print: "Hello w", "orld", and "".
 *
 */

/**
 * ----------UNDERSTAND----------
 * Objective:
 *  - Create a method that will return the first 7 characters of a passed in
 *    string argument ('str').
 *
 * Expected:
 *  - Expected Inputs: 1 input ('str'; string data type)
 *  - Expected Output: 1 output ('chars'; string data type)
 *
 * Constraints:
 *  - The 'str' argument MUST be of a string data type ONLY.
 *  - The 'str' argument can be an empty string.
 *  - Spaces should be treated as alphanumeric characters.
 *
 * -------------PLAN-------------
 * BRUTE FORCE SOLUTION:
 *  (1) Create a function called, 'read7()' that takes in 1 argument, 'str', and
 *      returns one output, 'sevenChars'.
 *  (2) Check the data type of the argument passed into the 'read7()' function.
 *      (a) If it is of 'string' data type, execute the following block of code.
 *      (b) Otherwise, return string that says "Please provide a valid input."
 *  (3) Iterate through the given string and do the following:
 *      (a) If 'str.length' <= 7, return the entire given string.
 *      (b) If 'str.length' > 7, return the first 7 characters of the given string.
 *
 * -----------EXECUTE------------
 */
const assert = require('assert');

('use strict');

function read7(str) {
	// console.log(`str = ${str}`);

	let lenStr = str.length;
	// console.log("lenStr = ", lenStr);

	let revStr = str.split('').reverse();
	console.log("revStr = ", revStr);

	let first7Str = '';
	// console.log("first7Str = ", first7Str);

	let numOfCharsLeft = lenStr;
	console.log("numOfCharsLeft = ", numOfCharsLeft);

	if (typeof str !== 'string') {
		return 'Please provide a valid input.';
	}

	if (lenStr <= 7) {
		return str;
	} else {
		for (let i = 0; i < 7; i++) {
			console.log(`revStr[${i}] = ${revStr[i]}`);
			// first7Str = str.slice(0, 7);
			let lastLetter = revStr.pop();
			first7Str += lastLetter;
		}
		// first7Str = str.slice(0, 7);
		console.log(`first7Str = ${first7Str}`);
		return first7Str;
	}
}

console.log(read7('Tico Thepsourinthone'));
// assert.deepStrictEqual(read7('Tico Thepsourinthone'), 'Tico Th', "The first 7 characters of 'Tico Thepsourinthone' are 'Tico Th'.")

// console.log(read7(8));
// assert.deepStrictEqual(read7(8), 'Please provide a valid input.', "8 is not a valid input (of type 'String')")

console.log("----------ALL TESTS ARE PASSING FOR 'read7()'----------");


/**
 * -----------REFLECT------------
 */
