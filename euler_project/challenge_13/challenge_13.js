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
	console.log('revStrA = ', revStrA);

	const revStrB = strB
		.split('')
		.reverse()
		.join('');
	// console.log('\nstrA = ', strB);
	console.log('revStrA = ', revStrB);

	let revStrSum = '';
	let valueToCarry = 0;
  let diffInLen = 0;

	for (let i = 0; i < revStrA.length; i++) {
		console.log('\ni = ', i);
		console.log(`revStrA[i] = ${revStrA[i]}`);
		console.log(`revStrB[i] = ${revStrB[i]}\n`);

    const currNumStrA = parseInt(revStrA[i]);
    const currNumStrB = parseInt(revStrB[i]);
    let sumOfTwoDigits = currNumStrA + currNumStrB;
    if (sumOfTwoDigits )
  };
  
  // if (diffInLen !== 0) {
  //   if (revStrA.length > revStrB.length) {
  //     diffInLen = revStrA.length - revStrB.length;

  //     for (let x = 0; x < revStrA.length; x++) {
  //       console.log("(BEFORE) revStrSum = ", revStrSum);
  //       revStrSum.push(revStrA[revStrB.length + x]);
  //       console.log("(AFTER) revStrSum = ", revStrSum);
  //     }
  //   };

  //   if (revStrA.length < revStrB.length) {
  //     diffInLen = revStrB.length - revStrA.length;

  //     for (let y = 0; y < revStrB.length; y++) {
  //       console.log("(BEFORE) revStrSum = ", revStrSum);
  //       revStrSum.push(revStrB[revStrA.length + y]);
  //       console.log("(AFTER) revStrSum = ", revStrSum);
  //     }
  //   };
  // }

  console.log('\ndiffInLen = ', diffInLen);
	valueToCarry += diffInLen;

	return revStrSum;
}

const strExample1 = '12345';
const strExample2 = '15243';

const example1 = sumOfTwoNumStrings(strExample1, strExample2);
console.log(example1);

// assert.deepStrictEqual(example1, '0');
// console.log("\n*--- ALL TESTS FOR 'sumOfTwoNumStrings()' PASSED ---*");

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
