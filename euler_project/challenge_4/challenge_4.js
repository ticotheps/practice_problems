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
    -Maybe?

-Example Input: 2
-Example Output: 9009 (91 * 99 = 9009)
*/

/* ---------------DEVISING A PLAN--------------- 
-BRUTE FORCE SOLUTION
  (1) Create a function, 'checkPalindrome', that takes in a number, 'num'
      & returns 'True' if the number is a palindrome, or 'False' if the
      number is NOT a palindrome.
  (2) Create another function, 'findLargestPalindrome', that takes in
      one input, 'numDigits', & returns one output, 'largestPalindrome'.
  (3) Create a variable, 'largestPalindrome', with a 'let' keyword that
      will store the current largest palindromic number as in integer.
  (4) Create 2 new variables, 'minRange' and 'maxRange', that will
      define the boundaries for the nested 'for' loops.
    (4) Use 2 nested 'for' loops to iterate through every possible 
        product made from 2 integers that contain 'numDigits' number of 
        digits in each integer.
        (a) Create a 'product' variable with the 'let' keyword to store 
            the current product of the two numbers.
        (b) For each iteration, determine whether or not 'product' is a
            'palindromic number'.
        (c) If 'product' is a palindromic number AND it is greater than
            the current 'largestPalindrome', set 'largestPalindrome'
            equal to the 'product'.
    (5) Return 'largestPalindrome'.
*/

/* IMPLEMENTING THE PLAN */
const assert = require("assert");
("use strict");

function checkPalindrome(num) {
  if (num == undefined || num == null) {
    return false;
  }

  let numString = Math.abs(num).toString();
  let lenNumString = numString.length;

  if (lenNumString === 1) {
    return true;
  } else if (lenNumString > 1 || lenNumString < 1) {
    let leftPointer = 0;
    let rightPointer = lenNumString - 1;

    while (leftPointer < rightPointer) {
      if (numString[leftPointer] === numString[rightPointer]) {
        leftPointer += 1;
        rightPointer -= 1;
      } else {
        return false;
      }
    }
    return true;
  }
}

console.log("*-----* ALL TESTS FOR 'checkPalindrome()' PASSED! *-----*");
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

// Time Complexity: O(n^2) = quadratic
// Space Complexity: O(1) = constant
function findLargestPalindrome(numDigits) {
  let largestPalindrome = 0;
  let minRange = 10 ** (numDigits - 1);
  let maxRange = 10 ** numDigits;

  for (let i = minRange; i < maxRange; i++) {
    for (let j = minRange; j < maxRange; j++) {
      let product = i * j;
      if (checkPalindrome(product) === true && product > largestPalindrome) {
        largestPalindrome = product;
      }
    }
  }
  return largestPalindrome;
}

console.log("*-----* ALL TESTS FOR 'findLargestPalindrome()' PASSED! *-----*");
assert.deepEqual(
  findLargestPalindrome(1),
  9,
  "9 is the largest palindromic product of two 1-digit numbers"
);
assert.deepEqual(
  findLargestPalindrome(2),
  9009,
  "9009 is the largest palindromic product of two 2-digit numbers"
);
assert.deepEqual(
  findLargestPalindrome(3),
  906609,
  "906609 is the largest palindromic product of two 3-digit numbers"
);

console.log(findLargestPalindrome(3));

/* REFLECTING/ITERATING THE PLAN 
- Can you improve the time/space complexity of your BRUTE FORCE SOLUTION?
  - I don't believe so. I believe the nested 'for' loops are required to 
    access to both variables, 'i' and 'j', for the purpose of getting
    their product.
*/
