/*---------- UNDERSTANDING THE PROBLEM ----------
- Objective:  Determine the 13 ADJACENT digits in the provided 1000-digit
              number that would have the greatest product and return that
              value.

- Expected Inputs:
  - Number of Expected Inputs: 
    - 2
  - Name/Type of Expected Inputs:
    - 'longNumString' => number
    - 'numOfAdjacentDigits' => number

- Expected Outputs:
  - Number of Expected Outputs:
    - 1
  - Name/Type of Expected Outputs:
    - 'greatestAdjacentDigitsProduct' => number

- Any Constraints?
  - Can 'longNumString' be a floating point number?
    - For this problem, assume that it must be an integer.
  - Can 'longNumString' be a negative number?
    - For this problem, assume that it must be positive.
  - Can 'greatestAdjacentDigitsProduct' be negative?
    - For this problem, assume that it must be positive.

- Example:
  - Example Inputs: 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450, 4

  - Example Output: 5832 (9 x 9 x 8 x 9 = 5832)

*/

/*--------------- DEVISING A PLAN ---------------
- BRUTE FORCE SOLUTION:
  (1) Create a function, 'findGreatestAdjacentDigitsProduct()', that will
      take in two parameters, 'longNumString' & 'numOfAdjacentDigits',
      and will return one output, 'greatestAdjacentDigitsProduct'.
  (2) Create a variable, 'greatestAdjacentDigitsProduct', using the 
      'const' keyword, which will be set to 0, but will eventually hold
      the value of the to-be-returned output.
  (3) Convert the 'longNumString' number into a string and set it equal
      to a new variable using the 'const' keyword, 'longNumStringStr'.
  (4) Using a 'for' loop, iterate through each number in 
      'longNumStringStr'.
      (a) Create a variable, 'chunkedNumsProduct', using the 'let'
          keyword, and set it equal to 1. This variable will store 
          the the product of the numbers that are iterated through
          in the INNER 'for' loop that correlate to the current 
          iteration of the OUTER 'for' loop.
      (b) Using a nested 'for' loop, consecutively iterate through a 
          'numOfAdjacentDigits' number of values in 'longNumStringStr', 
          (beginning with the zeroith index) to calculate the product
          of the numbers that are iterated through. 
      (c) If the value of 'chunkedNumsProduct' is GREATER than
          the value of 'greatestAdjacentDigitsProduct', set 
          'greatestAdjacentDigitsProduct' equal to 
          'chunkedNumsProduct'.
      (d) If the value of 'chunkedNumsProduct' is NOT GREATER
          than the value of 'greatestAdjacentDigitsProduct',
          don't do anything.
  (5) Return 'greatestAdjacentDigitsProduct'.
*/

/*------------ IMPLEMENTING THE PLAN ------------*/

const assert = require("assert");

("use strict");

function findGreatestAdjacentDigitsProduct(longNumString, numOfAdjacentDigits) {
  if (
    typeof longNumString !== "string" ||
    typeof numOfAdjacentDigits !== "number"
  ) {
    console.log(
      "Please provide two valid inputs (a 'string' & a 'number', respectively)."
    );
    return undefined;
  } else if (BigInt(longNumString) < 0 || numOfAdjacentDigits < 0) {
    console.log(
      "Please provide two valid inputs (positive integers greater than 0)."
    );
    return undefined;
  } else {
    let greatestAdjacentDigitsProduct = 0;

    for (let i = 0; i <= longNumString.length - numOfAdjacentDigits; i++) {
      // console.log("\ni = ", i);
      let chunkedNums = [];
      let chunkedNumsProduct = 1;
      // console.log("chunkedNumsProduct(starting) = ", chunkedNumsProduct);

      for (let j = 0; j < numOfAdjacentDigits; j++) {
        // console.log("\nj = ", j);

        chunkedNums.push(longNumString[i + j]);
        // console.log("chunkedNums = ", chunkedNums);

        chunkedNumsProduct *= longNumString[i + j];
        // console.log("***NEW*** chunkedNumsProduct = ", chunkedNumsProduct);
      }

      if (chunkedNumsProduct > greatestAdjacentDigitsProduct) {
        // console.log(
        //   "We found a greater product! Update 'greatestAdjacentDigitsProduct'"
        // );
        greatestAdjacentDigitsProduct = chunkedNumsProduct;
        // console.log(
        //   "greatestAdjacentDigitsProduct = ",
        //   greatestAdjacentDigitsProduct
        // );
        // } else {
        //   console.log("No update is required.");
      }
      chunkedNumsProduct = 1;
    }
    return greatestAdjacentDigitsProduct;
  }
}

const hugeNum =
  "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450";

console.log(findGreatestAdjacentDigitsProduct(undefined, undefined)); // should be undefined
console.log(findGreatestAdjacentDigitsProduct(undefined, 2)); // should be undefined
console.log(findGreatestAdjacentDigitsProduct("123456", undefined)); // should be undefined
console.log(findGreatestAdjacentDigitsProduct(null, null)); // should be undefined
console.log(findGreatestAdjacentDigitsProduct(null, 2)); // should be undefined
console.log(findGreatestAdjacentDigitsProduct("123456", null)); // should be undefined
console.log(findGreatestAdjacentDigitsProduct("-123456", 2)); // should be undefined
console.log(findGreatestAdjacentDigitsProduct("123456", -2)); // should be undefined
console.log(findGreatestAdjacentDigitsProduct("123456", 2)); // should be 30
console.log(findGreatestAdjacentDigitsProduct("123456789", 3)); // should be 504
console.log(findGreatestAdjacentDigitsProduct(hugeNum, 4)); // should be 5832

/*------------ REFLECTING/ITERATING -------------*/
