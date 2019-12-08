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
const assert = require("assert");

("use strict");

function findProductOfPythagTriplet(sumOfPythagTriplet) {
  let productOfPythagTriplet;
  let numA;
  let numB;

  for (let numA = 1; numA < sumOfPythagTriplet; numA++) {
    // console.log("\n*OUTER LOOP*");

    for (let numB = numA + 1; numA + numB < sumOfPythagTriplet; numB++) {
      // console.log("inner loop");
      let squareOfNumA = numA ** 2;
      // console.log("squareOfNumA = ", squareOfNumA);
      let squareOfNumB = numB ** 2;
      // console.log("squareOfNumB = ", squareOfNumB, "\n");

      let numC = Math.sqrt(squareOfNumA + squareOfNumB);
      // console.log("numC = ", numC, "\n");

      if (numA !== numB && numA + numB + numC === sumOfPythagTriplet) {
        // console.log(
        //   `We found a triplet! numA = ${numA}, numB = ${numB}, numC = ${numC}`
        // );
        productOfPythagTriplet = numA * numB * numC;
        return productOfPythagTriplet;
      }
    }
  }
  return "A Pythagorean Triplet for the provided input does NOT exist!";
}

assert.deepStrictEqual(
  findProductOfPythagTriplet(12),
  60,
  "When the sum of the three numbers in a Pythagorean Triplet is 12, the product of those three numbers is 60."
);

console.log(
  "\n*---- ALL TESTS FOR 'findProductOfPythagTriplet()' ARE PASSING ----*\n"
);

/*--------REFLECTING/ITERATING THE PLAN--------*/