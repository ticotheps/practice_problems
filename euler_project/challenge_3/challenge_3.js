/*----------UNDERSTANDING THE PROBLEM----------
- Expected Input(s): 
  - Only ONE expected input.
  - Type: number.
  - Can be named 'n' to represent a given number, in which you'd like to
    find the largest prime factor of.

- Expected Output(s):
  - Only ONE expected output.
  - Type: number.
  - Can be named 'largestPrimeFactor' to represent the largest prime
    factor for the given input, n.

- Constraints:
  - Define a 'prime factor'?
    - Prime Number: a number that is only divisible by 1 and itself.
      - "1" is NOT a prime number.
      - i.e. - 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31

  - What is 'prime factorization'?
    - Prime Factorization: breaking apart a number down to its lowest
      prime factors.
      - i.e.
                75
               /  \
              3    25
                  /  \
              3  5    5 => 3 x 5 x 5 = 75
  - Can it be a negative number? 
    - No.
  - Can it be a floating number?
    - No. 
*/

/*----------DEVISING A PLAN----------
OVERALL PLAN:
(1) Find all factors of 'n' first.
(2) Search within that list of factors for prime numbers.
(3) Add those prime numbers to a new array in ascending order.
(4) Return the LAST item in the array to ensure the Largest Prime Factor.

(1) Create function that takes in a given input, n, which is a positive
    integer.

(2) Create a variable, largestPFactor, that is set equal to 0. This
    number will represent the current largest prime factor while the
    second 'for' loop is evaluating all of the items in the cache. This
    variable will be returned at the end of the function.

(3) Initialize an empty cache of all of n's factors called 'factorsOfN' to 
    allow for easy & fast lookups later with JavaScript's hash table.

(4) Use a 'for' loop to iterate from "1" to n and add any numbers that n
    can be divided by evenly, as keys to the 'factorsOfN' object (with 
    a value of 'false' for each key).

(5) Use a separate 'for' loop to iterate through the 'factorsOfN'
    object to evaluate for any keys that are prime numbers. 

    (6) If "key in factorsOfN" is a prime number, then set the key's
        value equal to 'true' and replace the value of 'largestPFactor'
        with this key's value.
      
    (7) If "key in factorsOfN" is NOT a prime number, then don't do 
        anything.

(8) Return 'largestPFactor'.
*/

/*----------IMPLEMENTING THE PLAN----------*/
//--------------BRUTE FORCE SOLUTION-------------
// console.time('findLargestPFbrute');
// const findLargestPFbrute = n => {
//   let primeFactorsOfN = {};
//   const primeFactorsArr = [];
//   let largestPrimeFactor = 0;

//   for (let i = n; i > 1; i--) {
//     primeFactorsOfN[i] = true;
//   }

//   for (key in primeFactorsOfN) {
//     for (let j = 2; j <= key; j++) {
//       if (key != j && key % j == 0) {
//         // console.log(`${key} is divisible by ${j}!`);
//         primeFactorsOfN[key] = false;
//       }
//     }
//     if (primeFactorsOfN[key] == true) {
//       primeFactorsArr.unshift(key);
//     }
//   }

//   for (let k = 0; k < primeFactorsArr.length; k++) {
//     if (
//       n % primeFactorsArr[k] == 0 &&
//       primeFactorsArr[k] >= largestPrimeFactor
//     ) {
//       // console.log(`${primeFactorsArr[k]} is a prime factor of ${n}!`);
//       largestPrimeFactor = primeFactorsArr[k];
//     }
//   }

//   // console.log(primeFactorsOfN);
//   // console.log(primeFactorsArr);
//   return largestPrimeFactor;
// };
// console.timeEnd('findLargestPFbrute');

//--------------IMPROVED SOLUTION-------------
console.time('findLargestPFbest');

const findLargestPFbest = n => {
  var divisor = 2; // smallest prime number that is not 1
  var nRemaining = n;

  while (nRemaining > 1) {
    // console.log('\nnRemaining =', nRemaining);
    // console.log('divisor = ', divisor);

    if (nRemaining % divisor == 0) {
      nRemaining /= divisor;
    } else {
      divisor++;
    }
    // console.log('nRemaining =', nRemaining, '\n');
  }
  return divisor;
};

// console.log(`findLargestPFbest(12): ${findLargestPFbest(12)}`); // should be 3

// console.log(`findLargestPFbest(20): ${findLargestPFbest(20)}`); // should be 5

// console.log(`findLargestPFbest(1000): ${findLargestPFbest(1000)}`); // should be 5

// console.log(`findLargestPFbest(13195): ${findLargestPFbest(13195)}`); // should be 29

console.log(
  `findLargestPFbest(600851475143) = ${findLargestPFbest(600851475143)}`
); // should be 6857

console.timeEnd('findLargestPFbest');

/*----------REFLECTING/ITERATING----------
- BRUTE FORCE SOLUTION ANALYSIS:
  - Runtime Complexity: O(3n) => O(n) = linear; *** # of "for" loops: 4
  - Space Complexity: O(n) = linear

  - Can you improve the RC or SC?
    - Yes. Both, RC and SC, can be improved.

  - How?
    - Using a single "while" loop with some global variables instead of 
      3 "for" loops like a dum-dum.
  
  - Run Time Results?
    - findLargestPFbest(600851475143): 7.042ms
  
  - New Runtime Complexity: O(n) => linear
  
  - New Space Complexity: O(1) => constant

  - Success!

  - What did you learn from this solution?
    - That I like to overcomplicate things. 
 */
