/* 
Expected Input: 
  - an array of numbers

Expected Output:  
  - if the array contains NO duplicate numbers, return true
  - if the array contains duplicate numbers, return false
  
Constraints:
  - none
*/

const isUnique = arr => {
  let uniqueNumsInArr = true;

  for (let i = 0; i < arr.length; i++) {
    // console.log(`~~~~ ** OUTER LOOP ** ~~~~ * i * === ${i}`);

    for (let j = 0; j < arr.length; j++) {
      // console.log(`~~~~ INNER LOOP ~~~~ j === ${j}`);
      if (i !== j && arr[i] === arr[j]) {
        uniqueNumsInArr = false;
      }
    }
  }

  return uniqueNumsInArr;
};

// console.log(isUnique([1, 2, 3]) === true);

// console.log(isUnique([1, 1, 3]) === false);

console.log(isUnique([11, 35, 51, 91, 82, 51])); // should return false
console.log(isUnique([1, 1, 3])); // should return false
console.log(isUnique([1, 2, 3])); // should return true
console.log(isUnique([-1, 2, 3])); // should return true
