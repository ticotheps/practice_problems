/**
 * Write a recursive algorithm for the Fibonacci sequence
 *
 * Fibonacci Sequence
 * fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21]
 *
 * Each number is the sum of the previous two numbers.
 *
 * Write a program that prints out the nth Fibonacci number.
 *
 * The user can enter any value for 'n'.
 *
 * Constraints:
 *  - Will we always have a valid input? Yes.
 *    - Input will always be between 0 and 10^15
 *  - What is the expected output?
 *    - Just a single number on a line.
 *  - How performant is it?
 *    - Delivers the 1000000th (millionth) number in < 1 second.
 */

function findNthFibNum(nIndex) {
  console.log(`nIndex = ${nIndex}`);
  const firstFibNum = 0;
  const secondFibNum = 1;

  const cache = {}; // memoization
  console.log(`cache = ${cache}`);

  if (nIndex === firstFibNum || nIndex === secondFibNum) {
    return nIndex;
  }
  if (cache[nIndex] === false) {
    cache[nIndex] = findNthFibNum(nIndex - 1) + findNthFibNum(nIndex - 2);
  }
  return cache;
}

console.log(findNthFibNum(0));
console.log(findNthFibNum(1));
console.log(findNthFibNum(10));
