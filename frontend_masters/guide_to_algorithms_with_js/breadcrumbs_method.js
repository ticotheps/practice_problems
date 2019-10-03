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
// Runtime Complexity = O(n)
// Space Complexity = O(n)
const isUnique = arr => {
  const breadcrumbs = {};
  let uniqueNumsInArr = true;

  for (let i = 0; i < arr.length; i++) {
    console.log(`\nLOOP, i === ${i}`);
    console.log('~~~ breadcrumbs =', breadcrumbs);
    console.log(`~~~ arr[${i}] = ${arr[i]}`);

    if (breadcrumbs[arr[i]]) {
      console.log(`~~~ The value, ${arr[i]}, ALREADY DOES exist as a key in`);
      console.log(`~~~ the 'breadcrumbs' object. We have a DUPLICATE!`);
      uniqueNumsInArr = false;
      return uniqueNumsInArr;
    } else {
      console.log(`~~~ The value, ${arr[i]}, DOES NOT yet exist as a key in`);
      console.log(`~~~ the 'breadcrumbs' object so we will add it in.`);
      breadcrumbs[arr[i]] = true;
    }
  }
  return uniqueNumsInArr;
};

console.log(isUnique([1, 1, 3])); // should return false
// console.log(isUnique([1, 2, 3])); // should return true
