/*---------------UNDERSTANDING THE PROBLEM---------------
Expected Inputs:
  - Only 1 input
    - type: number 
      - can be named 'n'

Expected Outputs:
  - Only 1 output
    - type: number
      - can be named 'sum'
        - this number represents the sum of all the natural numbers below
          the given input, 'n', that are ALSO multiples of 3 or 5.

Constraints:
  - Define a "natural number".
    - (a) a positive, whole number
    - (b) zero is not a positive whole number (not a "natural number")

Examples:
  - Input #1: 10
    - All natural numbers under 10: 1, 2, 3, 4, 5, 6, 7, 8, 9.
    - All natural numbers under 10 that are ALSO multiples 
      of 3 or 5: 3, 5, 6, 9.
  - Output #1: 23
    - The sum of all natural numbers under 10 that are multiples 
      of 3 or 5 (3 + 5 + 6 + 9 = 23)

  - Input #2: 20
    - All natural numbers under 20: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                                    12, 13, 14, 15, 16, 17, 18, 19.
    - All natural numbers under 2o that are ALSO multiples
      of 3 or 5: 3, 5, 6, 9, 10, 12, 15, 18.
  - Output #2: 78 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 = 78)

  - Input #3: 50
    - All natural numbers under 50: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                                  11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                  21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                                  31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                                  41, 42, 43, 44, 45, 46, 47, 48, 49.
    - All natural numbers under 50 that are ALSO multiples
      of 3 or 5: 3, 5, 6, 9, 10, // sum => 33
                12, 15, 18, 20, // sum => 65
                21, 24, 25, 27, 30, // sum => 127
                33, 35, 36, 39, 40, // sum => 183
                42, 45, 48 // sum => 135
  - Output #2: 543 (33 + 65 + 127 + 183 + 135 = 543)
*/

/*---------------DEVISING A PLAN---------------

*/

//---------------IMPLEMENTING THE PLAN---------------

/*---------------REFLECTING/ITERATING---------------

*/
