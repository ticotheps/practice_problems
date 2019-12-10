/*----------UNDERSTANDING THE PROBLEM----------
- Objective 
  - Create an algorithm that will find the "Pythagorean Triplet" for 
    which a + b + c = 1000.

- Definitions
  - "Pythagorean Triplet": a set of 3 "natural numbers" that have the
    following two characteristics:
      (1) a < b < c
          (a) three uniquely distinct positive integers
      (2) a^2 + b^2 = c^2
          (a) For the lowest 2 numbers in the set, the squares of each of
          those numbers will add up to the square of the laregest number
          in the set.

- Expected Input(s)
  - Number of Expected Parameters: 1
  - Names of Expected Parameters: "sumOfPythagTriplet"
  - Data Types of Expected Parameters: Number

- Expected Output(s)
  - Number of Expected Outputs: 1
  - Names of Expected Output: "productOfPythagTriplet"
  - Data Type of Expected Output: Number

- Constraints
  - What will make the algorithm fail?
    - Negative numbers?
      - Yes
    - Number data types?
      - No
    - Floating point numbers?
      - Yes
    - Non-alphanumeric characters in the inputs?
      - Yes

- Example #1
  - Example #1 Input: 12
    - a^2 + b^2 = c^2
    - 9 + 16 = 625
    - 3^2 + 4^2 = 5^2
    - 3 + 4 + 5 = 12 
  - Example #1 Output: 60 (3 * 4 * 5 = 60)
    - a = 3
    - b = 4
    - c = 5
*/

/*---------------DEVISING A PLAN---------------
- BRUTE FORCE SOLUTION (Pseudocoded Steps)
  (1) Import the "assert" module for testing purposes.
  (2) Declare the '("use strict")' statement to enable strict mode.
  (3) Create a function, "findProductOfPythagTriplet()" that takes in 1 
      parameter, "sumOfPythagTriplet", and returns 1 output, 
      "productOfPythagTriplet".
  (4) Using the 'let' keyword, initialize a variable called
      "productOfPythagTriplet". This variable will store the product of
      all the numbers in a Pythagorean Triplet when the sum of those same
      numbers is equal the "sumOfPythagTriplet".
  (5) Using the 'let' keyword, initialize two more variables, "numA" & 
      "numB". These variables will store the values of the first two 
      numbers from an incomplete Pythagorean Triplet. 
  (6) Using a 'for' loop, iterate through the "numA" variable while it is
      less than the "sumOfPythagTriplet".
      (a) Using a nested 'for' loop, iterate through the "numB" variable
          while the sum of "numA" and "numB" is less than 
          "sumOfPythagTriplet". 
          (i)   Inside of the nested 'for' loop, using the 'let' keyword,
                declare two new variables, "squareOfNumA" & 
                "squareOfNumB", and set each of them equal to their 
                original values raised to the power of 2.
          (ii)  Inside of the nested 'for' loop, using the 'let' keyword 
                again, declare a new variable, "numC", and set it equal
                to the square root of the sum total of "squareOfNumA" and
                "squareOfNumB".
          (iii) Create a conditional 'if' statement that will only run 
                the following block of code if '"numA" is NOT equal to 
                "numB"' AND if 'numA' plus 'numB' plus 'numC' is equal to
                "sumOfPythagTriplet"'.
                (1)   Set the value of "productOfPythagTriplet" equal to
                      the product of "numA", "numB", & "numC".
                (2)   Return "productOfPythagTriplet".
  (7) Return a string that says "A Pythagorean Triplet for the provided 
      input does NOT exist!". 
*/

/*------------IMPLEMENTING THE PLAN------------*/
const assert = require('assert');

('use strict');

function findProductOfPythagTriplet(sumOfPythagTriplet) {
	if (
		sumOfPythagTriplet === null ||
		sumOfPythagTriplet === undefined ||
		sumOfPythagTriplet < 1 ||
		typeof sumOfPythagTriplet !== 'number'
	) {
		return false;
	} else {
		let productOfPythagTriplet = 0;

		for (let numA = 1; numA < sumOfPythagTriplet; numA++) {
			for (let numB = numA + 1; numA + numB < sumOfPythagTriplet; numB++) {
				let squareOfNumA = numA ** 2;

				let squareOfNumB = numB ** 2;

				let numC = Math.sqrt(squareOfNumA + squareOfNumB);

				if (numA !== numB && numA + numB + numC === sumOfPythagTriplet) {
					productOfPythagTriplet = numA * numB * numC;
					return productOfPythagTriplet;
				}
			}
		}
	}
	return 'A Pythagorean Triplet for the provided input does NOT exist!';
}

