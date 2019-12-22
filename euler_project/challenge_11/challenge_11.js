/*----------UNDERSTANDING THE PROBLEM----------
- Objective 
  - Create an algorithm that will return the LARGEST product of four adjacent
    numbers in any provided matrix.

- Definitions
  - "adjacent" = The 4 numbers can be next to each other in any of the following directions:
    - up
    - down
    - left
    - right
    - diagonally-up (left to right)
    - diagonally-down (left to right)
    - i.e. - 26, 63, 78, 14 (which are all in a diagonally-downwars row)
      
- Expected Input(s)
  - Number of Expected Parameters: 1
  - Names/Data Types of Expected Parameters
    (1) "matrix" => Array of sub-arrays made up of 2-digit numbers

- Expected Output(s)
  - Number of Expected Output(s): 1
  - Names/Data Types of Expected Output(s)
    (1) "largestProduct" => Number

- Constraints
  - What will make the algorithm fail?
    - Can the numbers in the matrix be negative?
      - No.
    - Can the numbers in the matrix be floating point numbers?
      - No.
    - Can the items in the sub-arrays of the matrix be strings?
      - No.
    - Do the numbers in the sub-arrays of the matrix need to be 2-digit numbers?
      - No..

- Example #1
  - Example #1 Input(s): (my_matrix)
  - Example #1 Output(s): 1,788,696 (= 26x63x78x14)
*/

/*---------------DEVISING A PLAN---------------
- BRUTE FORCE SOLUTION (Pseudocoded Steps) 
  (1) Create a 'const' variable, "my_matrix", that will hold the array of 
  sub-arrays (of numbers) to be passedninto the function as a matrix.

  (2) Create a function, "findLargestProductInMatrix()", that will take in 1
  parameter, "matrix", and will return one output, "largestProduct".

  (3) Inside the "findLargestProductInMatrix()" function, create a 'let'
  variable, "largestProduct", that will contain the largest product of 4
  consecutive numbers within the matrix, in any given direction (i.e. - left,
  right, up, down, diagonally (up-right, down-right).

  (4) Create a helper function, "productOf4Nums()", that will take in one
  input, "numsArray", and calculate the product of all those numbers in that
  array.

  (5) Inside the "findLargestProductInMatrix()" function, create 4 sets of
  nested 'for' loops that will iterate through the 'outer' & 'inner' array of 
  the matrix that is passed into the "findLargestProductInMatrix()" function.

  (6) The nested 'for' loops, will check for the largest product in the
  following directions: horizontal (left + right), vertical (up + down),
  diagonally-up (left to right), and diagonally-down (left to right).

  (7) Inside each nested 'for' loop, create 4 'const' variables,
  "horizontalNumsArray", "verticalNumsArray", "diagonalDownRightNumsArray", and
  "diagonalUpRightNumsArray",that will contain an array of 4 numbers from each
  iteration of the inner 'for' loop.

  (8) Also, inside each of the nested 'for' loops, create 4 'let' variables with
  each of these prefixes, "horizontal__________", "vertical__________",
  "diagonalDownRight__________", & "diagonalUpRight__________":
  "__________FirstNum", "__________SecondNum", "__________ThirdNum", and 
  "__________FourthNum", that will contain numbers according to the pattern
  specific to that nested 'for' loop. 

  (9) For each iteration of the inner 'for' loop of each set of nested 'for'
  loops, push the values of those 4 'let' variables into the corresponding
  "__________NumsArray" variable.

  (10) Call the helper function, "productOf4Nums()", while passing in the
  "__________NumsArray" variable and set it equal to a new corresponding 
  "__________Product" variable that will be compared to the 
  "largestProduct" value. 
    (a) If the value of the product is GREATER than the value of 
    "largestProduct", set "largestProduct" equal to that product.

  (11) Return "largestProduct".
*/

/*------------IMPLEMENTING THE PLAN------------*/

const assert = require('assert');

('use strict');

function productOf4Nums(numsArray) {
  const product = (numsArray.reduce(function(total, num) {
    return total *= num;
  }, 1));

  return product;
};

// console.log(productOf4Nums([1, 2, 3, 4]));

