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
(1) Nested 'For' Loop Approach
  - Runtime Complexity: O(n^2) = quadratic
  - Space Complexity: O(1)
(2) Single 'For' Loop Approach + Caching
  - Runtime Complexity: O(n) = linear
  - Space Complexity: O(n) = linear
*/

/*----------IMPLEMENTING THE PLAN----------*/

const findNumber = (arr, k) => {
  for (let i = 0; i < arr.length; i++) {
    // console.log(`\n*i = ${i}*`);
    for (let j = 0; j < arr.length; j++) {
      // console.log(`j = ${j}`);
      if (i != j && arr[i] == k) {
        return 'YES';
      }
    }
  }
  return 'NO';
};

console.log(findNumber([1, 2, 3, 4, 5], 1)); // Should return 'YES'
console.log(findNumber([1, 2, 3, 4, 5], 6)); // Should return 'NO'
console.log(findNumber([5, 3, 1, 2, 4], 1)); // Should return 'YES'
console.log(findNumber([5, 3, 1, 2, 4], 6)); // Should return 'NO'
console.log(findNumber([120, 2214, 3212, 44, 521], 432)); // Should return 'NO'

/*----------REFLECT/ITERATE ON THE PLAN---------- 

*/

// const findNumber = (arr, k) => {
//   let cache = {};
//   let kInCache = 'NO';

//   for (let i = 0; i < arr.length; i++) {
//     console.log(arr[i]);

//     if (arr[i] in cache) {
//       kInCache = 'YES';
//     } else {
//       cache[arr[i]] = true;
//     }
//     console.log(cache);
//   }

//   return kInCache;
// };
