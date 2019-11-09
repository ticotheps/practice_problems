// Space Complexity

// Example 1
function booooo(n) {
  for (let i = 0; i < n.length; i++) {
    console.log('booooo!');
  }
}

booooo([1, 2, 3, 4, 5]); // O(1) constant space complexity

// Example 2
function arrayOfHiNTimes(n) {
  let hiArray = [];

  for (let i = 0; i < n; i++) {
    hiArray[i] = 'hi';
  }
  return hiArray;
}

console.log(arrayOfHiNTimes(6)); // O(n)
