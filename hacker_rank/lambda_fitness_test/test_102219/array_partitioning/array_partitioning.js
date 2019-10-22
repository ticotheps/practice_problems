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
 */

/*----------DEVISING A PLAN----------
- BRUTE FORCE SOLUTION:

 */

/*----------IMPLEMENTING THE PLAN----------*/

/*----------REFLECTING/ITERATING ON THE PLAN----------

 */