const hugeNum = BigInt(
	98245098204580297420948509238450289450298345092832303849300
);
const floatNum = 0.1283949124934;

// TEST CASES for BRUTE FORCE SOLUTION
const sumOfTriplet12 = findProductOfPythagTriplet(12); // should return 60
const sumOfTriplet1000 = findProductOfPythagTriplet(1000); // should return 31875000
const sumOfTripletNoInput = findProductOfPythagTriplet(); // should return false
const sumOfTripletNegativeNum = findProductOfPythagTriplet(-12); // should return false
const sumOfTripletStringType = findProductOfPythagTriplet('12'); // should return false
const sumOfTripletBooleanType = findProductOfPythagTriplet('12'); // should return false
const sumOfTripletBigIntType = findProductOfPythagTriplet(hugeNum); // should return false
const sumOfTripletFloatNum = findProductOfPythagTriplet(floatNum); // should return false

// TESTS for BRUTE FORCE SOLUTION
assert.deepStrictEqual(
	sumOfTriplet12,
	60,
	'When the sum of the numbers in a Pythagorean Triplet is 12, the product of those numbers is 60.'
);
assert.deepStrictEqual(
	sumOfTriplet1000,
	31875000,
	'When the sum of the numbers in a Pythagorean Triplet is 1000, the product of those numbers is 31875000.'
);
assert.deepStrictEqual(
	sumOfTripletNoInput,
	false,
	"When the input is either 'null' or 'undefined', the 'false' Boolean is returned."
);
assert.deepStrictEqual(
	sumOfTripletNegativeNum,
	false,
	"When the input is a negative number, the 'false' Boolean is returned."
);
assert.deepStrictEqual(
	sumOfTripletStringType,
	false,
	"When the input has a data type of 'String', the 'false' Boolean is returned."
);
assert.deepStrictEqual(
	sumOfTripletBooleanType,
	false,
	"When the input has a data type of 'Boolean', the 'false' Boolean is returned."
);
assert.deepStrictEqual(
	sumOfTripletBigIntType,
	false,
	"When the input has a data type of 'big int', the 'false' Boolean is returned."
);
assert.deepStrictEqual(
	sumOfTripletFloatNum,
	false,
	"When the input is a floating point number, the 'false' Boolean is returned."
);

console.log(
	"\n*---- ALL TESTS FOR 'findProductOfPythagTriplet()' ARE PASSING ----*\n"
);

/*--------REFLECTING/ITERATING THE PLAN--------
- BRUTE FORCE SOLUTION ANALYSIS
  - Were you able to arrive at the correct answer with your solution?
    - Yes. findProductOfPythagTriplet(1000) = 31875000.
  - Analyze the Time & Space Complexity of your solution.
    - Time Complexity: O(n^2) = quadratic time
    - Space Complexity: O(1) = constant
  - Could either, Time or Space Complexity, be improved in your solution?
    - Yes. Time Complexity could be improved from O(n^2) to O(n).
  - If so, how would you go about improving it?
    - Instead of using two nested 'for' loops, I would create a Stack()
      data structure to temporarily store "numA" values and use one 'for'
      loop and one 'while' loop.
    - Create a new variable called "numAStack" that is set equal to a
      pair of empty square brackets (JavaScript does not have native 
      Stack() data structures so we have to build our own).
    - Create a "numB" variable & set it equal to the value of 2 (because
      according to the instructions, "numB" will always be greater than
      "numA").
    - Using the 'for' loop, iterate through all the numbers between 1 
      and the value of "sumOfPythagTriplet" (inclusive) in descending
      order and:
      - Add each iterated number to the "numAstack" stack using the 
        '.push()' method.
    - Using the 'while' loop, continue looping through the "numAStack"
      stack as long as it has a length greater than 0.
      - Use the '.pop()' method to remove the last item from the stack
        and store this value as a new variable called "poppedNumA" that 
        we will be evaluating during each iteration of the 'while' loop.
      - Create a new variable called "numC" and set it equal to the
        square root value of the sum of "numA"-squared plus 
        "numB"-squared.
      - If "numA" does NOT equal "numB" AND if the sum of "numA", "numB",
        and "numC" DOES equal the "sumOfPythagTriplet", then return 
        "numC".
      - Else, do nothing.
  - What is the new Time & Space Complexity of your improved solution?
    - Time Complexity: O(n) = linear time
    - Space Complexity: O(n) = linear space
*/
