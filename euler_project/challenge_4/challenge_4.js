/* ----------UNDERSTANDING THE PROBLEM----------
-What is a 'palindromic number'?
  -An integer that reads the same both ways (forwards & backwards).

-Expected Input(s): 
  -Number of Expected Inputs: 1
    -"numDigits" = the number of digits in each integer that are 
      multiplied together to get a product.

-Expected Output(s):
  -Number of Expected Outputs: 1
    -"largestPalindrome" = largest palindrome made from the product of two
      3-digit numbers.

-Any Constraints:
  -Can the numbers be floating point numbers?
    -No.
  -Can the numbers be negative?
    -No.

-Example Input: 2
-Example Output: 9009 (91 * 99 = 9009)
*/

/* ---------------DEVISING A PLAN--------------- 
-BRUTE FORCE SOLUTION
  (1) Create a function, 'checkPalindrome', that takes in a number, 'num'
      & returns 'True' if the number is a palindrome, or 'False' if the
      number is NOT a palindrome.
  (2) Create a another function, 'findLargestPalindrome', that takes in
      one input, 'numDigits', & returns one output, 'largestPalindrome'.
  (3) Create a variable, 'largestPalindrome', with a 'let' keyword that
      will store the current largest palindromic number as in integer.
    (4) Use 2 nested 'for' loops to iterate through every possible 
        product made from 2 integers that contain 'numDigits' number of 
        digits in each integer.
        (a) Create a 'product' variable with the 'let' keyword to store 
            the current product of the two numbers.
        (b) For each iteration, determine whether or not 'product' is a
            'palindromic number'.
            (i)     If the length of 'product' is equal to 0, return a
                    string that says "Please provide a valid input of 
                    type integer".
            (ii)    If the length of 'product' is equal to 1, set the
                    'largestPalindrome' variable equal to this product.
            (iii)   Else (If the length of 'product' is greater than 1),
                    call the 'checkPalindrome()' function and pass in the
                    'product' as the input. 
                  (1) If 'True', set the value of 'largestPalindrome' 
                      equal to the value of 'product'.
                  (2) If 'False', do nothing.
    (5) Return 'largestPalindrome'.
*/

/* IMPLEMENTING THE PLAN */
const assert = require("assert");
("use strict");

function checkPalindrome(num) {
  if (num == undefined || num == null) {
    // console.log("\nNo valid input provided");
    return false;
  }

  let numString = Math.abs(num).toString();
  // console.log("numString =", numString);
  let lenNumString = numString.length;
  // console.log("\nlenNumString =", lenNumString);

  if (lenNumString === 1) {
    // console.log(
    //   `\nOne digit in '${num}';\nTherefore, '${num}' is palindromic!`
    // );
    return true;
  } else if (lenNumString > 1 || lenNumString < 1) {
    // console.log(`\n${lenNumString} digits in ${num}; so let's explore!`);
    let leftPointer = 0;
    let rightPointer = lenNumString - 1;

    while (leftPointer < rightPointer) {
      if (numString[leftPointer] === numString[rightPointer]) {
        leftPointer += 1;
        rightPointer -= 1;
      } else {
        // console.log(`Whoops! '${num}'; is NOT palindromic!`);
        return false;
      }
    }
    // console.log(`YAHOO! '${num}'; is palindromic!`);
    return true;
  }
}

console.log("*-----* ALL TESTS HAVE PASSED! *-----*");
assert.deepEqual(checkPalindrome(), false, "No input was provided");
assert.deepEqual(checkPalindrome(0), true, "0 is palindromic");
assert.deepEqual(checkPalindrome(1), true, "1 is palindromic");
assert.deepEqual(checkPalindrome(2), true, "2 is palindromic");
assert.deepEqual(checkPalindrome(23), false, "23 is NOT palindromic");
assert.deepEqual(checkPalindrome(120), false, "120 is NOT palindromic");
assert.deepEqual(checkPalindrome(121), true, "121 is palindromic");
assert.deepEqual(checkPalindrome(9283), false, "9283 is NOT palindromic");
assert.deepEqual(checkPalindrome(92829), true, "92829 is palindromic");
assert.deepEqual(checkPalindrome(-9), true, "-9 is palindromic");

// console.log(checkPalindrome(0));
// console.log(checkPalindrome(1));
// console.log(checkPalindrome(2));
// console.log(checkPalindrome(23));
// console.log(checkPalindrome(120));
// console.log(checkPalindrome(121));
// console.log(checkPalindrome(9283));

/* REFLECTING/ITERATING THE PLAN */
