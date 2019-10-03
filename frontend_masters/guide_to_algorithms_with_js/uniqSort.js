/* 
Task: Transform this simple sorting algorithm into a unique sort.

It should not return any duplicate values in the sorted array.
*/

// input: [1, 5, 2, 1] => output: [1, 2, 5]
// input: [4, 2, 2, 3, 2, 2] => output: [2, 3, 4]

const uniqSort = arr => {
  const breadcrumbs = {};
  const uniqNumsArr = [];

  for (let i = 0; i < arr.length; i++) {
    console.log(`~~~~ LOOP ~~~~ i === ${i}`);

    if (!breadcrumbs[arr[i]]) {
      breadcrumbs[arr[i]] = true;
      uniqNumsArr.push(arr[i]);
    }
  }

  return uniqNumsArr.sort((a, b) => a - b);
};

console.log(uniqSort([4, 2, 2, 3, 2, 2, 2])); // => [2, 3, 4]
console.log(uniqSort([-7, 2, 3, 3, 10, 3, 5])); // => [-7, 2, 3, 5, 10]
console.log(uniqSort([-7, -22, 3, 45, 4, 199, 4])); // => [-7, 2, 3, 5, 10]