const my_matrix = [
  [08, 02, 22, 97, 38, 15, 00, 40, 00, 75, 04, 05, 07, 78, 52, 12, 50, 77, 91, 08],
  [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 04, 56, 62, 00],
  [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 03, 49, 13, 36, 65],
  [52, 70, 95, 23, 04, 60, 11, 42, 69, 24, 68, 56, 01, 32, 56, 71, 37, 02, 36, 91],
  [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
  [24, 47, 32, 60, 99, 03, 45, 02, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
  [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
  [67, 26, 20, 68, 02, 62, 12, 20, 95, 63, 94, 39, 63, 08, 40, 91, 66, 49, 94, 21],
  [24, 55, 58, 05, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
  [21, 36, 23, 09, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95],
  [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 03, 80, 04, 62, 16, 14, 09, 53, 56, 92],
  [16, 39, 05, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57],
  [86, 56, 00, 48, 35, 71, 89, 07, 05, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
  [19, 80, 81, 68, 05, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 04, 89, 55, 40],
  [04, 52, 08, 83, 97, 35, 99, 16, 07, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
  [88, 36, 68, 87, 57, 62, 20, 72, 03, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
  [04, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 08, 46, 29, 32, 40, 62, 76, 36],
  [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 04, 36, 16],
  [20, 73, 35, 29, 78, 31, 90, 01, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 05, 54],
  [01, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52 ,01, 89, 19, 67, 48]
]

console.time('findLargestProductInMatrix');
function findLargestProductInMatrix(matrix) {
  let largestProduct = 0;

  for (let i = 0; i < my_matrix.length; i++) {
    // console.log(`\nSub-Array #${i + 1}:`);
    for (let j = 0; j <= my_matrix[i].length - 4; j++) {
      const horizontalNumsArray = [];
      // console.log(`Item #${j + 1} in Sub-Array #${i + 1} = ${my_matrix[i][j]}`);
      let horizontalFirstNum = my_matrix[i][j];
      let horizontalSecondNum = my_matrix[i][j + 1];
      let horizontalThirdNum = my_matrix[i][j + 2];
      let horizontalFourthNum = my_matrix[i][j + 3];

      horizontalNumsArray.push(horizontalFirstNum, horizontalSecondNum, horizontalThirdNum, horizontalFourthNum);
      // console.log("horizontalNumsArray = ", horizontalNumsArray);

      let horizontalProduct = productOf4Nums(horizontalNumsArray);
      if (horizontalProduct > largestProduct) {
        largestProduct = horizontalProduct;
      };

      // console.log('\nfirstNum = ', horizontalFirstNum);
      // console.log('horizontalSecondNum = ', horizontalSecondNum);
      // console.log('horizontalThirdNum = ', horizontalThirdNum);
      // console.log('horizontalFourthNum = ', horizontalFourthNum);
    }
  }

  for (let m = 0; m <= my_matrix.length - 4; m++) {
    // console.log(`\nSub-Array #${m + 1}:`);
    for (let n = 0; n < my_matrix[m].length; n++) {
      const verticalNumsArray = [];
      // console.log(`Item #${n + 1} in Sub-Array #${m + 1} = ${my_matrix[m][n]}`);
      let verticalFirstNum = my_matrix[m][n];
      let verticalSecondNum = my_matrix[m + 1][n];
      let verticalThirdNum = my_matrix[m + 2][n];
      let verticalFourthNum = my_matrix[m + 3][n];

      verticalNumsArray.push(verticalFirstNum, verticalSecondNum, verticalThirdNum, verticalFourthNum);
      // console.log("verticalNumsArray = ", verticalNumsArray);

      let verticalProduct = productOf4Nums(verticalNumsArray);
      if (verticalProduct > largestProduct) {
        largestProduct = verticalProduct;
      };

      // console.log('\nverticalFirstNum = ', verticalFirstNum);
      // console.log('verticalSecondNum = ', verticalSecondNum);
      // console.log('verticalThirdNum = ', verticalThirdNum);
      // console.log('verticalFourthNum = ', verticalFourthNum);
    }
  }

  for (let q = 0; q <= my_matrix.length - 4; q++) {
    // console.log(`\nSub-Array #${q + 1}:`);
    for (let r = 0; r <= my_matrix[q].length - 4; r++) {
      const diagonalDownRightNumsArray = [];
      // console.log(`Item #${r + 1} in Sub-Array #${q + 1} = ${my_matrix[q][r]}`);
      let diagonalDownRightFirstNum = my_matrix[q][r];
      let diagonalDownRightSecondNum = my_matrix[q + 1][r + 1];
      let diagonalDownRightThirdNum = my_matrix[q + 2][r + 2];
      let diagonalDownRightFourthNum = my_matrix[q + 3][r + 3];

      diagonalDownRightNumsArray.push(diagonalDownRightFirstNum, diagonalDownRightSecondNum, diagonalDownRightThirdNum, diagonalDownRightFourthNum);
      // console.log("diagonalDownRightNumsArray = ", diagonalDownRightNumsArray);

      let diagonalDownRightProduct = productOf4Nums(diagonalDownRightNumsArray);
      if (diagonalDownRightProduct > largestProduct) {
        largestProduct = diagonalDownRightProduct;
      };

      // console.log('\ndiagonalDownRightFirstNum = ', diagonalDownRightFirstNum);
      // console.log('diagonalDownRightSecondNum = ', diagonalDownRightSecondNum);
      // console.log('diagonalDownRightThirdNum = ', diagonalDownRightThirdNum);
      // console.log('diagonalDownRightFourthNum = ', diagonalDownRightFourthNum);
    }
  }

  for (let s = 0; s <= my_matrix.length - 4; s++) {
    // console.log(`\nSub-Array #${s + 1}:`);
    for (let t = 0; t <= my_matrix[t].length - 4; t++) {
      const diagonalUpRightNumsArray = [];
      // console.log(`Item #${t + 1} in Sub-Array #${s + 1} = ${my_matrix[s][t]}`);
      let diagonalUpRightFirstNum = my_matrix[s][t + 3];
      let diagonalUpRightSecondNum = my_matrix[s + 1][t + 2];
      let diagonalUpRightThirdNum = my_matrix[s + 2][t + 1];
      let diagonalUpRightFourthNum = my_matrix[s + 3][t];

      diagonalUpRightNumsArray.push(diagonalUpRightFirstNum, diagonalUpRightSecondNum, diagonalUpRightThirdNum, diagonalUpRightFourthNum);
      // console.log("diagonalUpRightNumsArray = ", diagonalUpRightNumsArray);

      let diagonalUpRightProduct = productOf4Nums(diagonalUpRightNumsArray);
      if (diagonalUpRightProduct > largestProduct) {
        largestProduct = diagonalUpRightProduct;
      };

      // console.log('\ndiagonalUpRightFirstNum = ', diagonalUpRightFirstNum);
      // console.log('diagonalUpRightSecondNum = ', diagonalUpRightSecondNum);
      // console.log('diagonalUpRightThirdNum = ', diagonalUpRightThirdNum);
      // console.log('diagonalUpRightFourthNum = ', diagonalUpRightFourthNum);
    }
  }
  return largestProduct;
}

// console.log(findLargestProductInMatrix(my_matrix));

assert.deepStrictEqual(findLargestProductInMatrix(my_matrix), 70600674, "The largest product of 4 consecutive numbers in my_matrix is 70600674")

console.log("***** ALL TESTS FOR 'findLargestProductInMatrix()' PASS *****");
console.timeEnd('findLargestProductInMatrix');


/*--------REFLECTING/ITERATING THE PLAN--------
- BRUTE FORCE SOLUTION ANALYSIS
  - Were you able to arrive at the correct answer with your solution?
    - Yes.
  - Analyze the Time & Space Complexity of your solution.
    - Time Complexity: O(4n^2) => O(n^2) => quadratic
    - Space Complexity: O(1) => constant
  - Could either, Time or Space Complexity, be improved in your solution?
    - Yes
  - If so, how would you go about improving it?
    - Use 5 independent 'for' loops (no nesting) & a single cache object
    to store arrays of 4 numbers to later be evaluated with another 'for' loop.
  - What is the new Time & Space Complexity of your improved solution?
    - Time Complexity: O(5n + 1) => O(n) => linear
    - Space Complexity: O(n) => linear
*/
