/*----------UNDERSTANDING THE PROBLEM---------- 
- Expected Input(s):
  - Number of Inputs Expected: 1
  - Type: Array
  - Name/Value: 'arr'

- Expected Output(s):
  - Number of Outputs Expected: 1
    - Number of POSSIBLE choices for outputs: 2
  - Type: String
  - Name(s)/Value(s): 'YES' or 'NO'

- Constraints:
  - Can values of 'arr' be negative?
    - According to the example provided, 'arr' will only contain positive
      integers.
  - 1 <= 'arr[i]' (values within the array) <= 1,000,000,000
  - 1 <= 'n' (number of items in the array) <= 100,000 

- Examples:

*/

/*----------DEVISING A PLAN---------- 
(1) Nested 'For' Loop Approach (BRUTE FORCE SOLUTION)
  - Runtime Complexity: O(n^2) = quadratic
  - Space Complexity: O(1) = constant
(2) Single 'For' Loop Approach + Caching (IMPROVED SOLUTION)
  - Runtime Complexity: O(n) = linear
  - Space Complexity: O(n) = linear
*/

/*----------IMPLEMENTING THE PLAN----------*/

const findNumber = (arr, k) => {
  for (let i = 0; i < arr.length; i++) {
    // console.log(`\n*i = ${i}*`);
    if (arr[i] == k) {
      return 'YES';
    }
  }
  return 'NO';
};

console.log(findNumber([1, 2, 3, 4, 5], 4)); // Should return 'YES'
console.log(findNumber([1, 2, 3, 4, 5], 6)); // Should return 'NO'
console.log(findNumber([5, 3, 1, 2, 4], 4)); // Should return 'YES'
console.log(findNumber([5, 3, 1, 2, 4], 6)); // Should return 'NO'
console.log(findNumber([120, 2214, 3212, 44, 521], 44)); // Should return 'NO'

/*----------REFLECTING/ITERATING ON THE PLAN---------- 
- BRUTE FORCE SOLUTION ANALYSIS
  - Runtime Complexity: O(n) = linear
  - Space Complexity: O(1) = constant

  - Can RC or SC be improved at all?
    - No
*/
