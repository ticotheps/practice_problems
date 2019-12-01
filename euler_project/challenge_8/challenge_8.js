/*---------- UNDERSTANDING THE PROBLEM ----------
- Objective:  Determine the 13 ADJACENT digits in the provided 1000-digit
              number that would have the greatest product and return that
              value.

- Expected Inputs:
  - Number of Expected Inputs: 
    - 2
  - Name/Type of Expected Inputs:
    - 'longNumSeries' => number
    - 'numOfAdjacentDigits' => number

- Expected Outputs:
  - Number of Expected Outputs:
    - 1
  - Name/Type of Expected Outputs:
    - 'greatestAdjacentDigitsProduct' => number

- Any Constraints?
  - Can 'longNumSeries' be a floating point number?
    - For this problem, assume that it must be an integer.
  - Can 'longNumSeries' be a negative number?
    - For this problem, assume that it must be positive.
  - Can 'greatestAdjacentDigitsProduct' be negative?
    - For this problem, assume that it must be positive.

- Example:
  - Example Inputs: 
    [
      73167176531330624919225119674426574742355349194934
      96983520312774506326239578318016984801869478851843
      85861560789112949495459501737958331952853208805511
      12540698747158523863050715693290963295227443043557
      66896648950445244523161731856403098711121722383113
      62229893423380308135336276614282806444486645238749
      30358907296290491560440772390713810515859307960866
      70172427121883998797908792274921901699720888093776
      65727333001053367881220235421809751254540594752243
      52584907711670556013604839586446706324415722155397
      53697817977846174064955149290862569321978468622482
      83972241375657056057490261407972968652414535100474
      82166370484403199890008895243450658541227588666881
      16427171479924442928230863465674813919123162824586
      17866458359124566529476545682848912883142607690042
      24219022671055626321111109370544217506941658960408
      07198403850962455444362981230987879927244284909188
      84580156166097919133875499200524063689912560717606
      05886116467109405077541002256983155200055935729725
      71636269561882670428252483600823257530420752963450
    ], 4

  - Example Output: 5832 (9 x 9 x 8 x 9 = 5832)

*/

/*--------------- DEVISING A PLAN ---------------
- BRUTE FORCE SOLUTION:
  (1) Create a function, 'findGreatestAdjacentDigitsProduct()', that will take in
      two parameters, 'longNumSeries' & 'numOfAdjacentDigits', and will
      return one output, 'greatestAdjacentDigitsProduct'.
  (2) Create a variable, 'greatestAdjacentDigitsProduct', using the 'const' 
      keyword, which will hold the value of the to-be-returned output.
  (3) Create another variable, 'adjacentDigitsArray', using the 'const'
      keyword, which will hold the to-be-evaluated adjacent digits.
  (4) Convert the 'longNumSeries' number into an array and set it equal
      to a new variable using the 'const' keyword, 'longNumSeriesArray'.
  (5) Using a 'for' loop, iterate through 'longNumSeriesArray' in chunks
      of digits, by specifying the size of the chunk as the 
      'numOfAdjacentDigits' input.
      (6) Create a new variable, 'digitChunksArray', with the 'let'
          keyword, that will store the the first 'n' numbers values 
          (equal to the second parameter) from 'longNumSeriesArray'.
      (7) Using another 'for' loop, iterate through all the number
          values in 'digitChunksArray' to find the product of those
          numbers.
          (a) Create a variable, 'chunksArrayProduct', using the 'let'
              keyword, to store the current value of the calculated
              product for that iteration.
              (i)   If the value of 'chunksArrayProduct' is GREATER than
                    the value of 'greatestAdjacentDigitsProduct', set 
                    'greatestAdjacentDigitsProduct' equal to 
                    'chunksArrayProduct'.
              (ii)  If the value of 'chunksArrayProduct' is NOT GREATER
                    than the value of 'greatestAdjacentDigitsProduct',
                    don't do anything.
  (8) Return 'greatestAdjacentDigitsProduct'.
*/

/*------------ IMPLEMENTING THE PLAN ------------*/

/*------------ REFLECTING/ITERATING -------------*/
