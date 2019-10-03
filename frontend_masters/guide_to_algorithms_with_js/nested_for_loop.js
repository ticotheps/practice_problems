/* 
Expected Input: 
  - an array of numbers
Expected Output:  
  - if the array contains NO duplicate numbers, return true
  - if the array contains duplicate numbers, return false
Constraints:
  - integers = whole numbers
  - integers can be negative
*/
// Runtime Complexity = O(n^2)
// Space Complexity = O(1)
const isUnique = arr => {
  let uniqueIntegers = true;

  for (let i = 0; i < arr.length; i++) {
    console.log(`\n**************************************************`);
    console.log(
      `OUTER LOOP (i === ${i})           Iteration #: ${i + 1} of ${arr.length}`
    );
    console.log(`**************************************************`);

    for (let j = 0; j < arr.length; j++) {
      console.log(
        `~~~ INNER LOOP (j === ${j})   Iteration #: ${j + 1} of ${
          arr.length
        } ~~~\n`
      );
      if (i === j) {
        console.log(`~~~ No comparison made because i === j; no need to`);
        console.log(`~~~ compare an item from the array to itself.`);
        console.log(`--------------------------------------------------`);
      } else {
        console.log(
          `~~~ Comparison #${j + 1}: Are (${arr[i]}) & (${
            arr[j]
          }) duplicate ints?`
        );
        if (arr[i] === arr[j]) {
          console.log(`~~~~~~ YES! A duplicate has been found.`);
          console.log(`--------------------------------------------------`);
          uniqueIntegers = false;
          return uniqueIntegers;
        } else {
          console.log(`~~~~~~ NOPE. They are unique. NEXT!`);
          console.log(`--------------------------------------------------`);
        }
      }
    }
  }
  return uniqueIntegers;
};

console.log(isUnique([1, 1, 3])); // should return false
console.log(isUnique([1, 2, 3])); // should return true
// console.log(isUnique([-1, 2, 3])); // should return true
// console.log(isUnique([11, 35, 51, 91, 82, 51])); // should return false

// console.log(isUnique([1, 2, 3]) === true);
// console.log(isUnique([1, 1, 3]) === false);
