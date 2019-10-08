// Task 1: Write a function, 'times10', that takes an argument, 'n', and multiplies 'n' by 10.
// (This will be a simple multiplication function)
const times10 = n => {
  let product = n * 10;
  return product;
};

console.log('~~~~~~~~~~~~~~TASK 1~~~~~~~~~~~~~~');
console.log('times10 returns:', times10(9));

// Task 2: Use an object to cache the results of your 'times10' function.
// *Protip 1*: Create a function that checks if the value for n has been
//             calculated before.
// *Protip 2*: If the value for 'n' has not been calculated, calculate
//             it and then save that result inside the cache object.

// const cache = {};

// const memoTimes10 = n => {};

// console.log('~~~~~~~~~~~~~~TASK 2~~~~~~~~~~~~~~');
// console.log('Task 2 calculated value:', memoTimes10(9)); // calculated
// console.log('Task 2 cached value:', memoTimes10(9)); // cached
