const assert = require('assert');

const exampleString1 = 'Dad';
const exampleString2 = 'aba';
const exampleString3 = 'Dad:Tic!';
const exampleString4 = 'rotor';
const exampleString5 = '1009001';
const exampleString6 = '%@#@%';
const exampleString7 = 'a%@#@%b';

function checkPalindrome(string) {
  // console.time('checkPalindrome');
  // console.log('string = ', string);

  let regEx = /[\W_]/g;

  let newString = string.toLowerCase().replace(regEx, '');
  // console.log('newString = ', newString);

  let reversedString = newString
    .split('')
    .reverse()
    .join('');
  // console.log('reversedString = ', reversedString);

  if (newString === reversedString) {
    return true;
  } else {
    return false;
  }
}

//----------TESTS----------

assert.deepStrictEqual(
  true,
  checkPalindrome(exampleString1),
  "'Dad' is a palindrome"
);
// console.log(checkPalindrome(exampleString1)); // true
// console.timeEnd('checkPalindrome');

assert.deepStrictEqual(
  true,
  checkPalindrome(exampleString2),
  "'aba' is a palindrome"
);
// console.log(checkPalindrome(exampleString2)); // true
// console.timeEnd('checkPalindrome');

assert.deepStrictEqual(
  false,
  checkPalindrome(exampleString3),
  "'Dad:Tic!' is NOT a palindrome"
);
// console.log(checkPalindrome(exampleString3)); // false
// console.timeEnd('checkPalindrome');

assert.deepStrictEqual(
  true,
  checkPalindrome(exampleString4),
  "'rotor' is a palindrome"
);
// console.log(checkPalindrome(exampleString4)); // true
// console.timeEnd('checkPalindrome');

assert.deepStrictEqual(
  true,
  checkPalindrome(exampleString5),
  "'1009001' is a palindrome"
);
// console.log(checkPalindrome(exampleString5)); // true
// console.timeEnd('checkPalindrome');

assert.deepStrictEqual(
  true,
  checkPalindrome(exampleString6),
  "'%@#@%' is a palindrome"
);
// console.log(checkPalindrome(exampleString6)); // true
// console.timeEnd('checkPalindrome');

assert.deepStrictEqual(
  false,
  checkPalindrome(exampleString7),
  "'a%@#@%b' is a palindrome"
);
// console.log(checkPalindrome(exampleString7)); // false
// console.timeEnd('checkPalindrome');

console.log('7 of 7 TESTS HAVE PASSED!');
