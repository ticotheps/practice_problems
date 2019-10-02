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
  const breadcrumbs = {};
  let uniqueNumsInArr = true;

  for (let i = 0; i < arr.length; i++) {
    console.log(`~~~~ Loop ~~~~ i === ${i}`);

    if (breadcrumbs[arr[i]]) {
      uniqueNumsInArr = false;
    } else {
      breadcrumbs[arr[i]] = true;
    }
  }

  return uniqueNumsInArr;
};

console.log(isUnique([1, 2, 3])); // should return true
console.log(isUnique([1, 1, 3])); // should return false

// Runtime Complexity of Breadcrumbs (caching) Method = O(n)
