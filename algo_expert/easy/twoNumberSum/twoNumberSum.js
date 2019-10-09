/* 
Expected Inputs:
- 2 inputs
  - (1) type: array
    - non-empty
    - contains DISTINCT integer
  - (2) type: integer
    - represents a target sum

Expected Outputs:
- 1 output
  - type: array
    - contains one of the following:
      - (a) two integers, from the input array, IF those two integers sum
            up to the second provided input (target sum integer)
      - (b) no contents (empty), IF no two integers from teh input array
            sum up to the second provided input (target sum integer)

Any Constraints?
  - Can the integers be negative?
    -Yes
  - Integers: whole numbers only; no fractions
*/

/*
Example Inputs:
  - Input #1a: [1, 2, 3, 4, 5]
  - Input #1b: 8

  - Input #2a: [2, 4, 6, 8, 10]
  - Input #2b: 15

  - Input #3a: [-1, 1, 3, 5, 7]
  - Input #3b: 4

  - Input #4a: [-8, 22, 4, -5, 3]
  - Input #4b: 17

Example Output: 
  - Output #1: [3, 5]

  - Output #2: []

  - Output #3: [-1, 5]

  - Output #4: [-5, 22]
*/
