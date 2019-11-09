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

// Example 3

// Find 1st, Find nth...
const arr = [
  { tweet: 'hi', date: 2012 },
  { twee: 'my', date: 2014 },
  { tweet: 'teddy', date: 2018 },
];
arr[0]; // O(1)
arr[arr.length - 1]; // O(1)

// Example 4

// Compare the dates from each object in the array...
// O(n^2) because you will use nested "for" loops to
// compare the items from each object from the array
const arrOfObj = [
  { tweet: 'hi', date: 2012 },
  { twee: 'my', date: 2014 },
  { tweet: 'teddy', date: 2018 },
];
