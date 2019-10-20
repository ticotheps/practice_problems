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

(3) Initialize an empty cache of prime numbers called 'primeNumbers' to 
    allow for easy & fast lookups with JavaScript's hash table.

(4) Use a 'for' loop to add ALL prime numbers, as keys, to the 
    'primeNumbers' object (with a value of 'false' for each key), 
    beginning with 2 all the way up to n.

(5) Use a separate 'for' loop to iterate through the 'primeNumbers'
    object to evaluate for any keys in the 'primeNumbers' object that
    evaluates to true for this statement: "n % key === 0". 

    (6) If "n % key === 0" evaluates to true, then set 'largestPFactor' 
        equal to the value of key.
      
    (7) If "n % key === 0" evaluates to false, then do nothing.

(8) Return 'largestPFactor'.
*/

/*----------IMPLEMENTING THE PLAN----------*/

const findLargestPFactor = n => {
  let largestPFactor = n;
  // console.log(largestPFactor);

  let primeNumbers = {};
  // console.log(primeNumbers);

  for (let i = 2; i < n; i++) {
    if (n % i != 0) {
      console.log(i);
    }
  }

  return largestPFactor;
};

console.log(findLargestPFactor(3));
// console.log(findLargestPFactor(9));
// console.log(findLargestPFactor(13));
// console.log(findLargestPFactor(29));

/*----------REFLECTING/ITERATING----------
 */
