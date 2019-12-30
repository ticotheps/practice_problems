/*----------UNDERSTANDING THE PROBLEM----------
- Objective 
  - Sum up one-hundred 50-digit numbers and return the FIRST 10 digits of that
    sum.

- Expected Input(s)
  - Number of Expected Parameters: 2
  - Names/Types of Expected Parameters
    - "bigNumsArr" (array; made up of numbers that are stored inside of
      strings)
    - "firstNdigitsOfSum" (number; represents number of left-most digits to
      return from the sum)"

- Expected Output(s)
  - Number of Expected Outputs: 1
  - Names of Expected Output
    - "partialSum" (number; represents the first 'firstNdigitsOfSum' digits from
      the sum)

- Constraints
  - What will make the algorithm fail?
    - Negative numbers?
      - Yes.
    - Number data types?
      - Yes.
      - The numbers included in the given array are too large for JavaScript to
        handle, so they must be stored in strings.
    - Floating point numbers?
      - Yes.
    - Non-alphanumeric characters in the inputs?
      - Yes.
      - The strings included in the array must only contain numbers.

- Example #1
  - const someArrayOfBigNumStrings = [
    "123456789",
    "987654321",
    "192837465",
    "918273645"]
  - Example #1 Inputs: someArrayOfBigNumStrings, 5
  - Example #1 Output: 22222 (2222222220)
*/

/*---------------DEVISING A PLAN---------------
- BRUTE FORCE SOLUTION (Pseudocoded Steps) 

  (1) Create a variable, "bigNumsArr", to hold a list of 100 strings that
      contain 50 numeric characters per string. 

  (2) Create a helper function, "sumOfTwoNumStrings()", which will take in two
      inputs, "strA" & "strB", which are string values that contain only
      numerical characters. The function will convert them into number data 
      types before adding them together and storing them in a new variable
      called 'numSum'. Then, 'numSum' will be converted into a string before 
      being returned.

  (3) Create a function, "nDigitsOfBigSum()", which will take in two inputs,
      "bigNumsArr" & "firstNdigitsOfSum", and return a single output,
      "partialSum".

      (a) Create a variable, "currentSum", that will hold the running total
          sum of the number values that have been added together, but in the
          form of a string. It will be initiated with a value of "0".

      (b) Create another variable, "reversedNumToAdd", that will contain the
          reversed number value of the most currently iterated item from 
          the "bigNumsArr". This variable will contain a string data type.

      (c) Use a 'while' loop to continue popping off items from "bigNumsArr"
          so long as it is not empty.

          (d) Pop off the last item of the array, reverse the string, and then
              set it equal to the "reversedNumToAdd" variable.

          (e) Create a new variable, "reversedCurrentSum", that will reverse
              the value of the "currentSum" variable and store it as a string.

          (f) Call the "sumOfTwoNumStrings()" helper function, passing in 
              "reversedNumToAdd" & "reversedCurrentSum".
      
      (g) Return the first 'n' digits of the large sum.
  ...
*/

/*------------IMPLEMENTING THE PLAN------------*/

const assert = require('assert');

('use strict');

function sumOfTwoNumStrings(strA, strB) {
	const revStrA = strA
		.split('')
		.reverse()
		.join('');
	// console.log('\nstrA = ', strA);
	// console.log('revStrA = ', revStrA);

	const revStrB = strB
		.split('')
		.reverse()
		.join('');
	// console.log('\nstrB = ', strB);
	// console.log('revStrB = ', revStrB);

	let revArrOfSum = [];
	let valueToCarry = 0;
	let diffInLen = strA.length - strB.length;
	// console.log('\ndiffInLen = ', diffInLen);
	let longerString;

	if (diffInLen >= 0) {
		longerString = revStrA;
		// console.log(`\nlongerString = revStrA = ${revStrA}`);
	} else {
		longerString = revStrB;
		// console.log(`\nlongerString = revStrB = ${revStrB}`);
	}

	for (let i = 0; i < longerString.length; i++) {
		let currNumStrA;
		let currNumStrB;

		// console.log('\ni = ', i);
		// console.log(`revStrA[i] = ${revStrA[i]}`);
		// console.log(`revStrB[i] = ${revStrB[i]}\n`);

		if (!revStrA[i]) {
			currNumStrA = 0;
		} else {
			currNumStrA = parseInt(revStrA[i]);
		}

		if (!revStrB[i]) {
			currNumStrB = 0;
		} else {
			currNumStrB = parseInt(revStrB[i]);
		}

		// console.log('currNumStrA = ', currNumStrA);
		// console.log('currNumStrB = ', currNumStrB);
		// console.log('valueToCarry = ', valueToCarry);

		const numSumOfTwoDigitsAndCarry = currNumStrA + currNumStrB + valueToCarry;
		// console.log('\nnumSumOfTwoDigitsAndCarry = ', numSumOfTwoDigitsAndCarry);
		valueToCarry = 0;

		const strSumOfTwoDigits = numSumOfTwoDigitsAndCarry.toString();

		let sumOfDigitsArr;
		let lastDigitOfSum;

		if (numSumOfTwoDigitsAndCarry >= 10) {
			sumOfDigitsArr = strSumOfTwoDigits.split('');
			// console.log('sumOfDigitsArr = ', sumOfDigitsArr);

			valueToCarry = parseInt(sumOfDigitsArr.slice(0, -1).join(''));
			// console.log('(NEW) valueToCarry = ', valueToCarry);

			lastDigitOfSum = sumOfDigitsArr[sumOfDigitsArr.length - 1];
		}

		if (numSumOfTwoDigitsAndCarry < 10) {
			lastDigitOfSum = strSumOfTwoDigits;
		}

		// console.log('\n(BEFORE) revArrOfSum = ', revArrOfSum);
		revArrOfSum.push(lastDigitOfSum);
		// console.log('(ADD) lastDigitOfSum = ', lastDigitOfSum);
		// console.log('(AFTER) revArrOfSum = ', revArrOfSum, '\n');
	}

	return revArrOfSum.reverse().join('');
}

const strExample1 = '12345';
const strExample2 = '15243';
const exampleA = sumOfTwoNumStrings(strExample1, strExample2);
// console.log('\n12345 + 15243 = ', 12345 + 15243);
// console.log(exampleA);

const strExample3 = '67891';
const strExample4 = '16798';
const exampleB = sumOfTwoNumStrings(strExample3, strExample4);
// console.log('\n67891 + 16798 = ', 67891 + 16798);
// console.log(exampleB);

const strExample5 = '678';
const strExample6 = '34567';
const exampleC = sumOfTwoNumStrings(strExample5, strExample6);
// console.log('\n678 + 34567 = ', 678 + 34567);
// console.log(exampleC);

assert.deepStrictEqual(exampleA, '27588', '12345 + 15243 = 27588');
assert.deepStrictEqual(exampleB, '84689', '67891 + 16798 = 84689');
assert.deepStrictEqual(exampleC, '35245', '678 + 34567 = 35245');
console.log("\n*--- ALL TESTS FOR 'sumOfTwoNumStrings()' PASSED ---*\n");

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
