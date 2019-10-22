/*----------UNDERSTANDING THE PROBLEM----------
- What is an 'anagram'?
  - A coupling of two strings that contain the exact same letters, in
    the exact same frequencies, which allows for the first string's
    letters to be rearranged to form the second string and vice versa.

- Expected Input(s):
  - Number of Inputs: 2
  - Types (respectively): String, String
  - Names/Values (respectively): 'a', 'b'

- Expected Output(s):
  - Number of Outputs: 1
  - Type: Number (integer)
  - Name/Value: 'numOfDeletions'

- Constraints:
  - Any number of characters can be deleted from each string.
  - Characters can only be deleted from either side of the string.
  - The variable 'numOfDeletions' can't be negative or a floating number.

- Examples:
  - Inputs #1: 'cde', 'abc'
  - Inputs #2: 4 (# of deletions required for both strings to reach 'c')

 */

/*----------DEVISING A PLAN----------
- BRUTE FORCE SOLUTION:
  (1) Create a function called 'makeAnagram()' that will take in two
      parameters (string, string) and return a single output (number).

  (2) Create a variable 'lenOfA' and store a number that denotes the
      length of string 'a'.

  (3) Create a variable 'lenOfB' and store a number that denotes the
      length of string 'b'.

  (4) Create a variable 'numOfDeletions' and set the value equal to 0 to
      denote the total number deletions required to make string 'a' and
      string 'b' anagrams of each other.

  (5) Create a variable 'cacheOfA', which will be an object that stores
      characters (from string 'a') as the 'keys' and then integers 
      (representing the occuring frequency of that particular letter) as
      the 'values' to those keys, in the 'cacheOfA' object.
  
  (6) Create a variable 'cacheOfB', which will be an object that stores
      characters (from string 'b') as the 'keys' and then integers 
      (representing the occuring frequency of that particular letter) as
      the 'values' to those keys, in the 'cacheOfB' object.

  (7) Use a 'for' loop to iterate through the characters of string 'a' to
      determine a specific character's frequency of occurrence within
      string 'a'.
      (a) If the character being evaluated does not already exist in the
          associated cache, then add it as a new property, with a value
          of 1.
      (b) If the character being evaluated DOES ALREADY exist in the
          associated cache, then simply increment the value by 1.

  (8) Use another 'for' loop to iterate through the characters of string
      'b' to determine a specific character's frequency of occurrence 
      within string 'b'.
      (a) If the character being evaluated does not already exist in the
          associated cache, then add it as a new property, with a value
          of 1.
      (b) If the character being evaluated DOES ALREADY exist in the
          associated cache, then simply increment the value by 1.

  (9) Use a 'for' loop to iterate through the 'keyOfA' of 'cacheOfA'.

  (10)  Create a variable 'commonChars' and set it equal to 
        an empty array to hold characters that occur in both strings.
  
  (11)  Nest another 'for' loop inside of the previous 'for' loop to
        iterate through the 'keyOfB' of 'cacheOfB' to determine if
        there are any common characters between strings 'a' and 'b'. 
        (a) If 'keyOfA == keyOfB', then do the following evaluation...
            (i) If 'cacheOfA[keyOfA] == cacheOfB[keyOfB]', add 'keyOfA' 
                to the 'commonChars' array with the '.push()' 
                array method.
            (ii)  If 'cacheOfA[keyOfA] != cacheOfB[keyOfB]', find the
                  difference, 'let diff', between these values, and add
                  'diff' to the 'numOfDeletions' variable.
        (b) If 'keyOfA != keyOfB', then do the following evaluation...
  
  (12)  

      

 */

/*----------IMPLEMENTING THE PLAN----------*/

const makeAnagram = (a, b) => {
  const lenOfA = a.length;
  const lenOfB = b.length;
  let numOfDeletions = 0;
  const cacheOfA = {};
  const cacheOfB = {};
  const commonChars = [];

  for (let i = 0; i < lenOfA; i++) {
    if (a[i] in cacheOfA) {
      cacheOfA[a[i]] += 1;
    } else {
      cacheOfA[a[i]] = 1;
    }
  }

  for (let j = 0; j < lenOfB; j++) {
    if (b[j] in cacheOfB) {
      cacheOfB[b[j]] += 1;
    } else {
      cacheOfB[b[j]] = 1;
    }
  }

  for (keyOfA in cacheOfA) {
    for (keyOfB in cacheOfB) {
      if (keyOfA == keyOfB) {
        commonChars.push(keyOfA);
      }
    }
  }

  const deletionsInA = lenOfA - commonChars.length;
  const deletionsInB = lenOfB - commonChars.length;
  numOfDeletions = deletionsInA + deletionsInB;
  return numOfDeletions;
};

console.log(makeAnagram('cde', 'abc')); // should return 4
console.log(makeAnagram('cde', 'cde')); // should return 0
console.log(makeAnagram('thepsourinthone', 'sour')); // should return 11
console.log(makeAnagram('allred', 'red')); // should return 3

/*----------REFLECTING/ITERATING ON THE PLAN----------
- IMPROVED SOLUTION:

(1) Create a function called 'makeAnagram()' that will take in two
    parameters (string, string) and return a single output (number).

(2) Create a variable 'lengthOfA' to denote the length of string 'a'.

(3) Create a variable 'lengthOfB' to denote the length of string 'b'.

(4) Create a variable 'lengthOfA' to denote the length of string 'a'.
 */
