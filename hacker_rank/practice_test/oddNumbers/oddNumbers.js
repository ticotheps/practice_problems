/*----------UNDERSTANDING THE PROBLEM----------
- Expected input(s):
  - Number of inputs: 2
  - Types (respectively): Number, number
  - Names/values (respectively): 'l', 'r'

- Expected output(s):
  - Number of outputs: 1
  - Type: Array
  - Names/value: 'oddNumsArr'

- Constraints:
  - 'l' and 'r' must be 'integers', which means they will be whole 
    numbers.
    - 'Floats' are not allowed.
  - Can 'l' and 'r' be negative?
    - There is no information that says they cannot be negative.
    - So, YES, 'l' and 'r' can be negative.

- Examples:
  - Inputs #1: 1, 10
  - Outputs #1: [1, 3, 5, 7, 9]

  - Inputs #2: 1, 10
  - Outputs #1: [1, 3, 5, 7, 9]

  - Inputs #3: -10, 10
  - Outputs #1: [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9]
*/

/*----------DEVISING A PLAN----------
  - Pseudocode:
    (1) Create a function called 'oddNumbers()'.
    (2) Create a variable called 'oddNumsArr' and set it equal to an empty 
      array.
    (3) Use a 'for' loop to iterate through a range of numbers where 'l' is
      the inclusive starting index and 'r' is the inclusive ending index.
      (a) If the iterator, i, is odd (i % 2 != 0), then add it to the 
        'oddNumsArr' using the '.push()' array method.
      (b) If the iterator, i, is even (i % 2 == 0), don't do anything.
    (4) After the 'for' loop completes execution, return 'oddNumsArr'.
*/

/*----------IMPLEMENTING THE PLAN----------*/

const oddNumbers = (l, r) => {
  const oddNumsArr = [];

  for (let i = l; i <= r; i++) {
    if (i % 2 != 0) {
      // console.log(`${i} is an odd number!`);
      oddNumsArr.push(i);
    }
  }

  return oddNumsArr;
};

console.log(oddNumbers(1, 10)); // Should be [1, 3, 5, 7, 9]
console.log(oddNumbers(-10, 10)); // Should be [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9]

/*----------REFLECTING/ITERATING ON THE PLAN----------
- BRUTE FORCE SOLUTION
  - Runtime Complexity: O(n) = linear
  - Space Complexity: O(1) = constant

  - Can you improve the RC or the SP?
    - No
*/
