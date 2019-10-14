/*---------------UNDERSTANDING THE PROBLEM---------------
- Expected Inputs:
  - 1 input
    - type: number
      - positive, whole numbers only
      - cannot be a float
      - can be named 'n'
    - this number, n, represents an upper-limit that an individual value 
      in the 'fib_array' variable can have.

- Expected Outputs:
  - Only 1 output
    - type: number
      - can be named "evenSum"
    - this number represents the sum of all the even numbers from the 'fib_array' variable that are less than 'n'.

- Any Contstraints?
  - The first and second values in the 'fib_array' variable are 1 & 2,
    respectively.

- Examples:
  - Input #1: 10
    - fib_array = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    - even_nums_fib_array = [2, 8, 34]
  - Output #1: 44
    - even_nums_fib_array = [2, 8, 34]
    - evenSum = 2 + 8 + 34 = 44 
    - evenSum = 44

  - Input #2: 20
    - fib_array = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
                 144, 233, 377, 610, 987, 1597, 2584, 4181, 6755, 10946]
    - even_nums_fib_array = [2, 8, 34, 144, 610, 2584, 10946]
  - Output #2: 14328
    - even_nums_fib_array = [2, 8, 34, 144, 610, 2584, 10946]
    - evenSum = 2 + 8 + 34 + 144 + 610 + 2584 + 10946
    - evenSum = 14328
*/

/*---------------DEVISING A PLAN---------------
- BRUTE FORCE SOLUTION:
  - Strategy:
    - Create a variable 'i' that allows you to use a 'while loop'.
    - Use a 'while' loop to iterate as many times necessary until
      a pre-calculated value, 'even_nums_fib_array[i]' is greater than
      or equal to 'n'.
    - Following complete execution of the 'while' loop, we will create
      a 'for' loop to iterate through the 'fib_array' to evaluate for even values that are ALSO below 'n'.
    - While inside the 'for' loop, evaluate each item in the 'fib_array'.
      If the item IS below 'n' AND is also an even number, we will add it to a running sum total counter variable called 'evenSum', which is initialized with the value 0.

  - Pseudocode:

  - Runtime Complexity: O()
  - Space Complexity: O()
*/

//---------------IMPLEMENTING A PLAN---------------

/*---------------REFLECTING/ITERATING---------------
- Brute Force Solution Runtime Complexity: O()
- Brute Force Solution Space Complexity: O()

- Can I make my brute force solution FASTER?

- How much faster & space-efficient will your new solution be?

- How will you do it?
*/
