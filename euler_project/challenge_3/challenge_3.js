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
console.time('findLargestPFimproved');
const findLargestPFimproved = n => {
  const primeNums = {};
  let primeFactors = [];

  for (let i = 2; i <= n; i++) {
    // console.log('i = ', i);
    let factorCount = 0;
    for (let j = 1; j <= i; j++) {
      if (factorCount <= 2) {
        if (i % j == 0) {
          factorCount++;
        }
        // console.log(`factorCount = ${factorCount}`);
      }
    }
    if (factorCount <= 2) {
      primeNums[i] = true;
    }
  }
  console.log(primeNums);

  for (let k = n; k > 0; k--) {
    if (n % k == 0) {
      if (primeNums[k] == true) {
        // console.log(`Prime factor at ${k}!`);
        primeFactors.push(k);
      }
    }
  }
  console.log(primeFactors);
  const largestPrimeFactor = primeFactors[0];
  return largestPrimeFactor;
};

// console.log(`\nfindLargestPFbrute(3): ${findLargestPFbrute(3)}`); // should be 3
console.log(`findLargestPFimproved(3): ${findLargestPFimproved(3)}`); // should be 3

// console.log(`\nfindLargestPFbrute(11): ${findLargestPFbrute(11)}`); // should be 11
console.log(`findLargestPFimproved(11): ${findLargestPFimproved(11)}`); // should be 11

// console.log(`\nfindLargestPFbrute(20): ${findLargestPFbrute(20)}`); // should be 5
console.log(`findLargestPFimproved(20): ${findLargestPFimproved(20)}`); // should be 5

// console.log(`\nfindLargestPFbrute(1000): ${findLargestPFbrute(1000)}`); // should be 5
// console.log(`findLargestPFimproved(1000): ${findLargestPFimproved(1000)}`); // should be 5

// console.log(`\nfindLargestPFbrute(13195): ${findLargestPFbrute(13195)}`); // should be 29
// console.log(`findLargestPFimproved(13195): ${findLargestPFimproved(13195)}`); // should be 29

// console.log(
//   `\nfindLargestPFbrute(600851475143): ${findLargestPFbrute(600851475143)}`
// );
// console.log(
//   `findLargestPFimproved(600851475143): ${findLargestPFimproved(600851475143)}`
// );

//---------TESTING-------------

// console.log(`findLargestPFimproved(600851): ${findLargestPFimproved(600851)}`);
// console.log(
//   `findLargestPFimproved(6008514): ${findLargestPFimproved(6008514)}`
// );
// console.log(
//   `findLargestPFimproved(60085147): ${findLargestPFimproved(60085147)}`
// );
// console.log(
//   `findLargestPFimproved(600851475): ${findLargestPFimproved(600851475)}`
// );
// console.log(
//   `findLargestPFimproved(6008514751): ${findLargestPFimproved(6008514751)}`
// );
// console.log(
//   `findLargestPFimproved(60085147514): ${findLargestPFimproved(60085147514)}`
// );
// console.log(
//   `findLargestPFimproved(600851475143): ${findLargestPFimproved(600851475143)}`
// );

console.timeEnd('findLargestPFimproved');

/*----------REFLECTING/ITERATING----------
- BRUTE FORCE SOLUTION ANALYSIS:
  - Runtime Complexity: O(3n) => O(n) = linear; ***# of "for" loops: 4
  - Space Complexity: O(n) = linear

  - Can you improve the RC or SC?
    - Yes.

  - How?
    - Continue using "for" loops + a cache, but only use 3 "for" loops
  
  - Run Time Results?
    - findLargestPFbrute(3): 0.087ms
    - findLargestPFimproved(3): 0.005ms
  
  - Success!
 */
