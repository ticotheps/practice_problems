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
(1) Create function that takes in a given input, n, which is a positive
    integer.

(2) Create a variable, largestPFactor, that is set equal to n. This
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

const findLargestPFactor = n => {
  let largestPFactor = n;
  // console.log(largestPFactor);

  let primeNumbers = {};
  // console.log(primeNumbers);

  for (let i = 2; i <= n; i++) {
    // if (i % 2 != 0) {
    //   if (i % 3 != 0) {
    //     // console.log(`Added ${i} to the cache`);
    //     primeNumbers[i] = false;
    //     console.log(`Just set primeNumbers[${i}] = ${primeNumbers[i]}`);
    //   }
    // }
    console.log(i);
  }

  // return largestPFactor;
};

// console.log(findLargestPFactor(3));
console.log(findLargestPFactor(9));
// console.log(findLargestPFactor(10));
// console.log(findLargestPFactor(29));

/*----------REFLECTING/ITERATING----------
 */
