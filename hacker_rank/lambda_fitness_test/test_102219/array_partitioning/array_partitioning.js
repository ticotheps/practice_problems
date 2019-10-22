/*----------UNDERSTANDING THE PROBLEM----------
- Expected Input(s):
  - Number of Inputs: 2
  - Types (respectively): Number (an integer), Array
  - Names/Values (respectively): 'k', 'numbers'

- Expected Output(s):
  - Number of Outputs: 1 (with 2 possibilities)
  - Type: String
  - Names/Values (respectively): 'Yes', 'No'

- Constraints:
  - Each element in the array occurs in EXACTLY one subsequence.
    - This means that the elements within a subsequence are UNIQUE.
  - All the numbers in a subsequence are distinct.
  - Elements in the array having the same value must be in different
    subsequences.
  - ^All of these statements are essentially saying the same thing.
  - 1 <= n <= 100,000 (n = the length of the given array)
  - 1 <= k <= n (k = the number of items required in the subsequence)
  - 1 <= numbers[i] <= 100,000 (the value of an item in the array)

- Examples:
  - Sample Input #1: 2, [3, 5, 3, 2]
  - Sample Output #1: Yes
  - Explanation #1:
    - The array is [3, 5, 3, 2]. One solution is to partition into 2
      subsequences - [3, 2] and [5, 3]. So the answer is 'Yes'.

  - Sample Input #2: 3, [4, 8, 8, 8, 6, 4]
  - Sample Output #2: No
  - Explanation #2:
    - Element 8 occurs thrice in the array. There is no possible way to
      partition into subsequences of length 3, such that 8 occurs at most
      once in each subsequence. So the answer is 'No'.

  - Sample Input #3: 2, [1, 1, 1, 3, 4, 5]
  - Sample Output #3: No
  - Explanation #2:
    - Element 1 occurs thrice in the array. There is no possible way to
      partition into subsequences of length 3, such that 1 occurs at most
      once in each subsequence. So the answer is 'No'.
 */

/*----------DEVISING A PLAN----------
- BRUTE FORCE SOLUTION:

  1.  Create a function, 'partitionArray()', that takes in 2 parameters,
      'k' (an integer) and 'numbers' (an array), and returns either the
      string 'Yes' or the string 'No' based on whether or not the given
      'numbers' array can be partitioned into subsequences where the
      length of each subsequence is equal to 'k' and each item in the
      subsequent subsequences is a distinctly unique integer.

  2.  Create a variable with 'let' called 'lenOfNums', which denotes the
      length of the given input array, 'numbers'.

  3.  Create a variable with 'const' called 'cache', which denotes the
      frequency of each occuring item in the given input array.   

  4.  Use an 'if/else' statement to evaluate whether or not 'lenOfArr' 
      can be partitioned evenly into subsequences with a length of 'k'.

      a.  If 'lenOfArr' can be partitioned evenly into subsequences with
          a length of 'k', use a 'for' loop and a cache to determine the
          frequency of each item in the given array, storing the item
          itself as a 'key' and the number of occurrences as the 'value' 
          of a key/value pair in the cache.

      b.  If 'lenOfArr' CANNOT be partitioned evenly into subsequence
          with a length of 'k', do nothing.
  
  5.  Use a separate 'for' loop that will iterate through the keys of the
      cache object to determine if any associated values are > 1.

      a.  If a key's value IS greater than 1, do the following:

          i.  Evaluate whether or not the multiple occurrences of the
              key in quesion are AT LEAST 'k' indices apart in the
              given array.

                1.  If the occurrence in question ARE at least 'k' 
                    indices apart in the original given input array,
                    return 'Yes'.

                2.  If the occurrence in question is NOT at least 'k'
                    indices apart in the original given input array,
                    return 'No'.

      b.  If a key's value is NOT greater than 1, do nothing.

  6.  Return 'No'.
 */

/*----------IMPLEMENTING THE PLAN----------*/

const partitionArray = (k, numbers) => {
  let lenOfNums = numbers.length;
  const cache = {};

  if (lenOfNums % k == 0) {
    for (let i = 0; i < lenOfNums; i++) {
      // console.log(`i = ${i}; numbers[${i}] = ${numbers[i]}`);
      if (cache[numbers[i]]) {
        console.log(`${numbers[i]} ALREADY existed in the cache!`);
        cache[numbers[i]] += 1;
        console.log(cache);
      } else {
        console.log(`${numbers[i]} was just added to the cache!`);
        cache[numbers[i]] = 1;
        console.log(cache);
      }
    }

    for (key in cache) {
      if (cache[key] > 1) {
        for (let j = 0; j < lenOfNums; j++) {
          if (key == numbers[j] && key == numbers[k - 1]) {
            console.log(
              `The key, ${key}, has duplicates within the same subsquence!`
            );
            return 'No';
          } else {
            console.log(
              `The key, ${key}, DOES NOT have any duplicates within the same subsquence!`
            );
            return 'Yes';
          }
        }

        console.log(numbers);
      } else if (cache[key] == 1) {
        console.log(
          `The key, ${key}, is a DISTINCT integer in the given array!`
        );
      }
      console.log(cache);
      return 'Yes';
    }
  }
  console.log(cache);
  return 'No';
};

console.log(partitionArray(2, [1, 1, 3, 4, 5, 6])); // should return 'Yes'
// console.log(partitionArray(3, [4, 8, 8, 8, 6, 4])); // should return 'No'
// console.log(partitionArray(2, [1, 2, 3, 1, 4, 1])); // should return 'Yes'

/*----------REFLECTING/ITERATING ON THE PLAN----------

 */
