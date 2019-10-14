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
  - Pseudocode:
    - Create a variable 'fib_nums_arr' and set it equal to an array where
      1 & 2 are the first two values in the array, respectively. This
      array will hold all of the fibonacci numbers that are produced.
    - Create another variable 'even_fib_nums_arr' and set it equal to an
      array with only ONE value, 2, inside of it. This array will contain
      only the EVEN numbers from the 'fib_nums_arr'. 
    - Using a 'for' loop, we will loop through the following block of
      code 100 times to generate the next 100 values of the Fibonacci
      sequence.
    - While still inside the 'for' loop, we will add each calculated
      value for 'next_num' to the 'fib_nums_arr'.
    - While still inside the 'for' loop, if that value for 'next_num' is
      even AND it is less than the value of our parameter, 'n', we will
      also add that same value to the 'even_fib_nums_arr'.
    - Then, once the 'for' loop has completed executing, we will perform
      a '.reduce()' function on the 'even_fib_nums_arr' and set the
      resulting value equal a new variable called 'even_nums_sum'.
    - Lastly, we will return the 'even_nums_sum' value.

  - Runtime Complexity: O(2n) => O(n); linear runtime
  - Space Complexity: O(2) => O(1); constant space
*/

//---------------IMPLEMENTING A PLAN---------------

const fib_sum_even_nums = n => {
  const fib_nums_arr = [1, 2];
  const even_fib_nums_arr = [2];

  for (let i = 2; i < 33; i++) {
    let next_num = fib_nums_arr[i - 1] + fib_nums_arr[i - 2];
    fib_nums_arr.push(next_num);

    if (next_num < n && next_num % 2 == 0) {
      even_fib_nums_arr.push(next_num);
    }
  }

  console.log(`----------ALL FIBONACCI NUMBERS----------`);
  fib_nums_arr.map(number => {
    console.log(number);
  });
  console.log(`----------ALL FIBONACCI NUMBERS----------\n`);

  console.log(`\n----***EVEN FIBONACCI NUMBERS ONLY***----`);
  even_fib_nums_arr.map(number => {
    console.log(number);
  });
  console.log(`----***EVEN FIBONACCI NUMBERS ONLY***----\n`);

  const even_nums_sum = even_fib_nums_arr.reduce((sum, number) => {
    return sum + number;
  }, 0);

  return even_nums_sum;
};

console.log(
  `Total sum of all EVEN Fibonnaci Numbers that are also LESS THAN 4,000,000: ${fib_sum_even_nums(
    4000000
  )}`
);

/*---------------REFLECTING/ITERATING---------------
- Brute Force Solution Runtime Complexity: O()
- Brute Force Solution Space Complexity: O()

- Can I make my brute force solution FASTER?

- How much faster & space-efficient will your new solution be?

- How will you do it?
*/
